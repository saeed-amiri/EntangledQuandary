"""
Simple Qiskit program to demonstrate the basic concepts of Quantum
Computing
"""

import qiskit

# Create a quantum register with 1 qubit.
qreg = qiskit.QuantumRegister(1, 'qreg')

# Create a classical register with 1 bit.
creg = qiskit.ClassicalRegister(1, 'creg')

# Create a quantum circuit with the quantum and classical registers.
circ = qiskit.QuantumCircuit(qreg, creg)

# Apply the Not gate to the qubit.
circ.x(qreg[0])

# Measure the qubit.
circ.measure(qreg, creg)

# Print the circuit.
print(circ.draw())

# Get a backend to run the quantum circuit.
# backend = qiskit.BasicAer.get_backend("qasm_simulator")

# Execute the circuit on the backend.
# job = qiskit.execute(circ, backend, shots=10)
# result = job.result()

# Print the result.
# print(result.get_counts())