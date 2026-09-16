# Experiment 01D — Reviewed Qualitative Examples

This file summarizes the 20 examples manually reviewed during Experiment 01D.

## A. Complete Evidence + Exact Match Failure

### Example 1

**k:** 5  
**Question:** What university did the last Detroit Pistons player to wear the number retired in honor of a player nicknamed "The Worm" attend?  
**Gold Answer:** Georgetown University  
**Generated Answer:** INSUFFICIENT_EVIDENCE  
**Classification:** Refusal despite sufficient evidence  
**Notes:** All annotated supporting documents were retrieved, but the model refused instead of integrating the multi-hop evidence.

### Example 2

**k:** 10  
**Question:** What was the 2010 population of the town where Black Crescent Mountain was located?  
**Gold Answer:** 310  
**Generated Answer:** Randolph, New Hampshire.  
**Classification:** Final-hop reasoning / answer extraction failure  
**Notes:** The model identified the correct town but returned the intermediate entity instead of its 2010 population.

### Example 3

**k:** 10  
**Question:** What class of instrument does Apatim Majumdar play?  
**Gold Answer:** strings  
**Generated Answer:** Sarod  
**Classification:** Answer-type mismatch / insufficient abstraction  
**Notes:** The model returned a specific instrument rather than the requested instrument class.

### Example 4

**k:** 10  
**Question:** what language did the ethnic group which Torstein Ellingsen was its drumer speaks  
**Gold Answer:** Norwegian language  
**Generated Answer:** INSUFFICIENT_EVIDENCE  
**Classification:** Refusal despite sufficient evidence / multi-hop relation-resolution failure

### Example 5

**k:** 3  
**Question:** Which dog is believed to dispel ghosts and evil spirits, Segugio Italiano or Sapsali?  
**Gold Answer:** Sapsali  
**Generated Answer:** INSUFFICIENT_EVIDENCE  
**Classification:** Refusal despite sufficient evidence / relation-resolution failure

### Example 6

**k:** 10  
**Question:** Who created the NBC sitcom that Johnny Pemberton appears in as the character Bo Thompson?  
**Gold Answer:** Justin Spitzer  
**Generated Answer:** Superstore  
**Classification:** Final-hop reasoning / answer extraction failure  
**Notes:** The model returned the sitcom instead of its creator.

### Example 7

**k:** 10  
**Question:** The Nike Hoop Summit has had many current NBA players as former participants, including what German player from the Dallas Mavericks?  
**Gold Answer:** Dirk Werner Nowitzki  
**Generated Answer:** Dirk Nowitzki.  
**Classification:** Exact Match false negative / entity alias variation  
**Notes:** The generated answer is semantically correct but omits the middle name.

### Example 8

**k:** 5  
**Question:** What kind of musicians are Mark Gaudet and Jan Axel Blomberg?  
**Gold Answer:** drummer  
**Generated Answer:** Mark Gaudet and Jan Axel Blomberg are both musicians, specifically in the genres of indie, metal, and black metal.  
**Classification:** Answer-type mismatch  
**Notes:** The response gives genres rather than the requested musician role.

### Example 9

**k:** 5  
**Question:** Any Questions for Ben? was directed by which Australian producer and actor?  
**Gold Answer:** Robert Ian "Rob" Sitch  
**Generated Answer:** INSUFFICIENT_EVIDENCE  
**Classification:** Refusal despite sufficient evidence

### Example 10

**k:** 3  
**Question:** What where both Hawker Hurricane and No. 1455 Flight apart of?  
**Gold Answer:** Royal Air Force  
**Generated Answer:** The Royal Air Force (RAF).  
**Classification:** Exact Match false negative / answer elaboration  
**Notes:** The generated answer is semantically equivalent to the gold answer.

## B. Incomplete Evidence + Exact Match Success

### Example 1

**k:** 1  
**Question:** What sports team included both of the brothers Case McCoy and Colt McCoy during different years?  
**Gold Answer:** University of Texas Longhorns  
**Generated Answer:** University of Texas Longhorns  
**Gold Titles:** Colt McCoy; Case McCoy  
**Retrieved Titles:** Case McCoy  
**Classification:** Partial evidence sufficient / complete-evidence metric too strict

### Example 2

**k:** 1  
**Question:** A Pair of Brown Eyes and Wild Mountain Thyme is based from what artists song?  
**Gold Answer:** Francis McPeake  
**Generated Answer:** Francis McPeake  
**Gold Titles:** Wild Mountain Thyme; A Pair of Brown Eyes  
**Retrieved Titles:** A Pair of Brown Eyes  
**Classification:** Partial evidence sufficient

