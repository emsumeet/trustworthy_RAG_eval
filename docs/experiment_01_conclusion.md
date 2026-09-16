# Experiment 01 — Final Interpretation

## Study Overview

Experiment 01 investigated how retrieval depth affects evidence coverage and answer quality in a controlled HotpotQA distractor setting.

The study was divided into four stages:

- **01A:** dense retrieval baseline;
- **01B:** generation baseline;
- **01C:** metric-based failure decomposition;
- **01D:** qualitative failure analysis.

## Quantitative Results

### Retrieval

| k | Supporting Recall | Complete Evidence |
|---:|---:|---:|
| 1 | 0.430 | 0.000 |
| 3 | 0.715 | 0.450 |
| 5 | 0.825 | 0.650 |
| 10 | 1.000 | 1.000 |

### Generation

| k | Exact Match | Token F1 |
|---:|---:|---:|
| 0 | 0.240 | 0.326 |
| 1 | 0.200 | 0.276 |
| 3 | 0.210 | 0.309 |
| 5 | 0.330 | 0.452 |
| 10 | 0.390 | 0.559 |

### Metric-Defined Failure Decomposition

| k | Complete Evidence + EM Pass | Complete Evidence + EM Fail | Incomplete Evidence + EM Pass | Incomplete Evidence + EM Fail |
|---:|---:|---:|---:|---:|
| 1 | 0% | 0% | 20% | 80% |
| 3 | 16% | 29% | 5% | 50% |
| 5 | 25% | 40% | 8% | 27% |
| 10 | 39% | 61% | 0% | 0% |

## Qualitative Refinement

Manual review of 20 representative examples showed that the automatic categories should not be treated as direct causal labels.

Among 10 reviewed Complete Evidence + EM Fail examples:

- 4 were refusals despite sufficient evidence;
- 2 were final-hop reasoning or answer-extraction failures;
- 2 were answer-type mismatches;
- 2 were Exact Match false negatives for semantically correct answers.

Among 10 reviewed Incomplete Evidence + EM Pass examples:

- 5 appeared answerable from partial evidence;
- 4 appeared answerable from partial evidence with possible parametric-knowledge assistance;
- 1 appeared to use an alternative evidence path.

## Final Interpretation

The results suggest that retrieval quality, evidence sufficiency, generation behavior, and evaluation design are separate components of RAG reliability.

Increasing k improved annotated evidence coverage and eventually improved answer quality, but simply providing retrieved context did not guarantee improvement at low k.

Complete annotated evidence was also not sufficient to guarantee correct generation.

At the same time, the qualitative review showed that strict Exact Match can mark semantically correct answers as failures, while the complete-evidence metric can mark useful retrievals as failures when only part of the annotated evidence is required.

Therefore, trustworthy RAG evaluation should distinguish between:

1. retrieval coverage;
2. actual evidence sufficiency;
3. generation/reasoning quality;
4. semantic answer correctness;
5. evaluation-metric limitations.

## Status

Experiment 01 is complete.

The next study can build on this framework by comparing retrieval methods or improving the evaluation methodology.
