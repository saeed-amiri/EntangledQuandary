"""
quantum teleportation:
Alice wants to send a qubit to Bob.
Alice and Bob share an entangled pair of qubits.
Alice performs some operations on her qubit and her half of the entangled
pair.
Alice sends the results of her operations to Bob using classical
communication.
Bob uses the classical communication to perform operations on his half
of the entangled pair.
Bob now has the qubit that Alice wanted to send him.

The quantum teleportation protocol is a way to transfer the state of a
qubit from one location to another, using two classical bits and a Bell
pair of qubits as a quantum communication channel.

The quantum teleportation protocol consists of the following steps:
    1- Alice and Bob share an entangled pair of qubits.
    2- Alice applies a CNOT gate to her qubit and the qubit she wants to
        send to Bob.
    3- Alice applies a Hadamard gate to her qubit.
    4- Alice measures her two qubits and sends the results to Bob.
    5- Bob uses the results from Alice to perform operations on his qubit.

The quantum teleportation protocol is a fundamental building block for
quantum communication and quantum computing.

"""

import random

import cirq


def make_quantum_teleportation_circuit(ran_x: float,
                                       ran_y: float,
                                       ) -> tuple[cirq.LineQubit, cirq.Circuit
                                                  ]:
    """Make a quantum teleportation circuit.
    It will create sth like:
    0: ───X^ran_x───Y^ran_y───H───────────@───H───M('msg')───────@───
                                          │       │              │
    1: ───H──────────@────────M('bell')───X───────M──────────@───┼───
                     │        │                              │   │
    2: ──────────────X────────M──────────────────────────────X───@───
    """
    # Create a circuit with three qubits: one qubit to teleport, and two
    # qubits for the Bell pair.
    circuit = cirq.Circuit()
    msg, alice, bob = cirq.LineQubit.range(3)

    # Create a Bell pair between Alice and Bob.
    circuit.append([cirq.H(alice), cirq.CNOT(alice, bob)])
    circuit.append(cirq.measure(alice, bob, key='bell'))

    # Prepare the qubit to teleport.
    # Create a random initial state for the msg qubit, which is then
    # teleported to another qubit:
    circuit.append([cirq.X(msg)**ran_x, cirq.Y(msg)**ran_y])
    circuit.append(cirq.H(msg))
    circuit.append(cirq.CNOT(msg, alice))
    circuit.append(cirq.H(msg))
    circuit.append(cirq.measure(msg, alice, key='msg'))

    # Apply the correction operations.
    circuit.append([cirq.CNOT(alice, bob), cirq.CZ(msg, bob)])

    # Return the message and the circuit.
    return msg, circuit


def main():
    """Run the quantum teleportation protocol."""

    # Encode a random state to teleport.
    ran_x = random.random()
    ran_y = random.random()
    msg, circuit = make_quantum_teleportation_circuit(ran_x, ran_y)

    # Display the circuit.
    print("circuit for quantum teleportation:")
    print(circuit)


if __name__ == '__main__':
    main()
