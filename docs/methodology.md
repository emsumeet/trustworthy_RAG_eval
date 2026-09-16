# Methodology

## 1. Dataset

The project uses the HotpotQA dataset.

Configuration:

```text
distractor
```

Split:

```text
validation
```

The validation split contains 7,405 examples.

A reproducible subset of 100 questions is sampled using:

```text
Random seed: 42
```

The processed subset is stored locally as:

```text
data/processed/hotpotqa_validation_100.json
```

Each example includes:

- question
- gold answer
- supporting facts
- candidate context documents
- supporting document titles

---

## 2. Retrieval Model

Dense retrieval uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

For every question:

1. The question is embedded.
2. Candidate documents are embedded.
3. Embeddings are L2-normalized.
4. Cosine similarity is calculated.
5. Documents are ranked by similarity.
6. The top-k documents are selected.

---

## 3. Experimental Conditions

Experiment 01 evaluates:

```text
k = 0
k = 1
k = 3
k = 5
k = 10
```

`k=0` represents the no-retrieval generation baseline.

---

## 4. Retrieval Metrics

### Supporting Document Recall@K

Calculated as:

```text
Retrieved gold supporting documents
-----------------------------------
Total gold supporting documents
```

The score is averaged across the evaluation set.

---

### Complete Evidence Rate@K

For each question:

```text
1 = all required supporting documents retrieved
0 = one or more required documents missing
```

The average gives the complete-evidence retrieval rate.

---

## 5. Generation Model

Generation uses:

```text
llama3.2:3b
```

through Ollama.

Temperature:

```text
0
```

The model is instructed to return a short answer.

For retrieval-based conditions, it is instructed to answer using only the supplied evidence.

If evidence is insufficient, the prompt permits:

```text
INSUFFICIENT_EVIDENCE
```

---

## 6. Generation Metrics

### Exact Match

Generated and gold answers are normalized by:

- lowercase conversion,
- punctuation removal,
- article removal,
- whitespace normalization.

Exact Match is:

```text
1 = normalized prediction equals normalized gold answer
0 = otherwise
```

---

### Token-Level F1

Token-level precision and recall are calculated between prediction and gold-answer tokens.

Their harmonic mean gives token-level F1.

---

## 7. Controlled Variables

The following remain fixed during Experiment 01B:

```text
Dataset subset
Random seed
Retriever
Embedding model
Generator
Prompt structure
Temperature
Answer format
```

The primary manipulated variable is:

```text
retrieval depth k
```

---

## 8. Failure Decomposition

Examples will be separated into:

### Retrieval Failure + Generation Failure

Required evidence was not completely retrieved and the answer was incorrect.

### Retrieval Success + Generation Success

Complete supporting evidence was retrieved and the answer was correct.

### Retrieval Success + Generation Failure

Complete evidence was available but the model still generated an incorrect answer.

This isolates generation-stage failures.

### Retrieval Failure + Generation Success

The answer is correct despite incomplete annotated evidence.

Potential explanations include:

- partial evidence was sufficient,
- the model relied on parametric knowledge,
- alternative evidence supported the answer.

These cases require manual inspection.

---

## 9. Current Limitations

### Restricted Candidate Corpus

HotpotQA distractor provides a limited candidate context for each question.

This is easier than full-corpus retrieval.

### k=10 Condition

At k=10, all candidate documents are effectively retrieved.

Therefore, perfect retrieval coverage at k=10 is expected in this experimental setting.

### Single Retriever

Only one dense retriever is currently evaluated.

### Single Generator

Only one generation model is currently evaluated.

### Automated Answer Metrics

Exact Match and token-level F1 do not directly measure factual faithfulness.

Future experiments will add evidence-grounding metrics.

---

## 10. Planned Methodological Extensions

Future work will examine:

- BM25
- hybrid retrieval
- reranking
- query decomposition
- multi-step retrieval
- retrieval noise
- contradictory evidence
- adaptive retrieval
- factual consistency
- answer faithfulness
- citation precision
- citation recall
- uncertainty estimation
- abstention behavior
