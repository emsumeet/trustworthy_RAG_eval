# Experiment 01 — Effect of Retrieval Depth on RAG Reliability

## Research Question

How does retrieval depth (k) affect retrieval quality, evidence coverage,
and factual reliability in a Retrieval-Augmented Generation system?

---

## Hypothesis

Increasing retrieval depth should initially improve evidence coverage.

However, after a certain point, adding more retrieved documents may
introduce irrelevant information and retrieval noise without improving
answer reliability.

Therefore, answer quality is not expected to improve monotonically as
retrieval depth increases.

---

## Dataset

HotpotQA — distractor configuration.

Initial evaluation subset:

- Split: validation
- Sample size: 100 questions
- Random seed: 42

Each example contains:

- question
- gold answer
- question type
- difficulty level
- supporting facts
- candidate context documents

---

## Experimental Conditions

The following configurations will be compared:

1. No Retrieval
2. RAG with k = 1
3. RAG with k = 3
4. RAG with k = 5
5. RAG with k = 10

The same generation model and prompt will be used for all RAG
configurations.

Only retrieval depth will change.

---

## Retrieval Unit

The initial retrieval unit will be a document/paragraph from the
HotpotQA candidate context.

Each context paragraph will be represented independently in the
retrieval index.

---

## Retrieval Method

Initial baseline:

Dense semantic retrieval using sentence embeddings and cosine similarity.

The same embedding model will be used across all k conditions.

Later experiments may compare:

- BM25
- dense retrieval
- hybrid retrieval
- reranking

---

## Retrieval Metrics

### Supporting Document Recall@K

Measures whether the gold supporting documents appear in the top-k
retrieved documents.

### Complete Evidence Recall@K

Measures whether all gold supporting documents required to answer the
question are present in the top-k retrieved set.

### Evidence Coverage

Measures the proportion of required supporting evidence retrieved.

---

## Generation Metrics

### Exact Match

Whether the generated answer exactly matches the gold answer after
normalization.

### Token-Level F1

Measures overlap between the generated answer and gold answer.

### Answer Faithfulness

Measures whether the generated answer is supported by retrieved evidence.

Faithfulness evaluation will be added after the baseline pipeline is
working.

---

## Controlled Variables

The following will remain fixed:

- dataset subset
- random seed
- embedding model
- generation model
- generation prompt
- temperature
- answer-length constraints

Only retrieval depth k will vary in Experiment 01.

---

## Outputs

Results will be saved in machine-readable form.

Example columns:

question_id
question
gold_answer
k
retrieved_documents
supporting_document_recall
complete_evidence_retrieved
generated_answer
exact_match
f1
latency

---

## Failure Analysis

Failed examples will later be categorized as:

1. Required evidence not retrieved
2. Only part of the required evidence retrieved
3. Correct evidence retrieved but answer incorrect
4. Irrelevant retrieval distracted the generator
5. Correct answer generated despite missing evidence
6. Unsupported or hallucinated answer

---

## Initial Success Criterion

The first experiment is not intended to prove that one value of k is
universally optimal.

The goal is to determine whether measurable trade-offs appear between:

- retrieval depth
- evidence coverage
- answer accuracy
- retrieval noise
- computation cost

---

## Reproducibility

Random seed: 42

Initial sample size: 100 HotpotQA validation examples.

All experiment configurations and results will be version-controlled.
