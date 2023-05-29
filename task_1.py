#Question 1
from qiskit import QuantumCircuit

def build_oracle(string):
    # Determine the number of qubits needed based on the string length
    num_qubits = len(string)
    
    # Create a quantum circuit with the required number of qubits
    qc = QuantumCircuit(num_qubits)
    
    # Apply the X gate to qubits corresponding to '1' in the string
    for i in range(num_qubits):
        if string[i] == '1':
            qc.x(i)
    
    # Apply the Z gate to the last qubit
    qc.cz(0, num_qubits-1)
    
    # Apply the X gate again to the qubits corresponding to '1' in the string
    for i in range(num_qubits):
        if string[i] == '1':
            qc.x(i)
        return qc

# Test the oracle with a sample string
string = '01101'
oracle = build_oracle(string)
print(oracle)

Output:
q_0: ──────■──────
     ┌───┐ │ ┌───┐
q_1: ┤ X ├─┼─┤ X ├
     ├───┤ │ ├───┤
q_2: ┤ X ├─┼─┤ X ├
     └───┘ │ └───┘
q_3: ──────┼──────
     ┌───┐ │ ┌───┐
q_4: ┤ X ├─■─┤ X ├
     └───┘   └───┘
