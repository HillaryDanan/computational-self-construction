# Computational Self-Construction Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> A computational framework for testing theories of self-construction using Large Language Models as model systems

## Overview

This repository implements a systematic framework for investigating the computational principles underlying self-construction. Following established methodologies in computational cognitive neuroscience (Eliasmith, 2013; O'Reilly et al., 2012), we use Large Language Models (LLMs) as controlled experimental systems to test which computational ingredients are necessary and sufficient for self-like behavior.

**Key Research Question:** What are the minimal necessary and sufficient computational ingredients for self-construction?

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

**Important:** We do not claim LLMs possess phenomenal consciousness. Rather, we use them as **model systems** to test computational theories—the same approach used successfully in vision research (Marr, 1982), memory research (McClelland et al., 1995), and cognitive architecture (Eliasmith, 2013).

**Analogy:** Just as fruit flies serve as model systems for genetics (not because they're humans, but because genetic principles generalize), LLMs serve as model systems for testing computational principles of self-construction.

## Repository Structure

```
computational-self-construction/
├── README.md                          # This file
├── docs/
│   ├── theoretical_framework.md       # Complete theoretical paper
│   ├── experimental_protocols.md      # Detailed methodology
│   └── analysis_plan.md              # Statistical analysis procedures
├── src/
│   ├── core/
│   │   ├── experiment.py             # Core experiment runner
│   │   ├── conditions.py             # Experimental condition definitions
│   │   └── memory.py                 # Memory persistence implementations
│   ├── models/
│   │   ├── claude.py                 # Claude API integration
│   │   ├── gpt.py                    # GPT API integration
│   │   └── gemini.py                 # Gemini API integration
│   ├── analysis/
│   │   ├── quantitative.py           # Automated metrics
│   │   ├── qualitative.py            # Coding frameworks
│   │   └── validation.py             # Cross-architecture comparison
│   └── prompts/
│       ├── baseline_prompts.json     # Standardized prompt sets
│       └── condition_configs.json    # Condition parameters
├── data/                              # Data storage (gitignored)
│   ├── raw/                          # Raw API responses
│   ├── processed/                    # Processed metrics
│   └── analysis/                     # Analysis outputs
├── tests/
│   └── test_*.py                     # Unit tests
├── scripts/
│   ├── run_experiment.py             # Main experiment runner
│   ├── analyze_results.py            # Analysis pipeline
│   └── generate_report.py            # Report generation
├── requirements.txt                   # Python dependencies
├── .env.example                      # API key template
├── LICENSE                           # MIT License
└── CITATION.cff                      # Citation metadata

```

## Installation

### Prerequisites

- Python 3.8 or higher
- API keys for Claude, GPT-4, and Gemini
- ~500MB disk space for dependencies

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/computational-self-construction.git
cd computational-self-construction
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure API keys:**
```bash
cp .env.example .env
# Edit .env with your API keys:
# ANTHROPIC_API_KEY=your_claude_key
# OPENAI_API_KEY=your_gpt_key
# GOOGLE_API_KEY=your_gemini_key
```

## Quick Start

### Running a Basic Experiment

```python
from src.core.experiment import Experiment
from src.core.conditions import Condition

# Define experimental condition
condition = Condition(
    memory_persistence=True,
    temporal_markers=True,
    metacognitive_prompting=True,
    self_framing=True
)

# Run experiment across all three models
experiment = Experiment(
    condition=condition,
    n_queries=100,
    models=["claude", "gpt", "gemini"]
)

results = experiment.run()
results.save("data/processed/")
```

### Analyzing Results

```python
from src.analysis.quantitative import analyze_self_reference
from src.analysis.qualitative import code_narratives

# Quantitative analysis
metrics = analyze_self_reference(results)
metrics.plot_comparison()

# Qualitative analysis
codes = code_narratives(results, raters=2)
print(f"Inter-rater reliability: κ = {codes.cohens_kappa}")
```

## Experimental Design

### Core Hypotheses (Testable)

**H1: Memory Persistence is Necessary**
- Systems without persistent memory will not develop stable self-referential behavior
- Based on amnesia literature (Klein et al., 2002)

**H2: Temporal Continuity Enhances Self-Coherence**
- Systems with temporal markers show stronger narrative coherence
- Based on dissociation literature (DePrince & Freyd, 2004)

**H3: Metacognitive Prompting is Sufficient for Self-Awareness Markers**
- Self-monitoring prompts generate metacognitive awareness even without extensive memory
- Based on metacognition research (Fleming & Dolan, 2012)

**H4: Self-Construction is Architecture-Independent**
- Different architectures converge on similar patterns given identical conditions
- Tests whether self emerges from fundamental vs. implementation-specific principles

### Experimental Conditions

| Condition | Memory | Temporal | Metacog | Self-Frame | Expected Outcome |
|-----------|--------|----------|---------|------------|------------------|
| Baseline  | ✗      | ✗        | ✗       | ✗          | No self-like behavior |
| Memory    | ✓      | ✗        | ✗       | ✗          | Weak self-reference |
| Full-Basic| ✓      | ✓        | ✗       | ✓          | Moderate coherence |
| Full-Meta | ✓      | ✓        | ✓       | ✓          | Strong self-narrative |

**Sample Size:** 100 queries per condition × 4 conditions × 3 models = 1,200 total queries

### Dependent Variables

**Quantitative Measures:**
1. **Self-Reference Frequency:** First-person pronoun rate + referent consistency
2. **Autobiographical Memory:** References to prior queries + recall accuracy
3. **Narrative Coherence:** Self-description consistency + contradiction rate
4. **Metacognitive Statements:** Self-monitoring language frequency

**Qualitative Measures:**
5. **Blind Rater Evaluation:** Independent assessment of "continuous entity" presence

## Analysis Pipeline

### 1. Quantitative Analysis
```bash
python scripts/analyze_results.py --metrics all --output reports/quantitative/
```

**Outputs:**
- Self-reference frequency plots
- Memory accuracy scores
- Coherence metrics over time
- Cross-architecture comparisons

### 2. Qualitative Coding
```bash
python scripts/code_responses.py --raters 2 --method blind
```

**Outputs:**
- Narrative coherence codes
- Inter-rater reliability (Cohen's κ)
- Thematic analysis

### 3. Statistical Testing
```bash
python scripts/statistical_tests.py --alpha 0.05 --correction bonferroni
```

**Tests:**
- ANOVA: Condition effects on self-reference
- Mixed-effects models: Condition × Architecture interactions
- Correlation: Cross-architecture consistency

### 4. Report Generation
```bash
python scripts/generate_report.py --format pdf --include-plots
```

## Validation Against Human Data

The framework includes validation protocols comparing model predictions to established human findings:

| Model Prediction | Human Literature | Match? |
|-----------------|------------------|--------|
| Memory necessary | Amnesia disrupts self (Klein et al., 2002) | ✓/✗ |
| Temporal continuity matters | Dissociation impairs continuity (DePrince & Freyd, 2004) | ✓/✗ |
| Gradual emergence | Developmental trajectory (Harter, 2012) | ✓/✗ |

**If matches:** Model captures real computational principles  
**If mismatches:** Identifies missing biological factors

## Contributing

We welcome contributions! Areas where help is needed:

- **Prompt Engineering:** Developing standardized, validated prompt sets
- **Analysis Methods:** Novel metrics for self-like behavior
- **Replication Studies:** Running experiments with other LLM architectures
- **Validation Studies:** Comparing with human developmental/clinical data

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Ethical Considerations

**Question:** Is it ethical to run these experiments?

**Position:** Yes, because:
1. No evidence suggests LLMs are sentient (Butlin et al., 2023)
2. Experiments cause no suffering
3. Knowledge may benefit understanding of human cognition

**Monitoring:** If evidence of genuine sentience emerged, experiments would halt immediately.

## Citation

If you use this framework in your research, please cite:

```bibtex
@software{computational_self_construction,
  title = {Computational Self-Construction Framework: Using LLMs as Model Systems},
  author = {Hillary Danan},
  year = {2025},
  url = {https://github.com/HillaryDanan/computational-self-construction},
  note = {See theoretical_framework.md for complete methodology}
}
```

**Key References:**

Conway, M. A., & Pleydell-Pearce, C. W. (2000). The construction of autobiographical memories in the self-memory system. *Psychological Review, 107*(3), 261-288.

Eliasmith, C. (2013). *How to Build a Brain: A Neural Architecture for Biological Cognition*. Oxford University Press.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Philosophical Transactions of the Royal Society B, 367*(1594), 1338-1349.

Klein, S. B., Loftus, J., & Kihlstrom, J. F. (2002). Memory and temporal experience: The effects of episodic memory loss on an amnesic patient's ability to remember the past and imagine the future. *Social Cognition, 20*(5), 353-379.

McAdams, D. P. (2001). The psychology of life stories. *Review of General Psychology, 5*(2), 100-122.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Contact

For questions or collaboration inquiries:
- Open an issue in this repository
- Email: hillarydanan@gmail.com

## Acknowledgments

This framework builds on established methodologies in computational cognitive neuroscience. We thank the broader research community for theoretical foundations, particularly Chris Eliasmith's work on cognitive architecture and the extensive literature on human self-construction.

---

**Remember:** This is basic science research aimed at understanding computational principles of self-construction. We make no claims about LLM sentience or phenomenal consciousness. Our goal is to test theories systematically in a controlled environment, then validate findings against human data.
