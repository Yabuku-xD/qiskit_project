#Question 3
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute

def build_problem_oracle(pattern):
    # Determine the number of qubits needed based on the pattern length
    num_qubits = len(pattern)
    
    # Create a quantum circuit with the required number of qubits and a classical register
    qr = QuantumRegister(num_qubits)
    cr = ClassicalRegister(num_qubits)
    qc = QuantumCircuit(qr, cr)
    
    # Apply the X gate to the qubits corresponding to '1' in the pattern
    for i in range(num_qubits):
        if pattern[i] == '1':
            qc.x(qr[i])
    
    # Apply the Z gate to all qubits
    qc.h(qr)
    qc.z(qr)
    qc.h(qr)
    
    # Measure all qubits
    qc.measure(qr, cr)
    
    return qc

# Test the problem oracle with a sample pattern
pattern = '110'
oracle = build_problem_oracle(pattern)
print(oracle)

# Assess the size of the circuit with respect to the problem size
pattern_sizes = [2, 4, 6, 8, 10]  # Example pattern sizes
circuit_sizes = []

for size in pattern_sizes:
    pattern = '1' * size  # Create a pattern of all '1's with the specified size
    oracle = build_problem_oracle(pattern)
    circuit_sizes.append(oracle.size())

print(f"Pattern Sizes: {pattern_sizes}")
print(f"Circuit Sizes: {circuit_sizes}")

Output:
      ┌───┐┌───┐┌───┐┌───┐┌─┐   
q0_0: ┤ X ├┤ H ├┤ Z ├┤ H ├┤M├───
      ├───┤├───┤├───┤├───┤└╥┘┌─┐
q0_1: ┤ X ├┤ H ├┤ Z ├┤ H ├─╫─┤M├
      ├───┤├───┤├───┤└┬─┬┘ ║ └╥┘
q0_2: ┤ H ├┤ Z ├┤ H ├─┤M├──╫──╫─
      └───┘└───┘└───┘ └╥┘  ║  ║ 
c0: 3/═════════════════╩═══╩══╩═
                       2   0  1 
Pattern Sizes: [2, 4, 6, 8, 10]
Circuit Sizes: [10, 20, 30, 40, 50]
