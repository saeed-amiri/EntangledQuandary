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

There are many ways to prepare the Bell states:
1- Start from state |00> and Using the Hadamard gate and the CNOT gate,
which gives the first Bell state |Φ+⟩.
If we apply the X_2 gate to |Φ+⟩, we get the second Bell state |Φ-⟩:
X_2|Φ+⟩ = (I ⊗ X) (|00⟩ + |11⟩)/√2
            -> |00⟩ - |11⟩  = |Φ-⟩
The third and fourth Bell states |Ψ+⟩ and |Ψ-⟩ are prepared by applying
X_2 Z_2 |Φ+⟩ and X_2 Z_2 |Φ-⟩, respectively.
Note that X_2 = X ⊗ I and Z_2 = I ⊗ Z.
X|0> = |1> and Z|1> = -|1>
X|1> = |0> and Z|0> = |0>

2- Start from state |01> and Using the Hadamard gate and the CNOT gate,
which gives the third Bell state |Ψ+⟩.

3- Start from state |10> and Using the Hadamard gate and the CNOT gate,
which gives the fourth Bell state |Ψ-⟩.

Also see the flloing link from qiskit:
https://quantumcomputinguk.org/tutorials/introduction-to-bell-states
"""

# pylint: disable=import-error

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
    print("circuit for |\\phi+>:")
    print(circ)

    message(circ, qreg)
    print(simulate(circ, 10), end='\n\n')


def bell_psi_plus(qreg: cirq.Qid,
                  circ: cirq.Circuit) -> None:
    """
    The third Bell state
    |Ψ+⟩ = (|01⟩ + |10⟩)/√2
    0: ───H───@───
              │
    1: ───X───X───
    """
    # Apply the X pauli to the first qubit.
    circ.append(cirq.X(qreg[1]))

    # Apply the Hadamard gate to the first qubit.
    circ.append(cirq.H(qreg[0]))

    # Apply the CNOT gate to the first and second qubits.
    circ.append(cirq.CNOT(qreg[0], qreg[1]))

    # Display the circuit.
    print("circuit for |\\psi+>:")
    print(circ)

    message(circ, qreg)
    print(simulate(circ, 10), end='\n\n')


def bell_phi_minus(qreg: cirq.Qid,
                   circ: cirq.Circuit
                   ) -> None:
    """
    The second Bell state
    |Φ-⟩ = (|00⟩ - |11⟩)/√2
    0: ───X───H───@───
                  │
    1: ───────────X───
    """
    # Apply the X pauli to the first qubit.
    circ.append(cirq.X(qreg[0]))

    # Apply the Hadamard gate to the first qubit.
    circ.append(cirq.H(qreg[0]))

    # Apply the CNOT gate to the first and second qubits.
    circ.append(cirq.CNOT(qreg[0], qreg[1]))

    # Display the circuit.
    print("circuit for |\\phi->:")
    print(circ)

    message(circ, qreg)
    print(simulate(circ, 10), end='\n\n')


def bell_psi_minus(qreg: cirq.Qid,
                   circ: cirq.Circuit
                   ) -> None:
    """
    The fourth Bell state
    |Ψ-⟩ = (|01⟩ - |10⟩)/√2
    0: ───H───Z───@───
                  │
    1: ───X───Z───X───
                  │
    """
    # Apply the X pauli to the first qubit.
    circ.append(cirq.X(qreg[1]))

    # Apply the Hadamard gate to the first qubit.
    circ.append(cirq.H(qreg[0]))

    # Apply the Z pauli to the first and second qubits.
    circ.append(cirq.Z(qreg[0]))
    circ.append(cirq.Z(qreg[1]))

    # Apply the CNOT gate to the first and second qubits.
    circ.append(cirq.CNOT(qreg[0], qreg[1]))

    # Display the circuit.
    print("circuit for |\\psi->:")
    print(circ)

    message(circ, qreg)
    print(simulate(circ, 10), end='\n\n')


def message(circ: cirq.Circuit,
            qreg: cirq.Qid,
            key: str = 'z'
            ) -> None:
    """ measure the qubits """
    return circ.append(cirq.measure(*qreg, key=key))


def simulate(circ: cirq.Circuit,
             repetitions: int = 10
             ) -> cirq.Result:
    """ simulate the circuit """
    return cirq.Simulator().run(circ, repetitions=repetitions)


# Create a quantum circuit.
QREG = cirq.LineQubit.range(2)
CIRC = cirq.Circuit()


bell_phi_plus(QREG, CIRC.copy())

bell_psi_plus(QREG, CIRC.copy())

bell_phi_minus(QREG, CIRC.copy())

bell_psi_minus(QREG, CIRC.copy())
