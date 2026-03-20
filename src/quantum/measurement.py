"""Measurement collapse according to Born rule."""
import numpy as np
from typing import Dict
from .state import QuantumState

class QuantumMeasurement:
    @staticmethod
    def measure_shots(state: QuantumState, shots: int = 1024) -> Dict[str, int]:
        probs = state.get_probabilities()
        num_qubits = state.num_qubits
        outcomes = np.random.choice(len(probs), size=shots, p=probs)

        counts = {}
        for idx in range(len(probs)):
            bin_str = format(idx, f"0{num_qubits}b")
            counts[bin_str] = 0

        for outcome in outcomes:
            bin_str = format(outcome, f"0{num_qubits}b")
            counts[bin_str] += 1

        return {k: v for k, v in counts.items() if v > 0}
