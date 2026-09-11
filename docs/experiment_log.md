# Experiment Log

## Experiment 01A — Dense Retrieval Baseline

### Date

September 2026

### Objective

Measure how retrieval depth affects supporting-document recall and
complete evidence retrieval in the HotpotQA distractor setting.

### Dataset

HotpotQA distractor validation split.

Sample size: 100 questions  
Random seed: 42

### Retriever

Embedding model:

`sentence-transformers/all-MiniLM-L6-v2`

Document representations and question representations were L2-normalized
and ranked using cosine similarity.

### Results

| k | Supporting Document Recall@K | Complete Evidence Rate@K |
|---|---:|---:|
| 1 | 0.430 | 0.000 |
| 3 | 0.715 | 0.450 |
| 5 | 0.825 | 0.650 |
| 10 | 1.000 | 1.000 |

### Initial Observation

Increasing retrieval depth substantially increased supporting-document
recall and the probability of retrieving the complete set of gold
supporting documents.

At k=1, supporting-document recall was 0.430 and no evaluated question
contained complete supporting evidence.

Increasing retrieval depth to k=3 raised supporting-document recall to
0.715 and complete evidence retrieval to 0.450.

At k=5, these values increased to 0.825 and 0.650 respectively.

At k=10, both metrics reached 1.000.

### Important Limitation

The k=10 result should not be interpreted as evidence that k=10 is the
optimal RAG configuration.

The experiment uses the HotpotQA distractor setting, where each question
is supplied with a limited candidate context containing the gold
supporting documents together with distractor documents.

Retrieving all candidate documents therefore makes complete evidence
retrieval expected.

The next stage will test whether the increased evidence coverage improves
answer generation or whether the additional distractor context introduces
retrieval noise that negatively affects answer quality.

### Next Experiment

Experiment 01B will compare answer-generation performance under:

- No retrieval
- k=1
- k=3
- k=5
- k=10

The experiment will investigate the relationship between evidence
coverage and generated-answer quality.
