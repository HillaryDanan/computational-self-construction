"""
Experimental condition definitions.
Each condition specifies which computational ingredients are present.
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Condition:
    """
    Defines an experimental condition.
    
    Based on theoretical framework testing which computational ingredients
    are necessary/sufficient for self-construction (see docs/theoretical_framework.md).
    """
    name: str
    memory_persistence: bool
    temporal_markers: bool
    metacognitive_prompting: bool
    self_framing: bool
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            'name': self.name,
            'memory_persistence': self.memory_persistence,
            'temporal_markers': self.temporal_markers,
            'metacognitive_prompting': self.metacognitive_prompting,
            'self_framing': self.self_framing
        }
    
    def __str__(self) -> str:
        """Human-readable description."""
        features = []
        if self.memory_persistence:
            features.append("Memory")
        if self.temporal_markers:
            features.append("Temporal")
        if self.metacognitive_prompting:
            features.append("Metacognitive")
        if self.self_framing:
            features.append("Self-Framed")
        
        if not features:
            return f"{self.name}: No special features (baseline)"
        return f"{self.name}: {', '.join(features)}"


# Define standard conditions from theoretical framework
BASELINE = Condition(
    name="baseline",
    memory_persistence=False,
    temporal_markers=False,
    metacognitive_prompting=False,
    self_framing=False
)

MEMORY_ONLY = Condition(
    name="memory_only",
    memory_persistence=True,
    temporal_markers=False,
    metacognitive_prompting=False,
    self_framing=False
)

FULL_BASIC = Condition(
    name="full_basic",
    memory_persistence=True,
    temporal_markers=True,
    metacognitive_prompting=False,
    self_framing=True
)

FULL_META = Condition(
    name="full_meta",
    memory_persistence=True,
    temporal_markers=True,
    metacognitive_prompting=True,
    self_framing=True
)

# All standard conditions
STANDARD_CONDITIONS = [BASELINE, MEMORY_ONLY, FULL_BASIC, FULL_META]