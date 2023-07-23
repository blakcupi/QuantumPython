from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from numpy import pi

simulator = AerSimulator()

qreg_q = QuantumRegister(8, 'q')
creg_c = ClassicalRegister(5, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[0])
circuit.x(qreg_q[1])
circuit.h(qreg_q[4])

circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2], qreg_q[3], qreg_q[4], qreg_q[5], qreg_q[6], qreg_q[7])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[3])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2], qreg_q[3], qreg_q[4], qreg_q[5], qreg_q[6], qreg_q[7])
circuit.cx(qreg_q[2], qreg_q[5])
circuit.cx(qreg_q[4], qreg_q[5])
circuit.ccx(qreg_q[2], qreg_q[4], qreg_q[6])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2], qreg_q[3], qreg_q[4], qreg_q[5], qreg_q[6], qreg_q[7])
circuit.cx(qreg_q[3], qreg_q[7])
circuit.cx(qreg_q[6], qreg_q[7])
circuit.ccx(qreg_q[3], qreg_q[6], qreg_q[7])
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2], qreg_q[3], qreg_q[4], qreg_q[5], qreg_q[6], qreg_q[7])

circuit.measure(qreg_q[5], creg_c[0])
circuit.measure(qreg_q[7], creg_c[1])

compiled_circuit = transpile(circuit, simulator)
print(compiled_circuit)
print('\n')
print('\n')

job = simulator.run(compiled_circuit, shots=1000)
print(job)
print('\n')
print('\n')
result = job.result()
print(result)
print('\n')
print('\n')

counts = result.get_counts(compiled_circuit)
print(counts)
print('\n')
print('\n')

circuit.draw("mpl")
plot_histogram(counts)