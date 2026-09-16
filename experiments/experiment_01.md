# Experiment 01 — Effect of Retrieval Depth on RAG Reliability

## Research Question

How does retrieval depth affect evidence coverage and answer reliability in a Retrieval-Augmented Generation system?

---

## Hypothesis

Increasing retrieval depth should initially improve evidence coverage.

However, increasing k also introduces more irrelevant context.

Therefore, maximum retrieval depth may not necessarily produce maximum generation accuracy.

---

## Dataset

```text
HotpotQA
Configuration: distractor
Split: validation
Sample size: 100
Random seed: 42
```

---

## Experimental Conditions

```text
No retrieval
k = 1
k = 3
k = 5
k = 10
```

---

## Experiment 01A

### Objective

Evaluate retrieval performance independently of generation.

### Metrics

```text
Supporting Document Recall@K
Complete Evidence Rate@K
```

---

## Experiment 01B

### Objective

Measure whether retrieval improvements translate into generation improvements.

### Metrics

```text
Exact Match
Token-Level F1
```

---

## Controlled Variables

The following remain fixed:

```text
Dataset
Question subset
Random seed
Retriever
Generator
Prompt format
Temperature
Answer instructions
```

The primary independent variable is:

```text
retrieval depth k
```

---

## Analysis

Results from retrieval and generation will be compared to determine whether:

1. greater evidence coverage improves answer accuracy;
2. incomplete evidence leads to generation failures;
3. additional distractors negatively affect generation;
4. the generator sometimes succeeds despite retrieval failure.
