"""
Superdense coding in Cirq
Alice and Bob share a Bell pair, and Alice wants to send Bob a message.
Alice can send two classical bits of information to Bob by sending only
one qubit.
Alice and Bob share an entangled pair of qubits.
Alice performs some operations on her half of the entangled pair.
Alice sends the results of her operations to Bob using classical
communication.
Bob uses the classical communication to perform operations on his half
of the entangled pair.
Bob now has the message that Alice wanted to send him.
The superdense coding protocol is a way to send two classical bits of
information using only one qubit.
The superdense coding protocol consists of the following steps:
    1- Alice preppares an EPR pair., which is a Bell pair of qubits.
    2- For this, Alice applies a Hadamard gate to her qubit, and then a
        CNOT gate with her qubit as the control and Bob's qubit as the
        target.
    3- Alice sends her qubit to Bob.
    4- Alice which of the of the four possible states she wants to send to
        Bob. The four possible states are |00⟩, |01⟩, |10⟩, and |11⟩.
    5- Alice sends the results to Bob.
    6- Bob uses the results from Alice to perform operations on his qubit.
    7- Bob applies the Hadamard and then CNOT gates to his qubit.
    8- Bob measures his qubit.
    9- Bob now has two classical bits of information.
"""
