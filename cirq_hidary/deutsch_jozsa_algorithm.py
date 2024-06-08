"""
Deutsch-Jozsa Algorithm

Deutsch-Jozsa algorithm  (DJA) is a quantum algorithm that solves the
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
____________________________
Recap:
Problem: Determine if a given function is constant or balanced.
Classical solution: Requires 2^(n-1) + 1 evaluations.
Quantum solution (DJA): Requires only one evaluation.

Steps of DJA:
    1. Start with n qubits intialized to |0> and an auxiliary qubit |1>.
    2. Apply Hadamard gate to all qubits and the auxiliary qubit:
        H|0> = (|0> + |1>) / sqrt(2) = |+>
        H|1> = (|0> - |1>) / sqrt(2) = |->
        Applying H gate to n qubits:
        (1/sqrt(2)^n) * sum_{x=0}^{2^n-1} |x> (*) (1/sqrt(2))(|0> - |1>)
        for n = 1:
            |x> = |0> and |1>
        for n = 2:
            |x> = |00>, |01>, |10>, |11>
    3. Apply the Orcle (function). Which flips the sign of the amplitude
        of the state based on the value of the function: Orcale function
        In quantum computing the an orcale is a black box that used to
        encode a function to a quantum state:
        The orcale function operates on a two registers (set of qubits):
            - The first register (n qubits), the input x
            - The second register (a single qubit), the output f(x)
            U_f|x>|y> = |x>|y XOR f(x)>
        Ruule of the oracle:
        U_f|x>|+> = (-1)^f(x)|x>|+>
        which means that the oracle flips the sign of the amplitude of
        the state based on the value of the function.
        This flipping the sign of the amplitude is the key to determining
        the nature of the function.
    4. Apply Hadamard gate to the first n qubits.The measurment indicates
        whether the function is constant or balanced.
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
