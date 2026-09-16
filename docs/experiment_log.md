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
| 0 | 0.240 | 0.326 |
| 1 | 0.200 | 0.276 |
| 3 | 0.210 | 0.309 |
| 5 | 0.330 | 0.452 |
| 10 | 0.390 | 0.559 |

---

## Combined Exp 01 Results

Combined Experiment 01 Results

| k  |	Supporting Recall.  |	Complete Evidence.   |	Exact Match.  |	Token F1 |
|---|---:|---:|
|0	|—	|—	|0.240	|0.326|
|1	|0.430	|0.000	|0.200	|0.276|
|3	|0.715	|0.450	|0.210	|0.309|
|5	|0.825	|0.650	|0.330	|0.452|
|10	|1.000	|1.000	|0.390	|0.559|

---

## Initial Analysis
Experiment 01A showed a monotonic increase in retrieval coverage as k
increased.
Generation performance showed a different pattern.
The no-retrieval baseline achieved:
- Exact Match: 0.240
- Token F1: 0.326
At k=1, generation performance decreased despite retrieved context being
provided.
At k=3, retrieval recall increased to 0.715 and complete evidence reached
0.450, but generation performance remained slightly below the
no-retrieval baseline.
At k=5, Exact Match increased to 0.330 and Token F1 to 0.452.
At k=10, where complete annotated supporting evidence was available for
all evaluated questions, Exact Match reached 0.390 and Token F1 reached
0.559.
These results indicate that retrieval presence alone does not guarantee
better generation.
One possible explanation is that incomplete evidence can create a
misleading or insufficient context for multi-hop reasoning.
However, this interpretation requires example-level failure analysis
before stronger conclusions can be drawn.
Next Analysis
The next stage will classify individual question-condition pairs into:
1. Retrieval success + generation success
2. Retrieval success + generation failure
3. Retrieval failure + generation success
4. Retrieval failure + generation failure
This will help determine whether failures originate primarily from the
retriever or the generator.
