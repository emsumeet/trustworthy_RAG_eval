# Experiment 01D — Qualitative Failure Examples

Representative examples extracted from Experiment 01C.

Random seed: 42

## Retrieval Success + Generation Failure

Sample size reviewed: 10

---

### Example 1

**k:** 5

**Question:**

What university did the last Detroit Pistons player to wear the number retired in honor of a player nicknamed "The Worm" attend?

**Gold Answer:**

Georgetown University

**Generated Answer:**

INSUFFICIENT_EVIDENCE

**Exact Match:** 0

**Gold Supporting Documents:**

`['Dennis Rodman', 'Greg Monroe']`

**Manual Failure Classification:**

Refusal despite sufficient evidence

**Notes:**

The retriever successfully included all annotated gold supporting documents
(Dennis Rodman and Greg Monroe) at k=5, but the generator returned
`INSUFFICIENT_EVIDENCE`.

This is therefore not a retrieval failure under the current evaluation
definition. The failure occurred at the generation stage: the model failed
to connect the retrieved evidence required to identify Greg Monroe and his
university.

This example suggests a possible multi-hop reasoning or evidence-integration
failure rather than missing evidence.

---

### Example 2

**k:** 10

**Question:**

What was the 2010 population of the town where Black Crescent Mountain was located?

**Gold Answer:**

310

**Generated Answer:**

Randolph, New Hampshire.

**Exact Match:** 0

**Manual Failure Classification:**

Answer extraction / final-hop reasoning failure

**Notes:**

The model identified the correct town, `Randolph, New Hampshire`, but returned
the town name instead of the requested 2010 population.

The gold answer was `310`.

Because this example belongs to the Retrieval Success + Generation Failure
category at k=10, the complete annotated supporting evidence was available to
the generator.

The model appears to identify the relevant location correctly but fails to
complete the final reasoning step needed to extract the town's 2010 population.

---

### Example 3

**k:** 10

**Question:**

What class of instrument does Apatim Majumdar play?

**Gold Answer:**

strings

**Generated Answer:**

Sarod

**Exact Match:** 0

**Manual Failure Classification:**

Answer-type mismatch / insufficient abstraction

**Notes:**

The model returned `Sarod`, which is a specific instrument, while the question
asks for the broader class of instrument.

The gold answer is `strings`.

Because complete annotated supporting evidence was available, the error occurs
at the generation stage. The model appears to identify the relevant instrument
but fails to map it to the requested category.

---

### Example 4

**k:** 10

**Question:**

what language did the ethnic group which Torstein Ellingsen was its drumer speaks

**Gold Answer:**

Norwegian language

**Generated Answer:**

INSUFFICIENT_EVIDENCE

**Exact Match:** 0

**Manual Failure Classification:**

Refusal despite sufficient evidence / multi-hop relation resolution failure

**Notes:**

The model returned `INSUFFICIENT_EVIDENCE`, even though complete annotated
supporting evidence was available under the current evaluation setup.

The question requires multiple relation hops before arriving at the requested
language. The model appears to have failed to connect these intermediate
relations and therefore refused to answer.

---

### Example 5

**k:** 3

**Question:**

Which dog is believed to dispel ghosts and evil spirits, Segugio Italiano or Sapsali?

**Gold Answer:**

Sapsali

**Generated Answer:**

INSUFFICIENT_EVIDENCE

**Exact Match:** 0

**Manual Failure Classification:**

Refusal despite sufficient evidence / relation-resolution failure

**Notes:**

The model returned `INSUFFICIENT_EVIDENCE` despite the example being classified
as Retrieval Success + Generation Failure.

The question requires comparing two dog breeds and identifying which one is
associated with dispelling ghosts and evil spirits.

The failure appears to be at the generation or relation-resolution stage rather
than the retrieval stage.

---

### Example 6

**k:** 10

**Question:**

