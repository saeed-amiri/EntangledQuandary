"""
Deutsch-Jozsa Algorithm

Deutsch-Jozsa algorithm is a quantum algorithm that solves the
Deutsch-Jozsa problem.
"The problem is to determine whether a given function is constant or
balanced. A constant function is a function that returns the same value
for all inputs, while a balanced function returns 0 for half of the
inputs and 1 for the other half."
or
"Given access to a `one bit` input and `one bit` output Boolean function,
defermine, by querying the function is `balanced` or `constant`."

DJ algorithm generalizes the approach to handel Boolen functions of `n`
inputs.

There are exactly four one-input, one-output Boolean functions:
- Constant 0 function
- Constant 1 function
- Balanced function
- Balanced function
x   f_0  f_1   f_x   f_x_not
0   0    1     0     1
1   0    1     1     0
"""

import cirq

# Get two qubits, a data qubit and target qubit, respectively
q_0, q_1 = cirq.LineQubit.range(2)

# Dictionary of oracles
oracle = {
    'constant_0': [],
    'constant_1': [cirq.X(q_1)],
    'balanced': [cirq.CNOT(q_0, q_1)],
    'balanced_': [cirq.CNOT(q_0, q_1), cirq.X(q_1)]
}
