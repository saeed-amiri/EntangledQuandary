"""simple program in Cirq that creates a quantum circuit with
one qubit and applies NOT gate to it."""

import cirq

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit),  # NOT gate
    cirq.measure(qubit, key='m')  # measurement
)

print("\nHello world, Here is the circuit:")
print(circuit)

# Simulate the circuit
simulator = cirq.Simulator()

# Simulate the circuit several times
result = simulator.run(circuit, repetitions=20)

# Print the results
print("\nMeasurement results:")
print(result)
print("\nMeasurement results histogram:")
print(result.histogram(key='m'))

# Apply Hadamard gate
circuit.append(cirq.H(qubit))

print("\nHello world, Here is the circuit after applying Hadamard gate:")
print(circuit)

# Simulate the circuit
result = simulator.run(circuit, repetitions=20)

# Print the results
print("\nMeasurement results:")
print(result)
print("\nMeasurement results histogram:")
print(result.histogram(key='m'))
