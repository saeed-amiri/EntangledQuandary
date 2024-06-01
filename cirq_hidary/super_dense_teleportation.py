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
# pylint: disable=import-error


import cirq


# Helper function for visulization output
def bit_string(bits):
    """visulaization of the ouput"""
    return ''.join('1' if e else '0' for e in bits)


# Create two quantum and classical regesters
qreg = [cirq.LineQubit(x) for x in range(2)]
circ = cirq.Circuit()

# Dictionary of operations for each message
messages = {'00': [],
            '01': [cirq.X(qreg[0])],
            '10': [cirq.Z(qreg[0])],
            '11': [cirq.X(qreg[0]), cirq.Z(qreg[0])]}

# Alice creates a Bell pair
circ.append(cirq.H(qreg[0]))
circ.append(cirq.CNOT(qreg[0], qreg[1]))

# Alice picks a message to send
MESG = '01'
print(f"Alice's message = {MESG}")

# Alice encodes her message with the appropiate quantum operations
circ.append(messages[MESG])

print(f'Circuit is:\n {circ}')