Who created the NBC sitcom that Johnny Pemberton appears in as the character Bo Thompson?

**Gold Answer:**

Justin Spitzer

**Generated Answer:**

Superstore

**Exact Match:** 0

**Manual Failure Classification:**

Final-hop reasoning / answer extraction failure

**Notes:**

The model returned `Superstore`, which is the NBC sitcom referenced in the
question, instead of answering who created the sitcom.

The correct answer is `Justin Spitzer`.

The model therefore identified an intermediate entity correctly but failed to
perform the final relation needed to return the requested person.

---

### Example 7

**k:** 10

**Question:**

The Nike Hoop Summit has had many current NBA players as former participants, including what German player from the Dallas Mavericks?

**Gold Answer:**

Dirk Werner Nowitzki

**Generated Answer:**

Dirk Nowitzki.

**Exact Match:** 0

**Manual Failure Classification:**

Exact Match evaluation false negative / entity alias variation

**Notes:**

The generated answer `Dirk Nowitzki` refers to the same person as the gold
answer `Dirk Werner Nowitzki`.

The prediction is semantically correct, but Exact Match assigns a score of 0
because the generated answer omits the middle name.

This is primarily an evaluation-metric limitation rather than a true generation
failure.

---

### Example 8

**k:** 5

**Question:**

What kind of musicians are Mark Gaudet and Jan Axel Blomberg?

**Gold Answer:**

drummer

**Generated Answer:**

Mark Gaudet and Jan Axel Blomberg are both musicians, specifically in the genres of indie, metal, and black metal.

**Exact Match:** 0

**Manual Failure Classification:**

Answer-type mismatch

**Notes:**

The question asks what kind of musicians Mark Gaudet and Jan Axel Blomberg are.

The gold answer is `drummer`.

The generated response instead describes musical genres and does not provide
the requested musician role.

The model appears to recognize relevant entities but answers at the wrong
semantic level.

---

### Example 9

**k:** 5

**Question:**

Any Questions for Ben? was directed by which Australian producer and actor?

**Gold Answer:**

Robert Ian "Rob" Sitch

**Generated Answer:**

INSUFFICIENT_EVIDENCE

**Exact Match:** 0

**Manual Failure Classification:**

Refusal despite sufficient evidence

**Notes:**

The model returned `INSUFFICIENT_EVIDENCE` instead of identifying Robert Ian
"Rob" Sitch.

Because the example was categorized as Retrieval Success + Generation Failure,
the annotated supporting evidence was available.

This is therefore a generation-stage refusal under the current retrieval
definition.

---

### Example 10

**k:** 3

**Question:**

What where both Hawker Hurricane and No. 1455 Flight apart of?

**Gold Answer:**

Royal Air Force

**Generated Answer:**

The Royal Air Force (RAF).

**Exact Match:** 0

**Manual Failure Classification:**

Exact Match evaluation false negative / answer elaboration

**Notes:**

The generated answer `The Royal Air Force (RAF)` is semantically equivalent to
the gold answer `Royal Air Force`.

Exact Match assigns a score of 0 because the generated answer contains an
article and the additional abbreviation `RAF`.

This should be treated as a metric failure rather than a true generation
failure.

---

## Emerging Failure Taxonomy

The reviewed examples suggest the following failure types:

1. **Refusal despite sufficient evidence**
2. **Final-hop reasoning / answer extraction failure**
3. **Answer-type mismatch / insufficient abstraction**
4. **Multi-hop relation-resolution failure**
5. **Exact Match false negative / semantic-equivalence mismatch**

## Research Implication

Experiment 01C initially classified all Exact Match failures with complete
evidence as generation failures.

The qualitative review shows that this interpretation is too coarse.

Some cases are genuine generation failures, while others are evaluation
failures caused by strict Exact Match scoring.

This motivates a later evaluation stage using semantic answer equivalence,
manual validation, and evidence-grounded faithfulness measures.
