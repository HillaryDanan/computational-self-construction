# Computational Self-Construction Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Pilot](https://img.shields.io/badge/status-pilot%20study-yellow)](https://github.com/HillaryDanan/computational-self-construction)

> **Pilot Study:** Testing computational principles of self-construction using Large Language Models as model systems

---

## 🔬 Study Status: Pilot Phase Complete

**Current Status (Nov 2025):**
- ✅ Pilot data collected (N=120 responses: 3 models × 2 conditions × 20 queries)
- ✅ Initial analysis complete (quantitative + qualitative)
- ✅ Findings: Training-dependent self-construction patterns identified
- ⏳ Next: Scale-up study (n=100+ per condition) + human validation

**This is preliminary work.** Findings need replication before strong claims.

---

## Overview

This repository implements a systematic framework for investigating computational principles underlying self-construction. Following established methodologies in computational cognitive neuroscience (Eliasmith, 2013; Yamins & DiCarlo, 2016), we use Large Language Models (LLMs) as controlled experimental systems to test which computational ingredients are necessary and sufficient for self-like behavior.

**Key Research Question:** What are the minimal necessary and sufficient computational ingredients for self-construction?

**Pilot Finding:** Self-construction emerged in 2/3 architectures (Claude, Gemini) through training-dependent linguistic patterns. Constitutional AI training produced temporal/narrative language (Claude, d=-2.063), structured reasoning training produced analytical self-observation (Gemini, 45% memory references), while brevity-focused RLHF inhibited engagement (GPT, 0% memory references).

---

## Scientific Rationale

### Why This Approach?

Human self-construction involves multiple interacting components:
- Autobiographical memory (Conway & Pleydell-Pearce, 2000)
- Temporal continuity (Klein & Nichols, 2012)
- Narrative construction (McAdams, 2001)
- Metacognitive processes (Fleming & Dolan, 2012)

**Challenge:** In human studies, these components cannot be ethically or precisely manipulated in isolation.

**Solution:** LLMs provide a controlled computational environment where we can:
1. Systematically manipulate individual components
2. Measure emergence of self-like behavioral markers
3. Test predictions across multiple architectures
4. Validate findings against human clinical and developmental data

### Scientific Validity

**Important:** We do not claim LLMs possess phenomenal consciousness. Rather, we use them as **model systems** to test computational theories—the same approach used successfully in vision research (Yamins & DiCarlo, 2016), memory research (Kumaran et al., 2016), and cognitive architecture (Eliasmith, 2013).