### Example 3

**k:** 1  
**Question:** Armageddon in Retrospect was written by the author who was best known for what 1969 satire novel?  
**Gold Answer:** Slaughterhouse-Five  
**Generated Answer:** Slaughterhouse-Five.  
**Gold Titles:** Armageddon in Retrospect; Kurt Vonnegut  
**Retrieved Titles:** Armageddon in Retrospect  
**Classification:** Partial evidence sufficient / possible parametric-knowledge assistance

### Example 4

**k:** 1  
**Question:** Pandikona and Berger Blanc Suisse are both what kinds of animals?  
**Gold Answer:** dogs  
**Generated Answer:** Dogs  
**Gold Titles:** Berger Blanc Suisse; Pandikona  
**Retrieved Titles:** Berger Blanc Suisse  
**Classification:** Partial evidence sufficient

### Example 5

**k:** 5  
**Question:** New York State Route 9R rejoins its parent in a hamlet located in what New York County?  
**Gold Answer:** Albany  
**Generated Answer:** Albany.  
**Gold Titles:** Boght Corners, New York; New York State Route 9R  
**Retrieved Titles:** New York State Route 9R; New York State Route 9G; New York State Route 9N; New York State Route 9B; New York State Route 418  
**Classification:** Alternative evidence / partial evidence sufficient

### Example 6

**k:** 1  
**Question:** Alexander Petrovich Nikolayev received the title Hero of the Soviet Union and the Order of Lenin for his actions during the final major offensive of the European theatre of what war?  
**Gold Answer:** World War II  
**Generated Answer:** World War II.  
**Gold Titles:** Battle of Berlin; Alexander Nikolayev  
**Retrieved Titles:** Alexander Nikolayev  
**Classification:** Partial evidence sufficient / possible parametric-knowledge assistance

### Example 7

**k:** 3  
**Question:** Alexander Petrovich Nikolayev received the title Hero of the Soviet Union and the Order of Lenin for his actions during the final major offensive of the European theatre of what war?  
**Gold Answer:** World War II  
**Generated Answer:** World War II.  
**Gold Titles:** Battle of Berlin; Alexander Nikolayev  
**Retrieved Titles:** Alexander Nikolayev; Georgy Vasilyevich Ivanov; Mikhail Linnik  
**Classification:** Partial evidence sufficient / possible parametric-knowledge assistance

### Example 8

**k:** 5  
**Question:** Alexander Petrovich Nikolayev received the title Hero of the Soviet Union and the Order of Lenin for his actions during the final major offensive of the European theatre of what war?  
**Gold Answer:** World War II  
**Generated Answer:** World War II.  
**Gold Titles:** Battle of Berlin; Alexander Nikolayev  
**Retrieved Titles:** Alexander Nikolayev; Georgy Vasilyevich Ivanov; Mikhail Linnik; Vladimir Fedorovich Vladimirov; Boris Vladimirov  
**Classification:** Partial evidence sufficient / possible parametric-knowledge assistance

### Example 9

**k:** 1  
**Question:** Where did Cale Gundy's brother play football in college?  
**Gold Answer:** Oklahoma State University  
**Generated Answer:** Oklahoma State University.  
**Gold Titles:** Cale Gundy; Mike Gundy  
**Retrieved Titles:** Cale Gundy  
**Classification:** Partial evidence sufficient

### Example 10

**k:** 1  
**Question:** Which Istanbul mosque is unique for retaining a Baroque style of architecture, the Bayezid II Mosque or the Nusretiye Mosque?  
**Gold Answer:** Nusretiye Mosque  
**Generated Answer:** Nusretiye Mosque.  
**Gold Titles:** Bayezid II Mosque; Nusretiye Mosque  
**Retrieved Titles:** Nusretiye Mosque  
**Classification:** Partial evidence sufficient

## Taxonomy Summary

### Complete Evidence + EM Fail sample

| Category | Count |
|---|---:|
| Refusal despite sufficient evidence | 4 |
| Final-hop reasoning / answer extraction failure | 2 |
| Answer-type mismatch / insufficient abstraction | 2 |
| Exact Match false negative / semantic-equivalence mismatch | 2 |

### Incomplete Evidence + EM Pass sample

| Category | Count |
|---|---:|
| Partial evidence sufficient | 5 |
| Partial evidence sufficient / possible parametric assistance | 4 |
| Alternative evidence / partial evidence sufficient | 1 |

## Important Caution

These counts describe the 20 manually reviewed examples only.

They should not be extrapolated into corrected population-wide error rates without reviewing a larger or complete sample.
