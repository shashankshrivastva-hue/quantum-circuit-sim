"""Universal Quantum Gate Definitions."""
import numpy as np

# 1-Qubit Gates
I_GATE = np.array([[1, 0], [0, 1]], dtype=np.complex128)
X_GATE = np.array([[0, 1], [1, 0]], dtype=np.complex128) # Pauli-X / NOT
Y_GATE = np.array([[0, -1j], [1j, 0]], dtype=np.complex128) # Pauli-Y
Z_GATE = np.array([[1, 0], [0, -1]], dtype=np.complex128) # Pauli-Z
H_GATE = (1.0 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=np.complex128) # Hadamard
S_GATE = np.array([[1, 0], [0, 1j]], dtype=np.complex128) # Phase S
T_GATE = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=np.complex128) # T gate

# 2-Qubit CNOT Matrix
CNOT_GATE = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], dtype=np.complex128)