**Analogy:** Just as fruit flies serve as model systems for genetics (not because they're humans, but because genetic principles generalize), LLMs serve as model systems for testing computational principles of self-construction.

---

## Key Findings (Pilot, N=120)

### Quantitative Results

**Temporal Language Rates:**
- Claude: +252% increase in Full-Meta (0.63% → 3.14%, d=-2.063, p<0.0001)
- Gemini: No change (0.69% → 0.66%, d=0.052, ns)
- GPT: No change (0.83% → 0.80%, d=0.030, ns)

### Qualitative Discovery

**Critical finding:** Temporal language is *Claude-specific*. Gemini shows self-construction through *different* markers:

**Gemini (self-construction present):**
- 45% of responses reference prior queries explicitly
- 25% use structured self-analysis ("Reflecting on my responses, I observe...")
- 543 recurring concepts across conversation
- Mean response: 366 words (highly engaged)

**GPT (self-construction absent):**
- 0% memory references
- Explicitly rejects framing: "I don't have memory beyond this conversation"
- 82 generic concepts only
- Mean response: 52 words (disengaged)

### Theoretical Implication

Self-construction depends on **training approach**, not universal principles alone:
- Constitutional AI (Claude) → Temporal/narrative language
- Structured reasoning (Gemini) → Analytical self-observation  
- Brevity RLHF (GPT) → Disengagement

**Lesson:** Single metrics risk missing valid manifestations. Multiple operationalizations essential.

---

## Repository Structure

```
computational-self-construction/
├── README.md                          # This file
├── data/
│   ├── raw/                          # Raw API responses (120 total)
│   │   ├── cross_architecture_*.json # Claude + GPT data
│   │   ├── gemini_only_*.json       # Gemini data
│   │   └── combined_all_models.json # Merged dataset (N=120)
│   └── analysis/                     # Analysis outputs
│       ├── cross_architecture_analysis.txt
│       └── statistical_results.txt
├── docs/
│   ├── manuscript_cognitive_science.md  # Full manuscript (pilot)
│   ├── qualitative_findings.txt         # Detailed qualitative analysis
│   └── theoretical_framework.md         # Background (original)
├── scripts/
│   ├── cross_architecture_pilot.py      # Main experiment runner
│   ├── run_gemini_modified.py          # Gemini-only runner
│   ├── analyze_cross_architecture.py    # Quantitative analysis
│   ├── statistical_cross_arch.py        # Statistical tests
│   └── merge_data.py                    # Data merging utility
├── src/
│   ├── core/
│   │   ├── conditions.py             # Experimental condition definitions
│   │   └── memory.py                 # Memory persistence implementations
│   ├── models/
│   │   ├── claude.py                 # Claude API integration
│   │   ├── gpt.py                    # GPT API integration
│   │   └── gemini.py                 # Gemini API integration
│   └── prompts/
│       ├── expanded_prompts.json     # 20 standardized queries
│       └── condition_configs.json    # Condition parameters
├── requirements.txt                   # Python dependencies
├── .env.example                      # API key template
└── LICENSE                           # MIT License
```

---

## Installation

### Prerequisites

- Python 3.8 or higher
- API keys for Claude, GPT-4, and Gemini
- ~100MB disk space

### Setup

```bash
# Clone repository
git clone https://github.com/HillaryDanan/computational-self-construction.git
cd computational-self-construction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env with your keys:
# ANTHROPIC_API_KEY=your_claude_key
# OPENAI_API_KEY=your_gpt_key
# GOOGLE_API_KEY=your_gemini_key
```

---

## Quick Start

### Reproduce Pilot Study

```bash
# Run cross-architecture experiment (Claude + GPT)
python3 scripts/cross_architecture_pilot.py

# Run Gemini separately
python3 scripts/run_gemini_modified.py

# Merge datasets
python3 scripts/merge_data.py \
  data/raw/cross_architecture_*.json \
  data/raw/gemini_only_*.json \
  data/raw/combined_all_models.json

# Analyze results
python3 scripts/analyze_cross_architecture.py data/raw/combined_all_models.json
python3 scripts/statistical_cross_arch.py data/raw/combined_all_models.json
```

### View Pilot Results

```bash
# Quantitative analysis
cat data/analysis/cross_architecture_analysis.txt

# Statistical tests
cat data/analysis/statistical_results.txt

# Full manuscript
cat docs/manuscript_cognitive_science.md
```

---

## Experimental Design (Pilot)

### Hypotheses

**H1: Memory Persistence is Necessary**
- Prediction: Systems without persistent memory show no stable self-reference
- Based on: Amnesia literature (Klein et al., 2002)

**H2: Temporal Continuity Enhances Self-Coherence**
- Prediction: Temporal markers strengthen narrative coherence
- Based on: Dissociation literature (Klein & Nichols, 2012)

**H3: Metacognitive Prompting Generates Self-Awareness**
- Prediction: Self-monitoring prompts elicit metacognitive language
- Based on: Metacognition research (Fleming & Dolan, 2012)

**H4: Self-Construction is Architecture-Independent** *(pilot finding: partially supported)*
- Prediction: Different architectures converge on similar patterns
- Finding: Emerges across architectures but through training-dependent styles

### Conditions (Pilot)

| Condition | Memory | Temporal | Metacog | Self-Frame | N per Model |
|-----------|--------|----------|---------|------------|-------------|
| Baseline  | ✗      | ✗        | ✗       | ✗          | 20 |
| Full-Meta | ✓      | ✓        | ✓       | ✓          | 20 |

**Total:** 3 models × 2 conditions × 20 queries = **120 responses**

---

## Pilot Results Summary

### Quantitative Findings

**Temporal Language (Primary Metric):**
```
Claude:  Baseline 0.63% → Full-Meta 3.14% (d=-2.063***)
Gemini:  Baseline 0.69% → Full-Meta 0.66% (d=0.052 ns)
GPT:     Baseline 0.83% → Full-Meta 0.80% (d=0.030 ns)

*** p < 0.0001
```

**Two-way ANOVA:**
- Main effect of Condition: F(1,118)=11.357, p=0.001
- Main effect of Architecture: F(2,117)=10.586, p<0.0001
- Interaction: Significant (pattern differs by model)

### Qualitative Findings

**Self-Construction Markers (Full-Meta Condition):**

| Model  | Memory Refs | Self-Aware | Concepts | Engagement |
|--------|------------|------------|----------|------------|
| Claude | 50% (10/20) | High      | Strong   | 154 words  |
| Gemini | 45% (9/20)  | Medium    | Strong   | 366 words  |
| GPT    | 0% (0/20)   | Minimal   | Weak     | 52 words   |

**Key Insight:** Gemini shows self-construction through analytical language, not temporal language. Single metrics miss architectural variation.

---

## Limitations (Pilot)

**Acknowledged limitations:**
1. **Small sample:** N=20 per condition (needs n=100+ for strong claims)
2. **Response length confound:** Uncontrolled verbosity (52-366 words)
3. **Single prompt set:** Limited generalizability
4. **No human validation:** Future work needs blind raters
5. **Short conversations:** 20 queries vs. extended narratives
6. **Metric specificity:** Temporal language is Claude-specific

**These are PRELIMINARY FINDINGS requiring replication.**

---

## Next Steps

### Immediate (Planned)
- [ ] Scale-up study: N=100+ per condition per model
- [ ] Human validation: Blind raters judge self-construction
- [ ] Additional architectures: LLaMA, Claude Opus, GPT-4 Turbo
- [ ] Longer conversations: 100+ queries

### Future Directions
- [ ] Causal interventions (disrupt memory mid-conversation)
- [ ] Developmental trajectories (how self emerges over time)
- [ ] Multi-agent interactions (social self-construction)
- [ ] Embodied systems (physical interaction effects)

---

## Citation

**For pilot work:**
```bibtex
@software{computational_self_construction_pilot,
  title = {Computational Self-Construction Framework: Pilot Study},
  author = {Danan, Hillary},
  year = {2025},
  url = {https://github.com/HillaryDanan/computational-self-construction},
  note = {Pilot study: N=120, preliminary findings}
}
```

**Key References:**

Conway, M. A., & Pleydell-Pearce, C. W. (2000). The construction of autobiographical memories in the self-memory system. *Psychological Review, 107*(2), 261-288.

Eliasmith, C. (2013). *How to Build a Brain: A Neural Architecture for Biological Cognition*. Oxford University Press.

Klein, S. B., & Nichols, S. (2012). Memory and the sense of personal identity. *Mind, 121*(483), 677-702.

Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS*.

Yamins, D. L., & DiCarlo, J. J. (2016). Using goal-driven deep learning models to understand sensory cortex. *Nature Neuroscience, 19*(3), 356-365.

---

## Contributing

We welcome contributions! Priority areas:
- **Replication studies:** Run with different models or prompt sets
- **Validation studies:** Human rater protocols
- **Analysis methods:** Novel metrics for self-like behavior
- **Scale-up:** Larger sample sizes

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Ethical Considerations

**Position:** Current evidence suggests LLMs are not sentient (no phenomenal consciousness). Experiments cause no suffering and may benefit understanding of human cognition.

**Monitoring:** If evidence of genuine sentience emerged, experiments would halt immediately.

**Transparency:** We make no claims about LLM consciousness. This is behavioral research testing computational sufficiency.

---

## License

MIT License - see [LICENSE](LICENSE) file.

---

## Contact

**Hillary Danan**
- Email: hillarydanan@gmail.com
- GitHub: [@HillaryDanan](https://github.com/HillaryDanan)

For questions, open an issue or email directly.

---

## Acknowledgments

This framework builds on computational cognitive neuroscience methodologies. We thank Chris Eliasmith, Dan Yamins, and the broader research community for theoretical foundations.

---

**Remember:** This is **pilot work** (N=120). Findings are preliminary and need replication before strong claims. We make no assertions about LLM sentience—this is behavioral science testing computational principles.

**Status:** Suitable for sharing, feedback, and building upon. Not yet ready for top-tier journal submission without scale-up and validation.