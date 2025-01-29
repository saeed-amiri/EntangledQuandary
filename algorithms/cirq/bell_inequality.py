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
After the refree flip a coin:
Note: See the order of the states, first Alice, third Bob
    (0, 0): ───H───@───X^-0.25───
                   │
    (0, 1): ───H───┼─────────────
                   │
    (1, 0): ───────X─────────────

    (1, 1): ───H─────────────────

After players play sqrt(X):
    (0, 0): ───H───@───X^-0.25───X^0.5───
                   │             │
    (0, 1): ───H───┼─────────────@───────
                   │
    (1, 0): ───────X───X^0.5─────────────
                       │
    (1, 1): ───H───────@─────────────────

After collecting the measurements:
    (0, 0): ───H───@───X^-0.25───X^0.5────M('a')───
                   │             │
    (0, 1): ───H───┼─────────────@────────M('x')───
                   │
    (1, 0): ───────X───X^0.5─────M('b')────────────
                       │
    (1, 1): ───H───────@─────────M('y')────────────

"""
# pylint: disable=import-error

import numpy as np

import cirq


def bit_string(bits: list[int]) -> str:
    """return bit in string fasion"""
    return ''.join('1' if e else '_' for e in bits)


def make_bell_test_circuit() -> cirq.Circuit:
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
        cirq.X(alice)**(-0.25)
        ])
    print(f'\nIntitial circuit is:\n{circuit}')

    # Refrees flip coins
    circuit.append([
        cirq.H(alice_refree),
        cirq.H(bob_refree)
    ])
    print(f'\nAfter refrees flip coins, circuit is:\n{circuit}')

    # Players do a sqrt(X) based on their referee's coin
    circuit.append([
        cirq.CNOT(alice_refree, alice)**(0.5),
        cirq.CNOT(bob_refree, bob)**(0.5)
    ])
    print(f"\nAfter players play sqrt(X):\n{circuit}")

    # The results are recorded
    circuit.append([
        cirq.measure(alice, key='a'),
        cirq.measure(bob, key='b'),
        cirq.measure(alice_refree, key='x'),
        cirq.measure(bob_refree, key='y')
    ])
    print(f"\nAfter collecting the measurements:\n{circuit}")

    return circuit


def main() -> None:
    """Bell inequalty"""
    # Create a circuit
    circuit = make_bell_test_circuit()

    # Run the simulations
    repetitions = 1000
    print(f"\nSimulating {repetitions} repetitions...\n")
    result: "cirq.study.result.ResultDict" = \
        cirq.Simulator().run(program=circuit, repetitions=repetitions)

    # Collect results
    a_result: np.ndarray = np.array(result.measurements['a'][:, 0])
    b_result: np.ndarray = np.array(result.measurements['b'][:, 0])
    x_result: np.ndarray = np.array(result.measurements['x'][:, 0])
    y_result: np.ndarray = np.array(result.measurements['y'][:, 0])

    # Compute the winning percentage
    outcomes = a_result ^ b_result == x_result & y_result
    win_precentage: float = len([e for e in outcomes if e]) * 100 / repetitions

    if SHOW_ARRAYS:
        print("\nResults are:"
              f"Alice: {bit_string(a_result)}"
              f"Bob: {bit_string(b_result)}"
              f"Alice_Refree: {bit_string(x_result)}"
              f"Bob_refree: {bit_string(y_result)}"
              )
        print(f"(Alice XOR Bob) == (x AND y)\n{bit_string(outcomes)}")

    print(f"Win rate: {win_precentage}")


if __name__ == '__main__':
    SHOW_ARRAYS: bool = False
    main()
