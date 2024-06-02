"""
simulate a circuit that mimic the Bell inequality
Here is the main idea:
    1. A rferee prepares a pair of entangled qubits
    2. The referee sends one qubit to Alice (x) and the other to Bob (y)
    3. Alice and Bob measure their qubits (a(x), b(y))
    4. Alice and Bob send the results to the referee
    5. The referee checks the results:
        if a(x) XOR b(y) == xy they win
        else they lose
In quantum version of the game, Alice and Bob can set a strategy to win
"""
# pylint: disable=import-error
