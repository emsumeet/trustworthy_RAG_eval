# Experiment 01C — Failure Decomposition

## Research Question

When a RAG system produces an incorrect answer, does the failure originate from retrieval or from generation?

## Objective

Experiment 01C combines the retrieval results from Experiment 01A with the generation results from Experiment 01B.

Each question-condition pair is assigned to one of four categories:

1. Retrieval Success + Generation Success
2. Retrieval Success + Generation Failure
3. Retrieval Failure + Generation Success
4. Retrieval Failure + Generation Failure

Retrieval success is defined as complete retrieval of the annotated gold supporting documents.

Generation success is defined using Exact Match.

## Results

| k | Retrieval Success + Generation Success | Retrieval Success + Generation Failure | Retrieval Failure + Generation Success | Retrieval Failure + Generation Failure |
|---:|---:|---:|---:|---:|
| 1 | 0% | 0% | 20% | 80% |
| 3 | 16% | 29% | 5% | 50% |
| 5 | 25% | 40% | 8% | 27% |
| 10 | 39% | 61% | 0% | 0% |

## Key Observation

At `k=10`, complete annotated supporting evidence was retrieved for every evaluated question.

However, only 39% of answers achieved Exact Match.

The remaining 61% were:

```text
Retrieval Success + Generation Failure
```

This shows that complete retrieval of annotated evidence does not guarantee successful answer generation.

## Retrieval Failure + Generation Success

At `k=1`, complete evidence was not available for any question, but 20% of generated answers were still correct.

At `k=3` and `k=5`, 5% and 8% respectively were also correct despite incomplete annotated evidence.

Possible explanations include:

- partial evidence being sufficient;
- model parametric knowledge;
- alternative evidence within retrieved documents;
- limitations of using annotated supporting-document completeness as the only definition of evidence sufficiency.

These cases require manual inspection.

## Interpretation

The results suggest two distinct reliability problems.

### Retrieval-stage failure

When required evidence is missing, generation frequently fails.

### Generation-stage failure

Even when complete annotated evidence is available, the generator can still produce incorrect answers.

At `k=10`:

```text
Complete Evidence Rate = 1.000
Exact Match = 0.390
```

Therefore, improving retrieval alone is unlikely to solve all RAG reliability failures.

## Limitations

Generation success is currently defined using Exact Match.

An answer may be semantically correct while failing Exact Match.

Future analysis should include:

- Token-level F1
- manual inspection
- semantic answer evaluation
- evidence-grounded faithfulness evaluation

Complete evidence is currently defined using HotpotQA gold supporting document annotations.

This does not prove that those documents represent the only possible sufficient evidence.

## Next Step

The next stage will inspect representative examples from:

- Retrieval Success + Generation Failure
- Retrieval Failure + Generation Success

The goal is to identify more specific failure modes such as:

- reasoning failure;
- answer extraction failure;
- distractor interference;
- parametric knowledge;
- partial-evidence sufficiency;
- refusal despite sufficient evidence;
- unsupported answer generation.
