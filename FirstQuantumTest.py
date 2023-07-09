from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Use Aer's AerSimulator...양자 시뮬레이터 생성
simulator = AerSimulator()

# Create a Quantum Circuit acting on the q register...양자 회로에 사용될 게이트 라이브러리 생성
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0....중첩상태 만들기
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1...얽힘상태 만들기
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits...측정
circuit.measure([0, 1], [0, 1])

# Compile the circuit for the support instruction set (basis_gates)
# and topology (coupling_map) of the backend
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the aer simulator
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print("\nTotal count for 00 and 11 are:", counts)

# Draw the circuit....jupyter notebook에서 확인 가능
circuit.draw("mpl")

# Plot a histogram....jupyter notebook에서 확인 가능
plot_histogram(counts)