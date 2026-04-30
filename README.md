# ⚛️ Quantum Circuit Simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)](https://numpy.org)

High-performance arbitrary N-qubit quantum state vector simulator and circuit compiler supporting Kronecker tensor product gate compilation and Monte Carlo measurement collapse.

---

## 🏛️ Simulation Architecture

```mermaid
flowchart LR
    State["Initial State |0...0>"] --> Circuit[Circuit Gate Composer]
    Circuit --> Kron["Kronecker Tensor Compilation (U ⊗ I)"]
    Kron --> Multiply["Unitary Vector Multiplication U|ψ>"]
    Multiply --> Superposition["Superposition State Vector |ψ>"]
    Superposition --> Born["Born's Rule P(x) = |⟨x|ψ⟩|²"]
    Born --> Shots["Monte Carlo Sampling (1024 Shots)"]
```

## 🚀 Creating Entanglement (Bell State)

```python
from src.quantum.circuit import QuantumCircuit
from src.quantum.measurement import QuantumMeasurement

# Build Bell State (|00⟩ + |11⟩) / √2
qc = QuantumCircuit(2)
qc.h(0).cnot(0, 1)

state = qc.execute()
print("State probabilities:", state.get_probabilities())

# Measure
shots = QuantumMeasurement.measure_shots(state, shots=1024)
print("Measurement counts:", shots)
# Output: {'00': 518, '11': 506}
```

## 📜 License
MIT License. Built by [Shashank Shrivastva](https://github.com/shashankshrivastva-hue).
