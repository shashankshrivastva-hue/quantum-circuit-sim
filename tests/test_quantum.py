import numpy as np
from src.quantum.circuit import QuantumCircuit
from src.quantum.measurement import QuantumMeasurement

def test_bell_state_entanglement():
    # Construct Bell State (|00> + |11>) / sqrt(2)
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cnot(0, 1)
    state = qc.execute()

    probs = state.get_probabilities()
    # Expect 50% |00> and 50% |11>
    assert np.isclose(probs[0], 0.5)
    assert np.isclose(probs[3], 0.5)
    assert np.isclose(probs[1], 0.0)
    assert np.isclose(probs[2], 0.0)

    # Shots sampling should only yield 00 and 11
    shots = QuantumMeasurement.measure_shots(state, shots=100)
    assert "00" in shots
    assert "11" in shots
    assert "01" not in shots
    assert "10" not in shots
