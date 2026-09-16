# Experiment 01D — Qualitative Failure Analysis

## Research Question

Why do some RAG answers fail even when all annotated supporting documents are retrieved, and why do some answers succeed when the complete annotated evidence set is not retrieved?

## Objective

Experiment 01D qualitatively inspects representative examples from two surprising categories identified in Experiment 01C:

1. Complete annotated evidence retrieved + Exact Match failure
2. Incomplete annotated evidence retrieved + Exact Match success

The purpose is to determine whether the automatic categories correspond to true retrieval or generation failures, or whether some are artifacts of the evaluation metrics.

## Sampling

A deterministic sample was extracted using random seed 42.

Reviewed sample:

- 10 examples from Complete Evidence + Exact Match Failure
- 10 examples from Incomplete Evidence + Exact Match Success

Total manually reviewed examples: 20

## Findings — Complete Evidence + Exact Match Failure

Among the 10 reviewed examples:

| Primary qualitative category | Count |
|---|---:|
| Refusal despite sufficient evidence | 4 |
| Final-hop reasoning / answer extraction failure | 2 |
| Answer-type mismatch / insufficient abstraction | 2 |
| Exact Match false negative / semantic-equivalence mismatch | 2 |

### Interpretation

Eight of the ten reviewed examples appear to represent genuine generation-stage problems under the available evidence:

- refusal despite available evidence;
- failure to complete a final reasoning hop;
- failure to return the requested answer type;
- multi-hop relation-resolution problems.

However, two examples were semantically correct answers that were scored as failures by Exact Match.

Examples included:

- `Dirk Nowitzki` vs. gold `Dirk Werner Nowitzki`
- `The Royal Air Force (RAF)` vs. gold `Royal Air Force`

These cases show that Exact Match can underestimate true answer correctness.

## Findings — Incomplete Evidence + Exact Match Success

Among the 10 reviewed examples:

| Primary qualitative category | Count |
|---|---:|
| Partial evidence appears sufficient | 5 |
| Partial evidence sufficient / possible parametric-knowledge assistance | 4 |
| Alternative evidence / partial evidence sufficient | 1 |

All 10 reviewed examples suggest that failure to retrieve every annotated supporting document does not necessarily imply that the model lacked enough information to answer correctly.

Possible explanations include:

- one retrieved document already contained sufficient evidence;
- the question could be answered from an alternative evidence path;
- the model supplemented retrieved context with parametric knowledge;
- HotpotQA supporting-document annotations are useful gold evidence but are not necessarily the only sufficient evidence path.

The current experiment cannot distinguish these explanations without inspecting the full retrieved passage text and controlling model knowledge.

## Methodological Refinement

Experiment 01C originally used the labels:

- Retrieval Success + Generation Success
- Retrieval Success + Generation Failure
- Retrieval Failure + Generation Success
- Retrieval Failure + Generation Failure

Experiment 01D shows that these labels can imply stronger causal conclusions than the metrics support.

A more precise terminology is:

- Complete Evidence + Exact Match Pass
- Complete Evidence + Exact Match Fail
- Incomplete Evidence + Exact Match Pass
- Incomplete Evidence + Exact Match Fail

This terminology describes what was measured without assuming that:

- incomplete annotated evidence always means true retrieval failure; or
- Exact Match failure always means true generation failure.

## Revised Interpretation of Experiment 01

The quantitative results from Experiment 01 remain valid as metric measurements.

However, the qualitative analysis changes how those metrics should be interpreted.

### Retrieval depth

Supporting-document recall and complete-evidence rate increased as k increased:

| k | Supporting Recall | Complete Evidence |
|---:|---:|---:|
| 1 | 0.430 | 0.000 |
| 3 | 0.715 | 0.450 |
| 5 | 0.825 | 0.650 |
| 10 | 1.000 | 1.000 |

### Generation

Generation performance also improved at larger retrieval depths:

| k | Exact Match | Token F1 |
|---:|---:|---:|
| 0 | 0.240 | 0.326 |
| 1 | 0.200 | 0.276 |
| 3 | 0.210 | 0.309 |
| 5 | 0.330 | 0.452 |
| 10 | 0.390 | 0.559 |

At low retrieval depths, k=1 and k=3 performed below the no-retrieval baseline.

At k=5 and k=10, generation performance improved substantially.

### Failure decomposition

Experiment 01C produced the following metric-defined decomposition:

| k | Complete Evidence + EM Pass | Complete Evidence + EM Fail | Incomplete Evidence + EM Pass | Incomplete Evidence + EM Fail |
|---:|---:|---:|---:|---:|
| 1 | 0% | 0% | 20% | 80% |
| 3 | 16% | 29% | 5% | 50% |
| 5 | 25% | 40% | 8% | 27% |
| 10 | 39% | 61% | 0% | 0% |

At k=10, all annotated supporting documents were retrieved, while Exact Match was only 39%.

This demonstrates that complete annotated retrieval alone does not guarantee an Exact Match answer.

However, Experiment 01D also shows that some Exact Match failures are actually semantically correct answers.

Therefore, the 61% Complete Evidence + EM Fail rate at k=10 should not automatically be interpreted as a 61% true generation-failure rate.

## Main Conclusions

Experiment 01 supports four main conclusions:

1. Increasing retrieval depth improves annotated evidence coverage in the HotpotQA distractor setting.
2. Incomplete retrieval at low k can correspond to weaker generation performance than the no-retrieval baseline.
3. Complete annotated evidence does not guarantee correct answer generation.
4. Strict automatic metrics can mischaracterize both retrieval and generation behavior.

The fourth finding is especially important for trustworthy RAG evaluation: reliability analysis should evaluate not only the RAG system, but also the assumptions built into the evaluation metrics.

## Limitations

- Only 20 examples were manually reviewed.
- The qualitative sample should not be used to estimate population-wide corrected error rates.
- Exact Match remains useful for reproducible benchmarking but is not sufficient for semantic correctness.
- Complete supporting-document retrieval is useful for benchmark evaluation but does not prove that no alternative sufficient evidence path exists.
- The current setup uses one dense retriever and one local generator.
- HotpotQA distractor retrieval is easier than open-corpus retrieval.

## Next Research Direction

Experiment 01 is now complete as an initial study.

A natural next experiment is to compare retrieval methods while preserving the same dataset and evaluation framework, for example:

- BM25 sparse retrieval;
- dense retrieval;
- hybrid retrieval;
- reranking.

A later evaluation extension should also introduce semantic answer equivalence and evidence-grounded faithfulness metrics.
