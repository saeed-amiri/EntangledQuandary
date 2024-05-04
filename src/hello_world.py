"""First Qiskit program."""
from qiskit import QuantumCircuit

# Create a Quantum Circuit acting on a quantum register of one qubit
circ = QuantumCircuit(1)

# Add a H gate on qubit 0, putting this qubit in superposition.
circ.h(0)

# Draw the circuit
print("\nHello world, Here is the circuit:")
print(circ)
