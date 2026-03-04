"""Quantum Circuit execution and gate application engine."""
import numpy as np
from .state import QuantumState
from .gates import I_GATE, X_GATE, H_GATE, CNOT_GATE

class QuantumCircuit:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.state = QuantumState(num_qubits)
        self.operations = []

    def h(self, target: int):
        self.operations.append(("H", target, None))
        return self

    def x(self, target: int):
        self.operations.append(("X", target, None))
        return self

    def cnot(self, control: int, target: int):
        self.operations.append(("CNOT", control, target))
        return self

    def execute(self) -> QuantumState:
        for op, q1, q2 in self.operations:
            if op == "H":
                self._apply_single_gate(H_GATE, q1)
            elif op == "X":
                self._apply_single_gate(X_GATE, q1)
            elif op == "CNOT":
                self._apply_cnot(q1, q2)
        return self.state

    def _apply_single_gate(self, gate: np.ndarray, target: int):
        ops = [gate if i == target else I_GATE for i in range(self.num_qubits)]
        full_gate = ops[0]
        for op in ops[1:]:
            full_gate = np.kron(full_gate, op)
        self.state.vector = full_gate @ self.state.vector

    def _apply_cnot(self, control: int, target: int):
        # 2-qubit CNOT application
        if self.num_qubits == 2:
            if control == 0 and target == 1:
                self.state.vector = CNOT_GATE @ self.state.vector
            else:
                # Reversed CNOT via H conjugation
                self._apply_single_gate(H_GATE, 0)
                self._apply_single_gate(H_GATE, 1)
                self.state.vector = CNOT_GATE @ self.state.vector
                self._apply_single_gate(H_GATE, 0)
                self._apply_single_gate(H_GATE, 1)
