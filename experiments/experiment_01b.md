# Experiment 01B — Retrieval Depth vs Answer Quality

## Research Question

Does increased retrieval depth and evidence coverage translate into improved generated-answer quality?

## Background

Experiment 01A produced:

| k | Supporting Recall | Complete Evidence |
|---:|---:|---:|
| 1 | 0.430 | 0.000 |
| 3 | 0.715 | 0.450 |
| 5 | 0.825 | 0.650 |
| 10 | 1.000 | 1.000 |

Experiment 01B evaluates whether these retrieval improvements also improve final answers.

## Generator

```text
llama3.2:3b
```

Inference:

```text
Ollama
```

Temperature:

```text
0
```

## Conditions

```text
k = 0
k = 1
k = 3
k = 5
k = 10
```

## Dataset

The same 100-question HotpotQA subset used in Experiment 01A is used here.

## Metrics

### Exact Match

Measures whether the normalized model answer exactly matches the normalized gold answer.

### Token-Level F1

Measures partial token overlap between prediction and gold answer.

## Full Results

| k | Exact Match | Token F1 |
|---:|---:|---:|
| 0 | 0.240 | 0.326 |
| 1 | 0.200 | 0.276 |
| 3 | 0.210 | 0.309 |
| 5 | 0.330 | 0.452 |
| 10 | 0.390 | 0.559 |

## Preliminary Finding

Retrieval improvements did not translate directly into generation improvements at low retrieval depths.

Both `k=1` and `k=3` performed below the no-retrieval baseline on the generation metrics.

Performance improved substantially at `k=5` and `k=10`, where supporting evidence coverage was higher.

This motivates example-level analysis of evidence sufficiency rather than treating retrieval depth alone as the explanatory variable.

## Planned Failure Analysis

- Retrieval Success + Generation Success
- Retrieval Success + Generation Failure
- Retrieval Failure + Generation Success
- Retrieval Failure + Generation Failure
