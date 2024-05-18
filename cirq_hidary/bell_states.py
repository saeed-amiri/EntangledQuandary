"""
Script for preparing the Bell states using Cirq.
In Bell's original paper, he described four maximally entangled states.
These states are known as the Bell states.
The Bell states are prepared using a Hadamard gate and a CNOT gate.
The four Bell states are:

|Φ+⟩ = (|00⟩ + |11⟩)/√2
|Φ-⟩ = (|00⟩ - |11⟩)/√2
|Ψ+⟩ = (|01⟩ + |10⟩)/√2
|Ψ-⟩ = (|01⟩ - |10⟩)/√2

In Bell statesm for |Φ+⟩, the Hadamard gate is applied to the first qubit
and the CNOT gate is applied to the first and second qubits.
The circuit for |Φ+⟩ is:
H|00> = (H ⊗ I) (|0⟩ ⊗ |0⟩)
      -> (H|0⟩) ⊗ |0⟩ -> (|0⟩ + |1⟩) ⊗ |0⟩ -> |00⟩ + |11⟩
CNOT|00> = (CNOT ⊗ I) (|0⟩ ⊗ |0⟩)
         -> (CNOT|0⟩) ⊗ |0⟩ -> |0⟩ ⊗ |0⟩ -> |00⟩
         -> (CNOT|1⟩) ⊗ |0⟩ -> |1⟩ ⊗ |1⟩ -> |11⟩
-> |Φ+⟩ = (|00⟩ + |11⟩)/√2

The circuit for |Ψ+⟩ is:
H|01> = (H ⊗ I) (|0⟩ ⊗ |1⟩)
      -> (H|0⟩) ⊗ |1⟩ -> (|0⟩ + |1⟩) ⊗ |1⟩ -> |01⟩ + |11⟩
CNOT|01> = (CNOT ⊗ I) (|0⟩ ⊗ |1⟩)
         -> (CNOT|0⟩) ⊗ |1⟩ -> |0⟩ ⊗ |1⟩ -> |01⟩
         -> (CNOT|1⟩) ⊗ |1⟩ -> |1⟩ ⊗ |0⟩ -> |10⟩
-> |Ψ+⟩ = (|01⟩ + |10⟩)/√2

For |Φ-⟩ and |Ψ-⟩, the Pauli-Z gate is applied to the second qubit.
The Pauli-Z gate is a quantum gate that acts as the identity on the |0⟩
state and as a phase flip (sign change) on the |1⟩ state.
The Pauli-Z gate is represented by the following matrix:
Z = |1 0|
    |0 -1|
The circuit for |Φ-⟩ calculates by applying the Pauli-Z gate to  |Φ+⟩.
The circuit for |Ψ-⟩ calculates by applying the Pauli-Z gate to  |Ψ+⟩.
|Φ-⟩ = (|00⟩ - |11⟩)/√2
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
