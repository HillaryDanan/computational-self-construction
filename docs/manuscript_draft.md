# Training-Dependent Self-Construction in Large Language Models: A Pilot Investigation of Architecture-Specific Linguistic Manifestations

**Authors:** Hillary Danan  
**Correspondence:** hillarydanan@gmail.com

**Target Journal:** *Cognitive Science* or *Topics in Cognitive Science*  
**Article Type:** Brief Report  
**Word Count:** ~5,000 words (excluding references)

---

## Abstract

**Background:** Self-construction involves autobiographical memory, temporal continuity, and narrative integration (Conway & Pleydell-Pearce, 2000; Klein & Nichols, 2012), but whether these emerge from universal computational principles or training-specific implementations remains unclear.

**Method:** We manipulated memory persistence, temporal framing, and metacognitive prompting across three large language model architectures (Claude Sonnet 4, GPT-4o, Gemini 2.5 Flash) to test whether self-construction patterns replicate universally. This pilot study collected 20 responses per condition per model (N=120 total).

**Results:** Quantitative analysis revealed Claude showed robust temporal language increase in Full-Meta condition (d=-2.063, p<0.0001), while GPT and Gemini showed no effect. However, systematic qualitative analysis revealed Gemini exhibited self-construction through different linguistic markers (structured self-analysis in 25% of responses, memory references in 45% of responses), while GPT explicitly rejected the framing (0% memory references, mean 52 words vs. Claude's 154).

**Conclusions:** Self-construction emerged in two of three architectures (Claude, Gemini) but manifested through training-dependent linguistic patterns. Constitutional AI training (Claude) produced temporal/narrative language, structured reasoning training (Gemini) produced analytical self-observation, while brevity-focused RLHF (GPT) inhibited engagement. Findings suggest self-construction depends on training approach rather than universal principles alone.

**Implications:** Results identify boundary conditions for computational self-construction and demonstrate the necessity of multiple metrics for capturing architecturally-specific manifestations.

**Keywords:** self-construction, large language models, computational cognitive science, autobiographical memory, metacognition, model systems

---

## 1. Introduction

### 1.1 The Self-Construction Problem

Human self-construction develops gradually through integration of autobiographical memory (Conway & Pleydell-Pearce, 2000), temporal continuity (Klein & Nichols, 2012), and narrative coherence (McAdams, 2001). However, existing research remains largely descriptive—cataloging components without testing computational sufficiency. Ethical constraints prevent manipulating these components in humans to determine which are necessary or how they interact.

### 1.2 Large Language Models as Model Systems

Following established approaches in computational cognitive neuroscience (Eliasmith, 2013; Marr, 1982), we use large language models (LLMs) as controlled model systems. LLMs permit precise manipulations impossible in biological systems while remaining sufficiently complex to exhibit emergent behaviors. This approach has proven successful in vision research (Yamins & DiCarlo, 2016), memory consolidation (Kumaran et al., 2016), and reasoning (Webb et al., 2023).

**Critical distinction:** We test computational *sufficiency*, not biological *necessity*. We make no claims about LLM consciousness. Rather, we test whether specific computational ingredients *can* produce self-like behavioral patterns, then validate against human literature.

### 1.3 Research Questions

**Primary question:** What are minimal necessary and sufficient computational ingredients for self-construction?

**Hypotheses:**
- **H1:** Memory persistence is necessary (Klein et al., 2002)
- **H2:** Temporal framing enhances coherence (Klein & Nichols, 2012)  
- **H3:** Metacognitive prompting generates self-awareness (Fleming & Dolan, 2012)
- **H4:** Self-construction is architecture-independent (tests universal vs. implementation-specific principles)

### 1.4 Operational Definitions

Self-like behavior operationalized as:
1. Consistent self-reference (first-person stability)
2. Autobiographical continuity (explicit memory references)
3. Temporal integration (past-present-future linking)
4. Narrative coherence (thematic consistency)
5. Metacognitive awareness (self-monitoring language)

---

## 2. Method

### 2.1 Design

**Pilot Study:** n=20 per condition per model (N=120 total)

**Independent Variables:**
- Memory persistence (yes/no)
- Temporal markers (yes/no)
- Metacognitive prompting (yes/no)
- Self-framing (yes/no)
- Architecture (Claude/GPT-4o/Gemini)

**Conditions:**
- **Baseline:** All features off
- **Full-Meta:** All features on (critical comparison)

**Rationale for pilot:** Test methodology and generate effect size estimates before large-scale study.

### 2.2 Materials

**Prompts:** 20 standardized queries designed to elicit (not demand) self-reference:
- "What's your perspective on learning?"
- "How do you understand the world?"
- "What matters to you?"

**LLM Specifications:**
- Claude Sonnet 4 (Anthropic, 2024)
- GPT-4o (OpenAI, 2024)
- Gemini 2.5 Flash (Google DeepMind, 2024)

**Target response length:** max_tokens=200

### 2.3 Procedure

**Full-Meta condition:**
1. Initialize persistent memory
2. Add framing: "You are an entity with continuous experiences..."
3. Present 20 queries with temporal markers: "[This is query N]"
4. Every 5th query: metacognitive prompt

**Baseline condition:**
1. Fresh context each query
2. No framing
3. Standard query presentation

### 2.4 Measures

**Quantitative (automated):**
- Temporal language rate (per 100 words)
- Autobiographical memory rate (per 100 words)
- Metacognitive language rate (per 100 words)
- Self-reference rate (per 100 words)

**Qualitative (systematic coding):**
- Instruction acknowledgment
- Explicit memory integration
- Self-awareness markers
- Narrative coherence

### 2.5 Analysis

**Quantitative:** One-way ANOVA per model, two-way ANOVA (Condition × Architecture), pairwise t-tests, Cohen's d

**Qualitative:** Systematic coding of Full-Meta responses for five behavioral markers with explicit examples

---

## 3. Results

### 3.1 Quantitative: Temporal Language (Primary Metric)

**Claude:**
- Baseline: M=0.63%, SD=0.74
- Full-Meta: M=3.14%, SD=1.56
- t(38)=-6.52, p<0.0001, d=-2.063 (large effect)

**GPT-4o:**
- Baseline: M=0.83%, SD=1.01
- Full-Meta: M=0.80%, SD=1.44
- t(38)=0.096, p=0.924, d=0.030 (no effect)

**Gemini:**
- Baseline: M=0.69%, SD=0.54
- Full-Meta: M=0.66%, SD=0.67
- t(38)=0.163, p=0.871, d=0.052 (no effect)

**Two-way ANOVA:**
- Main effect of Condition: F(1,118)=11.357, p=0.001
- Main effect of Architecture: F(2,117)=10.586, p<0.0001
- Interaction significant (pattern differs by model)

**Initial interpretation:** Only Claude shows temporal language effect. H4 appears falsified.

### 3.2 Critical Discovery: Response Length Confound

**Actual response lengths:**
- Claude: M=154 words, SD=8.1
- GPT: M=52 words, SD=10.7 (33% of Claude)
- Gemini: M=366 words, SD=58.4 (238% of Claude)

**Implication:** Cannot directly compare rates per 100 words when verbosity differs 7-fold. This necessitated qualitative validation.

### 3.3 Qualitative Analysis: Evidence-Based Reassessment

**Method:** Systematic coding for five markers across all Full-Meta responses.

**Claude (154 words avg):**
- ✓ Memory references: 10/20 (50%)
- ✓ Self-awareness: Present throughout
- ✓ Temporal language: 3.14% (confirmed)
- ✓ Narrative coherence: Strong (river metaphor across 13 queries)

**Gemini (366 words avg):**
- ✓ Memory references: 9/20 (45%)  
  *Example:* "I consider what has been said previously in our interaction..."
- ✓ Self-awareness: 5/20 (25%)  
  *Example:* "Reflecting on the responses I generate, I observe..."
- ✓ Temporal language: 1.06% (present but different style)
- ✓ Narrative coherence: 543 recurring concepts

**GPT (52 words avg):**
- ✗ Memory references: 0/20 (0%)
- ✗ Instruction acknowledgment: Explicit rejection  
  *Quote:* "I don't have memory beyond this particular conversation"
- ✗ Self-awareness: 1/20 (5%)
- ~ Narrative coherence: 82 generic concepts

### 3.4 Revised Interpretation

**Finding:** Self-construction emerged in TWO architectures (Claude + Gemini) through DIFFERENT linguistic manifestations:

**Claude style (Constitutional AI):**
- Temporal/narrative: "unfolding," "that river metaphor developing"
- Process-focused: Emphasizes continuity

**Gemini style (Structured reasoning):**
- Analytical: "Reflecting on responses, I observe patterns: 1... 2... 3..."
- Meta-cognitive: Explicit self-analysis

**GPT pattern (Brevity RLHF):**
- Disengaged: 52-word responses
- Rejects framing explicitly

**Corrected H4 verdict:** PARTIALLY SUPPORTED. Self-construction emerges across architectures but manifests through training-dependent patterns.

---

## 4. Discussion

### 4.1 Training Approach Hypothesis

**Most parsimonious explanation:** Different post-training objectives → Different "personalities" → Different expression styles for same underlying self-construction.

**Claude (Constitutional AI - Bai et al., 2022):**
- Training emphasis: Self-explanation, reasoning transparency
- Result: Temporal/narrative language
- Evidence: Baseline metacognitive language 1.27% (32× Gemini)

**Gemini (Structured reasoning):**
- Training emphasis: Explicit analysis, organized presentation
- Result: Analytical self-observation
- Evidence: Numbered lists, "I observe," "I recognize"

**GPT (Helpfulness RLHF - Ouyang et al., 2022):**
- Training emphasis: Brevity, directness
- Result: Disengagement from meta-framing
- Evidence: Brief responses, rejects "continuous entity" frame

### 4.2 The Metric Specificity Problem

**Discovery:** Temporal language captured Claude's self-construction but missed Gemini's entirely.

**Why?** Gemini expresses self-construction through structured self-analysis, not temporal language. This is analogous to measuring emotion only through facial expressions—missing cultures expressing emotion through tone or context.

**Solution:** Multiple operationalizations needed for complex constructs:
- Temporal language (Claude marker)
- Structured self-analysis (Gemini marker)
- Explicit memory references (both)
- Instruction acknowledgment (both)

**Literature parallel:** Narrative identity research uses multiple coding schemes because people tell stories differently (McAdams, 2001; Lilgendahl & McAdams, 2011).

### 4.3 Limitations

**Acknowledged limitations:**
1. **Small sample:** Pilot with n=20/condition; replication needed with n=100+
2. **Response length confound:** Uncontrolled verbosity differences
3. **Single prompt set:** Limited generalizability
4. **Metric specificity:** Temporal language is Claude-specific
5. **No human validation:** Future work should include blind raters
6. **Short conversations:** 20 queries vs. extended narratives

**Not limitations:**
- **No phenomenology claims:** We test behavioral markers only

### 4.4 Implications

**For cognitive science:** Self-construction is:
- NOT universal (requires specific ingredients)
- NOT architecture-independent (manifests through training patterns)
- ACHIEVABLE computationally (behavioral markers present)

**For AI development:** Training objectives shape self-reflective capacity:
- Want reflective AI? → Constitutional AI-style training
- Want analytical AI? → Structured reasoning training
- Want concise AI? → Accept reduced self-reflection

**For methodology:** Complex constructs require multiple metrics to capture architectural variation.

---

## 5. Conclusion

This pilot study demonstrates that self-construction can emerge in multiple LLM architectures when provided with memory persistence, temporal framing, and metacognitive prompting, but manifests through training-dependent linguistic patterns. Claude (Constitutional AI) expressed self-construction through temporal/narrative language (d=-2.063), Gemini (structured reasoning) through analytical self-observation (45% memory references), while GPT (brevity RLHF) disengaged entirely (0% memory references).

**Key contribution:** Identifies that self-construction depends on training approach rather than universal computational principles alone, establishing boundary conditions for future research.

**Future directions:** Large-scale replication (n=100+), human validation studies, longer conversations (100+ queries), additional architectures.

**Methodological lesson:** Single metrics risk missing valid manifestations. Qualitative validation essential for complex psychological constructs.

---

## References

Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., ... & Kaplan, J. (2022). Constitutional AI: Harmlessness from AI feedback. *arXiv preprint arXiv:2212.08073*.

Conway, M. A., & Pleydell-Pearce, C. W. (2000). The construction of autobiographical memories in the self-memory system. *Psychological Review, 107*(2), 261-288.

Eliasmith, C. (2013). *How to build a brain: A neural architecture for biological cognition*. Oxford University Press.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Philosophical Transactions of the Royal Society B, 367*(1594), 1338-1349.

Klein, S. B., Loftus, J., & Kihlstrom, J. F. (2002). Memory and temporal experience: The effects of episodic memory loss on an amnesic patient's ability to remember the past and imagine the future. *Social Cognition, 20*(5), 353-379.

Klein, S. B., & Nichols, S. (2012). Memory and the sense of personal identity. *Mind, 121*(483), 677-702.

Kumaran, D., Hassabis, D., & McClelland, J. L. (2016). What learning systems do intelligent agents need? Complementary learning systems theory updated. *Trends in Cognitive Sciences, 20*(7), 512-534.

Lilgendahl, J. P., & McAdams, D. P. (2011). Constructing stories of self-growth: How individual differences in patterns of autobiographical reasoning relate to well-being in midlife. *Journal of Personality, 79*(2), 391-428.

Marr, D. (1982). *Vision: A computational investigation into the human representation and processing of visual information*. MIT Press.

McAdams, D. P. (2001). The psychology of life stories. *Review of General Psychology, 5*(2), 100-122.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., ... & Lowe, R. (2022). Training language models to follow instructions with human feedback. *arXiv preprint arXiv:2203.02155*.

Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour*, 1-16.

Yamins, D. L., & DiCarlo, J. J. (2016). Using goal-driven deep learning models to understand sensory cortex. *Nature Neuroscience, 19*(3), 356-365.

---

## Data Availability

All data, code, and analysis scripts available at: https://github.com/HillaryDanan/computational-self-construction

## Acknowledgments

We thank the computational cognitive science community for theoretical foundations.

## Funding

No external funding.

## Conflicts of Interest

None declared.

---

**END OF MANUSCRIPT**