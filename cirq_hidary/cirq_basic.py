"""simple program in Cirq that creates a quantum circuit with
one qubit and applies NOT gate to it."""
# pylint: disable=import-error


import typing
import cirq

if typing.TYPE_CHECKING:
    # Make sure the imports are only required for type checking
    from cirq import Circuit, GridQubit, Simulator, Result


def get_state_vector(qubit: 'GridQubit'
                     ) -> None:
    """Get the state vector of the qubit.
    I is the identity gate.
    |0⟩ = [1, 0]
    |1⟩ = [0, 1]
    I := [[1, 0], [0, 1]]
    I|0⟩ = |0⟩
    I|1⟩ = |1⟩
    """
    circuit = cirq.Circuit(cirq.I(qubit))
    simulator: "Simulator" = cirq.Simulator()
    result = simulator.simulate(circuit)
    print(f"State vector of the qubit: {result.final_state_vector}\n")


def simulating_circuit(circuit: 'Circuit',
                       repetitions: int = 20
                       ) -> 'Result':
    """Simulate the circuit"""
    simulator: "Simulator" = cirq.Simulator()
    return simulator.run(circuit, repetitions=repetitions)


def not_gate(qubit: 'GridQubit'
             ) -> 'Circuit':
    """apply NOT gate to the circuit
    NOT gate is also known as X, Pauli-X, or bit-flip gate.
    Pauli X := [[0, 1], [1, 0]
    X := |0⟩⟨1| + |1⟩⟨0|
    X|0⟩ = |1⟩
    X|1⟩ = |0⟩

    key: 'm' is used to get the measurement results.
    """
    circuit = cirq.Circuit(
        cirq.X(qubit),  # NOT gate
        cirq.measure(qubit, key='m')  # measurement
    )
    return circuit


def hadamard_gate(qubit: 'GridQubit'
                  ) -> 'Circuit':
    """apply Hadamard gate to the circuit
    Hadamard gate is also known as H gate.
    It enables us to take a qubit frin a definite state to a
    superposition of two states.
    H := [[1, 1], [1, -1]] / sqrt(2)
    H|0⟩ = (|0⟩ + |1⟩) / sqrt(2)
    H|1⟩ = (|0⟩ - |1⟩) / sqrt(2)
    the probability of measuring |0⟩ or |1⟩ is 50%.
    the phase of |0⟩ is 0 and the phase of |1⟩ is 180 degrees in the
    Bloch sphere.
    The Hadamard gate is self-inverse.
    The sqrt(2) is used to normalize the state vector and is a reult of
    the Born rule.
    """
    circuit = cirq.Circuit(
        cirq.H(qubit),  # Hadamard gate
        cirq.measure(qubit, key='m')  # measurement
    )
    return circuit


def get_histogram(result: 'Result') -> str:
    """Get the histogram of the measurement results."""
    return result.histogram(key='m')


def print_circuit(gate: str,
                  circuit: 'Circuit'
                  ) -> None:
    """Print the circuit."""
    print(f"Hello world, Here is the circuit for {gate} gate:\n"
          f"\t{circuit}")


def print_result_with_histogram(repetitions: int,
                                result: "Result"
                                ) -> None:
    """Print the measurement results for the gate."""
    print(f"\tMeasurement results: {result}\n"
          f"\tMeasurement results histogram for {repetitions} rep.:\n"
          f"\t{get_histogram(result)}\n")


def main():
    """Run the program."""
    # Pick a qubit.
    qubit = cirq.GridQubit(0, 0)

    # get the state vector of the circuit
    get_state_vector(qubit)

    # Apply NOT gate
    circuit_not = not_gate(qubit)
    print_circuit("NOT", circuit_not)

    # Simulate the circuit
    result = simulating_circuit(circuit_not, repetitions := 10)

    # Print the results
    print_result_with_histogram(repetitions, result)

    # Apply Hadamard gate
    circuit_had = hadamard_gate(qubit)

    print_circuit("Hadamard", circuit_had)

    # Simulate the circuit
    result = simulating_circuit(circuit_had, repetitions := 10)

    # Print the results
    print_result_with_histogram(repetitions, result)


if __name__ == '__main__':
    main()
