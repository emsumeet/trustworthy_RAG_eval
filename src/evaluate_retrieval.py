import json
import os

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer


DATA_PATH = "data/processed/hotpotqa_validation_100.json"
OUTPUT_PATH = "results/retrieval_baseline.csv"

K_VALUES = [1, 3, 5, 10]

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def load_data():
    with open(
        DATA_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def extract_documents(example):
    """
    Convert HotpotQA context into:

    [
        {
            "title": "...",
            "text": "..."
        }
    ]
    """

    context = example["context"]

    titles = context["title"]
    sentences = context["sentences"]

    documents = []

    for title, sentence_list in zip(
        titles,
        sentences
    ):
        text = " ".join(sentence_list)

        documents.append({
            "title": title,
            "text": text
        })

    return documents


def get_gold_titles(example):
    """
    Return unique supporting-document titles.
    """

    titles = example[
        "supporting_facts"
    ]["title"]

    return set(titles)


def retrieve(
    question,
    documents,
    model
):
    """
    Rank documents using dense embeddings
    and cosine similarity.
    """

    document_texts = [
        doc["text"]
        for doc in documents
    ]

    question_embedding = model.encode(
        question,
        normalize_embeddings=True
    )

    document_embeddings = model.encode(
        document_texts,
        normalize_embeddings=True
    )

    # Because embeddings are normalized,
    # dot product = cosine similarity
    scores = np.dot(
        document_embeddings,
        question_embedding
    )

    ranked_indices = np.argsort(
        scores
    )[::-1]

    ranked_documents = []

    for index in ranked_indices:
        ranked_documents.append({
            "title": documents[index]["title"],
            "score": float(scores[index])
        })

    return ranked_documents


def calculate_metrics(
    ranked_documents,
    gold_titles,
    k
):
    top_k = ranked_documents[:k]

    retrieved_titles = {
        doc["title"]
        for doc in top_k
    }

    retrieved_gold = (
        retrieved_titles &
        gold_titles
    )

    supporting_recall = (
        len(retrieved_gold) /
        len(gold_titles)
    )

    complete_evidence = (
        gold_titles.issubset(
            retrieved_titles
        )
    )

    return (
        supporting_recall,
        int(complete_evidence)
    )


def main():

    print(
        "Loading HotpotQA evaluation subset..."
    )

    data = load_data()

    print(
        f"Loaded {len(data)} questions."
    )

    print()
    print(
        f"Loading embedding model: "
        f"{MODEL_NAME}"
    )

    model = SentenceTransformer(
        MODEL_NAME
    )

    print()
    print("Evaluating retrieval...")
    print()

    results = []

    for question_number, example in enumerate(
        data,
        start=1
    ):

        question = example["question"]

        documents = extract_documents(
            example
        )

        gold_titles = get_gold_titles(
            example
        )

        ranked_documents = retrieve(
            question,
            documents,
            model
        )

        for k in K_VALUES:

            (
                supporting_recall,
                complete_evidence
            ) = calculate_metrics(
                ranked_documents,
                gold_titles,
                k
            )

            top_titles = [
                doc["title"]
                for doc
                in ranked_documents[:k]
            ]

            results.append({
                "question_id": example["id"],
                "question": question,
                "k": k,
                "gold_titles": list(
                    gold_titles
                ),
                "retrieved_titles":
                    top_titles,
                "supporting_document_recall":
                    supporting_recall,
                "complete_evidence":
                    complete_evidence
            })

        if question_number % 10 == 0:
            print(
                f"Processed "
                f"{question_number}/"
                f"{len(data)} questions"
            )

    dataframe = pd.DataFrame(
        results
    )

    os.makedirs(
        "results",
        exist_ok=True
    )

    dataframe.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print()
    print("==============================")
    print(" Retrieval Results")
    print("==============================")
    print()

    for k in K_VALUES:

        subset = dataframe[
            dataframe["k"] == k
        ]

        avg_recall = subset[
            "supporting_document_recall"
        ].mean()

        complete_rate = subset[
            "complete_evidence"
        ].mean()

        print(f"k = {k}")
        print(
            f"  Supporting Document "
            f"Recall@{k}: "
            f"{avg_recall:.3f}"
        )
        print(
            f"  Complete Evidence "
            f"Rate@{k}: "
            f"{complete_rate:.3f}"
        )
        print()

    print(
        f"Detailed results saved to: "
        f"{OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()
