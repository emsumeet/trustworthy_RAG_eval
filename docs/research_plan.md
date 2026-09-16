# Trustworthy RAG Evaluation — Research Plan

## Research Objective

This project investigates how retrieval quality and evidence sufficiency affect the reliability of Retrieval-Augmented Generation systems.

The primary goal is to determine whether improving retrieval automatically improves generated answers, and to identify cases where retrieval and generation fail independently.

---

## Primary Research Question

How do retrieval quality and evidence sufficiency influence answer reliability in Retrieval-Augmented Generation systems?

---

## Motivation

RAG systems provide language models with external information before generation.

However, retrieving documents does not guarantee that generated claims are supported by those documents.

Failures can occur because:

- relevant evidence was not retrieved;
- only part of the required evidence was retrieved;
- irrelevant documents introduced noise;
- retrieved sources contained conflicting information;
- the generator ignored retrieved evidence;
- the model relied on parametric knowledge;
- the system answered despite insufficient evidence.

This project studies these failure modes experimentally.

---

# Hypotheses

## H1 — Retrieval Quality

Higher-quality retrieval should increase the likelihood of correct and evidence-supported answers.

---

## H2 — Evidence Sufficiency

Retrieval relevance alone is not sufficient.

Questions requiring multiple pieces of evidence may fail when only part of the required evidence is retrieved.

---

## H3 — Retrieval Depth

Increasing retrieval depth should initially improve evidence coverage.

However, additional documents may introduce retrieval noise.

Therefore, generation quality may not improve monotonically as retrieval depth increases.

---

# Experiment Roadmap

## Experiment 01

Effect of retrieval depth on RAG reliability.

Conditions:

```text
No retrieval
k = 1
k = 3
k = 5
k = 10
```

### Experiment 01A

Evaluate retrieval quality.

Metrics:

- Supporting Document Recall@K
- Complete Evidence Rate@K

### Experiment 01B

Evaluate generated answers.

Metrics:

- Exact Match
- Token-level F1

---

# Future Experiments

Planned experiments include:

- BM25 vs dense retrieval
- hybrid retrieval
- reranking
- query decomposition
- multi-hop retrieval
- controlled retrieval noise
- contradictory evidence
- adaptive retrieval depth
- evidence insufficiency detection
- model abstention
- uncertainty calibration
- factuality evaluation
- citation evaluation

---

# Research Output Goals

The project is intended to produce:

- reproducible experiments,
- quantitative results,
- controlled comparisons,
- failure analysis,
- ablation studies,
- visualizations,
- a technical research report,
- and potentially a workshop or preprint submission.
