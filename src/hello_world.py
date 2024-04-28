from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# Create a Quantum Circuit acting on a quantum register of one qubit
circ = QuantumCircuit(1)

# Add a H gate on qubit 0, putting this qubit in superposition.
circ.h(0)

# Add a measure gate to see the state.
circ.measure_all()

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
job = execute(circ, simulator, shots=1000)

# Grab the results from the job.
result = job.result()

# Returns counts
counts = result.get_counts(circ)
print("\nTotal count for 0 and 1 are:",counts)

# Draw the circuit
print("\nHere is the circuit:")
circ.draw()