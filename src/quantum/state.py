"""Quantum State Vector representation for N qubits."""
import numpy as np

class QuantumState:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.dim = 1 << num_qubits
        # Initialize to state |00...0>
        self.vector = np.zeros(self.dim, dtype=np.complex128)
        self.vector[0] = 1.0 + 0.0j

    def get_probabilities(self) -> np.ndarray:
        return np.abs(self.vector) ** 2

    def is_normalized(self) -> bool:
        return bool(np.isclose(np.sum(self.get_probabilities()), 1.0))
