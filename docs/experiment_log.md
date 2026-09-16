# Experiment Log

# Experiment 01A — Dense Retrieval Baseline

## Objective

Measure how retrieval depth affects supporting-document recall and complete evidence retrieval.

## Dataset

```text
Dataset: HotpotQA
Configuration: distractor
Split: validation
Sample size: 100
Random seed: 42
```

## Retriever

```text
sentence-transformers/all-MiniLM-L6-v2
```

Similarity:

```text
Cosine similarity
```

---

## Results

| k | Supporting Document Recall@K | Complete Evidence Rate@K |
|---|---:|---:|
| 1 | 0.430 | 0.000 |
| 3 | 0.715 | 0.450 |
| 5 | 0.825 | 0.650 |
| 10 | 1.000 | 1.000 |

---

## Observation

Increasing retrieval depth substantially increased evidence coverage.

At `k=1`, average supporting-document recall was 0.430 and complete evidence was not retrieved for any evaluated question.

At `k=3`, recall increased to 0.715 and the complete-evidence rate reached 0.450.

At `k=5`, recall increased to 0.825 and complete-evidence retrieval reached 0.650.

At `k=10`, both metrics reached 1.000.

---

## Limitation

The `k=10` result should not be interpreted as showing that k=10 is universally optimal.

The HotpotQA distractor setting provides a restricted candidate context. Retrieving all candidate documents therefore guarantees inclusion of the gold supporting documents.

The generation experiment is required to determine whether the extra distractor context helps or harms final answer quality.

---

# Experiment 01B — Generation Baseline

## Objective

Determine whether increased retrieval depth and evidence coverage translate into improved answer quality.

## Generator

```text
llama3.2:3b
```

served locally through Ollama.

Temperature:

```text
0
```

---

## Experimental Conditions

```text
k = 0
k = 1
k = 3
k = 5
k = 10
```

---

## Metrics

- Exact Match
- Token-level F1

---

## Pilot Experiment

A five-question pilot was performed before the full experiment.

Total generations:

```text
5 questions × 5 conditions = 25
```

### Pilot Results

| k | Exact Match | Token F1 |
|---|---:|---:|
| 0 | 0.200 | 0.257 |
| 1 | 0.000 | 0.000 |
| 3 | 0.000 | 0.040 |
| 5 | 0.200 | 0.231 |
| 10 | 0.600 | 0.773 |

These values are treated only as pipeline-validation results because the sample contains five questions.

No conclusions about optimal retrieval depth are drawn from the pilot.

---

# Full Experiment

Total generations:

```text
100 questions × 5 conditions = 500
```

## Results

Pending.

| k | Exact Match | Token F1 |
|---|---:|---:|
| 0 | Pending | Pending |
| 1 | Pending | Pending |
| 3 | Pending | Pending |
| 5 | Pending | Pending |
| 10 | Pending | Pending |

---

## Planned Analysis

After completion, the results will be combined with Experiment 01A to analyze:

```text
retrieval depth
        ↓
evidence coverage
        ↓
generation accuracy
```

Particular attention will be given to:

- retrieval success + generation success,
- retrieval success + generation failure,
- retrieval failure + generation failure,
- retrieval failure + generation success.
