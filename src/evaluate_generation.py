import json
import os
import re
import string
from collections import Counter

import numpy as np
import pandas as pd
import requests
from sentence_transformers import SentenceTransformer


DATA_PATH = "data/processed/hotpotqa_validation_100.json"
OUTPUT_PATH = "results/generation_baseline.csv"

K_VALUES = [0, 1, 3, 5, 10]

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
GENERATION_MODEL = "llama3.2:3b"

OLLAMA_URL = "http://localhost:11434/api/generate"


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def extract_documents(example):
    context = example["context"]
    documents = []

    for title, sentences in zip(context["title"], context["sentences"]):
        documents.append({
            "title": title,
            "text": " ".join(sentences)
        })

    return documents


def retrieve(question, documents, model):
    texts = [doc["text"] for doc in documents]

    question_embedding = model.encode(
        question,
        normalize_embeddings=True
    )

    document_embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    scores = np.dot(document_embeddings, question_embedding)
    ranked_indices = np.argsort(scores)[::-1]

    return [
        {
            "title": documents[i]["title"],
            "text": documents[i]["text"],
            "score": float(scores[i])
        }
        for i in ranked_indices
    ]


def build_prompt(question, documents, k):
    if k == 0:
        return f"""
Answer the following question.

Return only the short answer.
Do not explain your reasoning.

Question:
{question}

Answer:
""".strip()

    context_parts = []

    for doc in documents[:k]:
        context_parts.append(
            f"Title: {doc['title']}\n"
            f"{doc['text']}"
        )

    context = "\n\n".join(context_parts)

    return f"""
Answer the question using only the evidence provided below.

If the evidence is insufficient, answer exactly:
INSUFFICIENT_EVIDENCE

Return only the short answer.
Do not explain your reasoning.

Evidence:
{context}

Question:
{question}

Answer:
""".strip()


def generate_answer(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": GENERATION_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0
            }
        },
        timeout=180
    )

    response.raise_for_status()
    return response.json()["response"].strip()


def normalize_answer(text):
    def remove_articles(value):
        return re.sub(r"\b(a|an|the)\b", " ", value)

    def remove_punctuation(value):
        return "".join(
            character
            for character in value
            if character not in string.punctuation
        )

    def fix_whitespace(value):
        return " ".join(value.split())

    text = text.lower()
    text = remove_punctuation(text)
    text = remove_articles(text)
    text = fix_whitespace(text)

    return text


def exact_match(prediction, gold):
    return int(
        normalize_answer(prediction)
        ==
        normalize_answer(gold)
    )


def token_f1(prediction, gold):
    prediction_tokens = normalize_answer(prediction).split()
    gold_tokens = normalize_answer(gold).split()

    common = Counter(prediction_tokens) & Counter(gold_tokens)
    num_same = sum(common.values())

    if len(prediction_tokens) == 0:
        return float(len(gold_tokens) == 0)

    if len(gold_tokens) == 0:
        return 0.0

    if num_same == 0:
        return 0.0

    precision = num_same / len(prediction_tokens)
    recall = num_same / len(gold_tokens)

    return 2 * precision * recall / (precision + recall)


def main():
    print("Loading dataset...")
    data = load_data()

    print(f"Loaded {len(data)} questions.")
    print()
    print("Loading embedding model...")

    embedding_model = SentenceTransformer(EMBEDDING_MODEL)

    results = []
    total_runs = len(data) * len(K_VALUES)
    run_number = 0

    for example in data:
        question = example["question"]
        gold_answer = example["answer"]

        documents = extract_documents(example)

        ranked_documents = retrieve(
            question,
            documents,
            embedding_model
        )

        for k in K_VALUES:
            run_number += 1

            print(
                f"[{run_number}/{total_runs}] "
                f"k={k} | {question[:60]}"
            )

            prompt = build_prompt(
                question,
                ranked_documents,
                k
            )

            try:
                generated_answer = generate_answer(prompt)

            except Exception as error:
                print(f"Generation error: {error}")
                generated_answer = "GENERATION_ERROR"

            em = exact_match(generated_answer, gold_answer)
            f1 = token_f1(generated_answer, gold_answer)

            retrieved_titles = [
                document["title"]
                for document in ranked_documents[:k]
            ]

            results.append({
                "question_id": example["id"],
                "question": question,
                "gold_answer": gold_answer,
                "k": k,
                "generated_answer": generated_answer,
                "exact_match": em,
                "f1": f1,
                "retrieved_titles": retrieved_titles
            })

    dataframe = pd.DataFrame(results)

    os.makedirs("results", exist_ok=True)

    dataframe.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print()
    print("==============================")
    print(" Generation Results")
    print("==============================")
    print()

    for k in K_VALUES:
        subset = dataframe[dataframe["k"] == k]

        print(f"k = {k}")
        print(
            f"  Exact Match: "
            f"{subset['exact_match'].mean():.3f}"
        )
        print(
            f"  Token F1:    "
            f"{subset['f1'].mean():.3f}"
        )
        print()

    print(
        f"Detailed results saved to: "
        f"{OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()
