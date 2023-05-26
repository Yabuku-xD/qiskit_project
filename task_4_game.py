#Question 4
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute

# Function to define and run the quantum game
def play_quantum_game():
    # Create a quantum circuit with 1 qubit and 1 classical bit
    qr = QuantumRegister(1)
    cr = ClassicalRegister(1)
    qc = QuantumCircuit(qr, cr)
    
    # Prepare the initial state |0>
    qc.initialize([1, 0], qr[0])
    
    # Apply a Hadamard gate
    qc.h(qr[0])
    
    # Measure the qubit
    qc.measure(qr[0], cr[0])
    
    # Simulate the circuit and obtain the result
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    counts = result.get_counts(qc)
    
    # Check the measurement result and determine the outcome
    outcome = int(list(counts.keys())[0])
    if outcome == 0:
        print("You win!")
    else:
        print("You lose!")
        
# Play the quantum game
play_quantum_game()
