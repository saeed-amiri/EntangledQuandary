"""
simulate a circuit that mimic the Bell inequality
Here is the main idea:
    1. A rferee prepares a pair of entangled qubits
    2. The referee sends one qubit to Alice (x) and the other to Bob (y)
    3. Alice and Bob measure their qubits (a(x), b(y))
    4. Alice and Bob send the results to the referee
    5. The referee checks the results:
        if a(x) XOR b(y) == xy they win
        else they lose(
In quantum version of the game, Alice and Bob can set a strategy to win
First preapre a Bell state between Alice and Bob and apply and a control
-sqrt(X), the circuit will be:
    (0, 0): ───H───@───X^-0.25───
                   │
    (1, 0): ───────X─────────────
"""
# pylint: disable=import-error

import numpy as np

import cirq


def make_bell_test_circuit() -> None:
    """make a bell test circuit"""
    # Qubit for Alice, Bob, Refree
    alice: "cirq.devices.grid_qubit.GridQubit" = cirq.GridQubit(0, 0)
    bob: "cirq.devices.grid_qubit.GridQubit" = cirq.GridQubit(1, 0)

    alice_refree: "cirq.devices.grid_qubit.GridQubit" = cirq.GridQubit(0, 1)
    bob_refree: "cirq.devices.grid_qubit.GridQubit" = cirq.GridQubit(1, 1)

    circuit: "cirq.circuits.circuit.Circuit" = cirq.Circuit()

    # Prepare shared entangeld state between Alice and Bob
    circuit.append([
        cirq.H(alice),
        cirq.CNOT(alice, bob),
        cirq.X(alice)**(-1/4.0)
        ])
    print(circuit)


def main() -> None:
    """Bell inequalty"""
    # Create a circuit
    circuit = make_bell_test_circuit()


if __name__ == '__main__':
    main()
