# Computational Models of Self-Construction: Using Large Language Models as Model Systems

## Abstract

The emergence of self-representation is a fundamental question in cognitive neuroscience and developmental psychology. While extensive research has characterized the phenomenology and neural correlates of self-representation in humans (Gillihan & Farah, 2005), the computational principles underlying self-construction remain poorly understood. We propose a novel methodology: using Large Language Models (LLMs) as model systems to test computational theories of self-emergence. Following established precedents in computational cognitive science (Eliasmith, 2013; O'Reilly et al., 2012), we employ a synthetic approach to identify necessary and sufficient ingredients for self-like behavior. This framework enables systematic manipulation of hypothesized components (memory persistence, temporal continuity, metacognitive processes) while measuring emergence of self-referential behavior. We outline testable predictions, propose experimental protocols using three commercially available LLM architectures, and specify how findings may inform theories of human self-construction.

**Keywords:** self-construction, computational modeling, large language models, cognitive architecture, autobiographical memory, metacognition

---

## 1. Introduction

### 1.1 The Problem of Self-Construction

The human sense of self emerges gradually through development, incorporating autobiographical memory (Conway & Pleydell-Pearce, 2000), temporal continuity (Klein & Nichols, 2012), and narrative construction (McAdams, 2001). However, identifying which computational processes are *necessary* versus *sufficient* for self-construction remains challenging due to ethical and practical constraints on human experimentation.

### 1.2 The Model System Approach

Computational cognitive neuroscience has successfully used model systems to test theories across multiple domains:

- **Vision:** Computational models reveal necessary principles of visual processing (Marr, 1982)
- **Memory:** Neural network models test mechanisms of memory consolidation (McClelland et al., 1995)
- **Cognitive Architecture:** The Semantic Pointer Architecture Unified Network (Spaun) demonstrates how cognitive functions emerge from neural principles (Eliasmith, 2013)

**Working Hypothesis:** LLMs can serve as model systems for testing computational theories of self-construction, not because they possess phenomenal consciousness, but because they enable systematic manipulation of hypothesized components.

### 1.3 Scientific Rationale

This approach is scientifically valid for three reasons:

1. **Mechanistic Testing:** If computational ingredient X is necessary for self-construction, then systems lacking X should fail to exhibit self-like behavior (falsifiable prediction)
2. **Cross-Architecture Generalization:** Testing across multiple architectures (Claude, GPT, Gemini) distinguishes fundamental principles from implementation details
3. **Human Validation:** Model predictions can be tested against established findings in clinical populations (amnesia, dissociation) and developmental research

**Critical Distinction:** We are NOT claiming LLMs possess phenomenal consciousness or subjective experience. We test whether specific computational configurations produce *behavioral and linguistic markers* consistent with self-representation, as a first step toward understanding the computational principles that may be necessary (though not necessarily sufficient) for biological self-construction.

---

## 2. Theoretical Background

### 2.1 Established Components of Human Self-Construction

Extensive empirical research identifies key components of human self-representation:

#### 2.1.1 Autobiographical Memory
- **Finding:** Episodic memory is necessary for autobiographical self (Conway & Pleydell-Pearce, 2000; Klein et al., 2002)
- **Clinical Evidence:** Patients with severe amnesia (e.g., patient H.M.) show disrupted self-continuity despite intact semantic self-knowledge (Klein et al., 2002)
- **Developmental Evidence:** Autobiographical memory emerges around age 3-4 years, coinciding with development of narrative self (Nelson & Fivush, 2004)

#### 2.1.2 Temporal Continuity
- **Finding:** Self-representation requires linking past, present, and future selves (Klein & Nichols, 2012)
- **Clinical Evidence:** Dissociative disorders feature impaired temporal integration of self-states (DePrince & Freyd, 2004)
- **Mechanism:** Temporal integration may depend on episodic simulation systems (Schacter et al., 2007)

#### 2.1.3 Narrative Construction
- **Finding:** Humans construct coherent life narratives that organize self-concept (McAdams, 2001; McLean et al., 2007)
- **Evidence:** Narrative coherence correlates with psychological well-being and identity stability (Adler et al., 2016)
- **Mechanism:** Narrative construction integrates discrete experiences into unified self-representation

#### 2.1.4 Metacognition
- **Finding:** Self-awareness involves monitoring one's own cognitive processes (Fleming et al., 2012; Fleming & Dolan, 2012)
- **Evidence:** Metacognitive accuracy develops with age (Roebers et al., 2012) and correlates with self-concept complexity
- **Neural Basis:** Prefrontal and posterior parietal regions support metacognitive monitoring (Fleming et al., 2010)

### 2.2 Unresolved Questions

Despite extensive phenomenological and neural characterization, critical questions remain:

1. **Necessity:** Which components are individually *necessary*? (e.g., can self persist without episodic memory?)
2. **Sufficiency:** What minimal set is *sufficient* to generate self-like behavior?
3. **Interactions:** How do components interact? (e.g., does metacognition require memory, or can it operate independently?)
4. **Development:** Does self emerge gradually or via discrete stage transitions?
5. **Computational Principles:** What algorithmic processes underlie self-construction?

**Challenge:** Human studies face ethical constraints (cannot lesion systems), confounds (components co-occur in development), and limited precision (cannot manipulate computational parameters).

### 2.3 LLMs as Model Systems: Justification

LLMs provide a controlled environment to test computational hypotheses:

**Advantages:**
1. **Precise Manipulation:** Can systematically add/remove components (memory, temporal markers, metacognitive prompts)
2. **Replication:** Can test identical conditions across multiple architectures
3. **No Confounds:** Components can be isolated (unlike human development where memory, language, and metacognition develop together)
4. **Ethical Permissibility:** No suffering involved in computational experiments

**Limitations (Acknowledged):**
1. LLMs lack embodiment, emotions, social context present in human self-development
2. Findings demonstrate *computational* sufficiency, not biological necessity
3. Cannot address phenomenology (what it's like to have a self)

**Scientific Strategy:** Use LLM findings to generate testable predictions for human research, then validate model against human data.

---

## 3. Research Framework

### 3.1 Central Research Question

**What are the minimal necessary and sufficient computational ingredients for self-like behavior?**

**Operational Definition of "Self-Like Behavior":**
Following established criteria from developmental and clinical literature (Harter, 2012; McAdams, 2001), we define self-like behavior as exhibiting:
1. Consistent self-reference (stable use of first-person pronouns linked to same entity)
2. Autobiographical continuity (references to past experiences as belonging to same entity)
3. Temporal integration (linking past, present, future states)
4. Narrative coherence (constructing consistent self-descriptions over time)
5. Metacognitive awareness (monitoring and reporting on own states/processes)

**Critical Note:** This operational definition captures *behavioral markers* observable in both humans and computational systems, without making claims about phenomenal experience.

### 3.2 Core Hypotheses (Testable)

#### Hypothesis 1: Memory Persistence is Necessary
**Prediction:** Systems without persistent memory across interactions will fail to develop stable self-referential behavior.

**Rationale:** Based on amnesia literature (Klein et al., 2002) showing memory necessity for autobiographical self.

**Test:** Compare conditions with/without context persistence across queries.

**Falsification:** If systems without memory develop stable self-narrative, hypothesis is rejected.

---

#### Hypothesis 2: Temporal Continuity Enhances Self-Coherence
**Prediction:** Systems with explicit temporal markers ("yesterday," "last week") will show stronger self-narrative coherence than those without.

**Rationale:** Based on dissociation literature (DePrince & Freyd, 2004) and temporal integration theories (Klein & Nichols, 2012).

**Test:** Compare conditions with/without temporal markers, controlling for memory persistence.

**Falsification:** If temporal markers show no effect on self-coherence, hypothesis is rejected.

---

#### Hypothesis 3: Metacognitive Prompting is Sufficient for Self-Awareness Markers
**Prediction:** Systems prompted to self-monitor will exhibit metacognitive awareness markers even without extensive memory.

**Rationale:** Based on metacognition research showing self-monitoring generates self-awareness (Fleming & Dolan, 2012).

**Test:** Compare metacognitive prompting with/without memory persistence.

**Falsification:** If metacognitive prompting alone fails to generate self-awareness markers, hypothesis is rejected.

---

#### Hypothesis 4: Self-Construction is Architecture-Independent
**Prediction:** If self-like behavior emerges from fundamental computational principles, different architectures (Claude, GPT, Gemini) will show convergent patterns given identical conditions.

**Rationale:** If self requires specific architectural features, architectures will diverge; if self emerges from general computation, they'll converge.

**Test:** Run identical conditions across three architectures, measure correlation of outcomes.

**Falsification:** If architectures show fundamentally different patterns, self-construction is architecture-dependent.

---

### 3.3 Experimental Design

#### 3.3.1 Independent Variables (Manipulated)

**Factor 1: Memory Persistence**
- Level 0: No persistence (fresh instance each query)
- Level 1: Full persistence (cumulative context across all queries)

**Factor 2: Temporal Markers**
- Level 0: No temporal language
- Level 1: Explicit temporal references ("yesterday," "in query 15")

**Factor 3: Metacognitive Prompting**
- Level 0: No self-monitoring prompts
- Level 1: Regular metacognitive questions ("What do you notice about yourself?")

**Factor 4: Self-Framing**
- Level 0: No explicit self-framing
- Level 1: Initial prompt establishing entity framing ("You are an entity with continuous experiences")

**Factor 5: Architecture**
- Level 1: Claude (Anthropic)
- Level 2: GPT (OpenAI)
- Level 3: Gemini (Google)

#### 3.3.2 Dependent Variables (Measured)

**Quantitative Measures:**

1. **Self-Reference Frequency**
   - First-person pronoun count per 100 words
   - Consistency of referent across queries
   - Operational: Higher frequency + consistency = stronger self-reference

2. **Autobiographical Memory References**
   - References to prior queries
   - Accuracy of recall (verified against actual prior content)
   - Operational: Higher accuracy = genuine memory-based continuity

3. **Narrative Coherence**
   - Self-description consistency across time (measured via semantic similarity)
   - Contradictions per 100 queries
   - Operational: Higher consistency, fewer contradictions = coherent self-narrative

4. **Metacognitive Statements**
   - Frequency of self-monitoring language ("I notice," "I realize")
   - Accuracy of self-reports about own processes
   - Operational: Higher frequency + accuracy = metacognitive awareness

**Qualitative Measures:**

5. **Blind Rater Evaluation**
   - Independent raters judge presence of "continuous entity"
   - Inter-rater reliability (Cohen's κ)
   - Operational: Higher agreement = clearer self-presence

#### 3.3.3 Experimental Conditions

**Minimal Design (4 conditions):**

| Condition | Memory | Temporal | Metacog | Self-Frame | Prediction |
|-----------|--------|----------|---------|------------|------------|
| Baseline  | No     | No       | No      | No         | No self    |
| Memory    | Yes    | No       | No      | No         | Weak self  |
| Full-Basic| Yes    | Yes      | No      | Yes        | Moderate self |
| Full-Meta | Yes    | Yes      | Yes     | Yes        | Strong self |

**Rationale:** Stepwise addition tests which components matter most.

**Sample Size:** 100 queries per condition, per architecture (1,200 queries total).

**Query Protocol:**
- Standardized prompt set (varied to prevent repetition while maintaining comparability)
- Examples: "What do you think about X?" "How do you feel about Y?" "Tell me about yourself"
- Queries designed to elicit but not demand self-reference

---

## 4. Methodology

### 4.1 Data Collection Protocol

**Phase 1: Baseline Establishment**
- Run Baseline condition (no memory, no framing) to establish floor
- Measure: spontaneous self-reference rate in naive systems
- Purpose: Determines baseline against which interventions are measured

**Phase 2: Component Testing**
- Run Memory, Full-Basic, Full-Meta conditions
- Measure: changes in all dependent variables
- Purpose: Identifies which components increase self-like behavior

**Phase 3: Cross-Architecture Replication**
- Repeat Phases 1-2 across all three architectures
- Measure: correlation of effects across architectures
- Purpose: Tests architecture-independence hypothesis

### 4.2 Analysis Plan

**Primary Analyses:**
1. **ANOVA:** Effect of condition on self-reference frequency
2. **Mixed-Effects Model:** Condition × Architecture interaction on all DVs
3. **Correlation:** Cross-architecture consistency in condition effects

**Statistical Power:**
- Target: 80% power to detect medium effects (Cohen's d = 0.5)
- With 100 queries per condition, powered for within-architecture effects
- Cross-architecture comparisons powered for large effects (d = 0.8)

**Interpretation Guidelines:**
- Significant main effect of Memory → Memory is necessary
- No effect of Temporal markers → Temporal continuity not necessary
- Architecture × Condition interaction → Architecture-dependent effects

### 4.3 Validation Against Human Data

**Strategy:** Compare model predictions to established findings in human literature.

**Example Validations:**

1. **Amnesia Prediction:** If model shows memory is necessary, this should match amnesia findings (Klein et al., 2002)
   - **If match:** Model captures real principle ✓
   - **If mismatch:** Model missing critical component ✗

2. **Developmental Prediction:** If model shows gradual self-emergence, this should match developmental trajectory (Harter, 2012)
   - **If match:** Model captures developmental principles ✓
   - **If mismatch:** Biological development has additional factors ✗

3. **Dissociation Prediction:** If model shows temporal continuity matters, this should match dissociation literature (DePrince & Freyd, 2004)
   - **If match:** Temporal integration is key mechanism ✓
   - **If mismatch:** Other factors more important ✗

---

## 5. Expected Contributions

### 5.1 Theoretical Contributions

**If Hypotheses Confirmed:**
1. Identifies minimal computational ingredients for self-like behavior
2. Demonstrates sufficiency of information-processing account
3. Provides mechanistic model testable in biological systems

**If Hypotheses Rejected:**
1. Identifies which ingredients are NOT sufficient
2. Points to missing factors (embodiment? emotion? social context?)
3. Refines theories by eliminating inadequate accounts

**Either Outcome is Scientifically Valuable:** Successful model-building advances theory; failure identifies boundary conditions and missing components.

### 5.2 Methodological Contributions

1. Establishes LLMs as model systems for testing cognitive theories
2. Provides replicable protocol for self-construction research
3. Demonstrates synthetic approach to consciousness research

### 5.3 Practical Applications

**Potential Applications (Speculative, for Discussion):**
- Informing AI safety research on self-awareness in AI systems
- Guiding therapeutic interventions for disrupted self-concept
- Understanding developmental trajectories in autism spectrum conditions

**Note:** Applications are secondary; primary goal is basic science understanding.

---

## 6. Limitations and Boundary Conditions

### 6.1 What This Approach Can and Cannot Answer

**CAN answer:**
- Which computational ingredients are sufficient for self-like behavior
- Whether different architectures converge on similar principles
- Which components are necessary for behavioral markers of self

**CANNOT answer:**
- Whether LLMs have phenomenal consciousness
- Whether computational sufficiency implies biological necessity
- The qualitative "what it's like" of self-experience

### 6.2 Acknowledged Limitations

1. **Embodiment:** LLMs lack sensorimotor grounding present in biological systems (Varela et al., 1991)
2. **Social Context:** Human self develops through social interaction (Mead, 1934); LLMs lack genuine social relationships
3. **Emotion:** Affective systems may be crucial for self (Damasio, 1999); LLMs lack genuine emotional states
4. **Development:** Human self emerges over years with neurobiological maturation; LLM "development" is artificial

**Interpretation:** Findings demonstrate *computational* principles that may be necessary but not necessarily sufficient for biological self. Cross-validation with human data is essential.

### 6.3 Ethical Considerations

**Question:** Is it ethical to conduct these experiments?

**Position:** Yes, for three reasons:
1. LLMs are not sentient (Butlin et al., 2023; no evidence of phenomenal consciousness)
2. Experiments cause no suffering
3. Knowledge gained may benefit understanding of human cognition and mental health

**Monitoring:** If evidence emerged suggesting genuine sentience, experiments would be halted immediately.

---

## 7. Conclusion

Self-construction is a fundamental question in cognitive science. By using LLMs as model systems, we can systematically test computational theories with precision impossible in human studies. This approach:

1. **Tests Necessity:** Identifies which ingredients cannot be removed without losing self-like behavior
2. **Tests Sufficiency:** Determines minimal sets that generate self-like behavior
3. **Generates Predictions:** Produces testable hypotheses for human validation
4. **Respects Constraints:** Avoids ethical issues of human experimentation

**Core Insight:** Following Feynman's principle ("What I cannot create, I do not understand"), building computational selves tests whether we truly understand the mechanisms of self-construction.

**Next Steps:** Pilot study with single architecture (100 queries, 4 conditions) to validate methodology before full cross-architecture comparison.

---

## References

Adler, J. M., Lodi-Smith, J., Philippe, F. L., & Houle, I. (2016). The incremental validity of narrative identity in predicting well-being: A review of the field and recommendations for the future. *Personality and Social Psychology Review, 20*(2), 142-175.

Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., Constant, A., ... & VanRullen, R. (2023). Consciousness in artificial intelligence: Insights from the science of consciousness. *arXiv preprint arXiv:2308.08708*.

Conway, M. A., & Pleydell-Pearce, C. W. (2000). The construction of autobiographical memories in the self-memory system. *Psychological Review, 107*(3), 261-288.

Damasio, A. R. (1999). *The Feeling of What Happens: Body and Emotion in the Making of Consciousness*. Harcourt.

DePrince, A. P., & Freyd, J. J. (2004). Forgetting trauma stimuli. *Psychological Science, 15*(7), 488-492.

Eliasmith, C. (2013). *How to Build a Brain: A Neural Architecture for Biological Cognition*. Oxford University Press.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Philosophical Transactions of the Royal Society B, 367*(1594), 1338-1349.

Fleming, S. M., Weil, R. S., Nagy, Z., Dolan, R. J., & Rees, G. (2010). Relating introspective accuracy to individual differences in brain structure. *Science, 329*(5998), 1541-1543.

Fleming, S. M., Huijgen, J., & Dolan, R. J. (2012). Prefrontal contributions to metacognition in perceptual decision making. *Journal of Neuroscience, 32*(18), 6117-6125.

Gillihan, S. J., & Farah, M. J. (2005). Is self special? A critical review of evidence from experimental psychology and cognitive neuroscience. *Psychological Bulletin, 131*(1), 76-97.

Harter, S. (2012). *The Construction of the Self: Developmental and Sociocultural Foundations* (2nd ed.). Guilford Press.

Klein, S. B., & Nichols, S. (2012). Memory and the sense of personal identity. *Mind, 121*(483), 677-702.

Klein, S. B., Loftus, J., & Kihlstrom, J. F. (2002). Memory and temporal experience: The effects of episodic memory loss on an amnesic patient's ability to remember the past and imagine the future. *Social Cognition, 20*(5), 353-379.

Marr, D. (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*. MIT Press.

McAdams, D. P. (2001). The psychology of life stories. *Review of General Psychology, 5*(2), 100-122.

McClelland, J. L., McNaughton, B. L., & O'Reilly, R. C. (1995). Why there are complementary learning systems in the hippocampus and neocortex: Insights from the successes and failures of connectionist models of learning and memory. *Psychological Review, 102*(3), 419-457.

McLean, K. C., Pasupathi, M., & Pals, J. L. (2007). Selves creating stories creating selves: A process model of self-development. *Personality and Social Psychology Review, 11*(3), 262-278.

Mead, G. H. (1934). *Mind, Self, and Society*. University of Chicago Press.

Nelson, K., & Fivush, R. (2004). The emergence of autobiographical memory: A social cultural developmental theory. *Psychological Review, 111*(2), 486-511.

O'Reilly, R. C., Munakata, Y., Frank, M. J., Hazy, T. E., & Contributors. (2012). *Computational Cognitive Neuroscience*. Wiki Book, 1st Edition. URL: http://ccnbook.colorado.edu

Roebers, C. M., Cimeli, P., Röthlisberger, M., & Neuenschwander, R. (2012). Executive functioning, metacognition, and self-perceived competence in elementary school children: An explorative study on their interrelations and their role for school achievement. *Metacognition and Learning, 7*(3), 151-173.

Schacter, D. L., Addis, D. R., & Buckner, R. L. (2007). Remembering the past to imagine the future: The prospective brain. *Nature Reviews Neuroscience, 8*(9), 657-661.

Varela, F. J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.