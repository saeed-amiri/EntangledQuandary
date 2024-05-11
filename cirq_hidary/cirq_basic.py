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
    """Get the state vector of the qubit."""
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
    """apply Hadamard gate to the circuit"""
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
    circuit = not_gate(qubit)
    print_circuit("NOT", circuit)

    # Simulate the circuit
    result = simulating_circuit(circuit, repetitions := 1)

    # Print the results
    print_result_with_histogram(repetitions, result)

    # Apply Hadamard gate
    circuit = hadamard_gate(qubit)

    print_circuit("Hadamard", circuit)

    # Simulate the circuit
    result = simulating_circuit(circuit, repetitions := 10)

    # Print the results
    print_result_with_histogram(repetitions, result)


if __name__ == '__main__':
    main()
