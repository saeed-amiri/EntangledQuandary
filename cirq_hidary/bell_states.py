"""
Script for preparing the Bell states using Cirq.
|Φ+⟩ = (|00⟩ + |11⟩)/√2
0: ───H───@───
          │
1: ───────X───

|Φ-⟩ = (|00⟩ - |11⟩)/√2
|Ψ+⟩ = (|01⟩ + |10⟩)/√2
|Ψ-⟩ = (|01⟩ - |10⟩)/√2
"""

import cirq


def bell_phi_plus(qreg: cirq.Qid,
                  circ: cirq.Circuit) -> None:
    """
    |Φ+⟩ = (|00⟩ + |11⟩)/√2
    0: ───H───@───
              │
    1: ───────X───
    """
    # Apply the Hadamard gate to the first qubit.
    circ.append(cirq.H(qreg[0]))

    # Apply the CNOT gate to the first and second qubits.
    circ.append(cirq.CNOT(qreg[0], qreg[1]))

    # Display the circuit.
    print("circuit:")
    print(circ)


# Create a quantum circuit.
QREG = cirq.LineQubit.range(2)
CIRC = cirq.Circuit()

bell_phi_plus(QREG, CIRC.copy())
