# qubit number=5
# total number=8
import cirq
import qiskit

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import BasicAer, execute
from pprint import pprint
from math import log2
import numpy as np

def bitwise_xor(s: str, t: str) -> str:
    length = len(s)
    res = []
    for i in range(length):
        res.append(str(int(s[i]) ^ int(t[i])))
    return ''.join(res[::-1])


def bitwise_dot(s: str, t: str) -> str:
    length = len(s)
    res = 0
    for i in range(length):
        res += int(s[i]) * int(t[i])
    return str(res % 2)

def build_oracle(n: int, f) -> QuantumCircuit:
    # implement the oracle O_f
    # NOTE: use multi_control_toffoli_gate ('noancilla' mode)
    # https://qiskit.org/documentation/_modules/qiskit/aqua/circuits/gates/multi_control_toffoli_gate.html
    # https://quantumcomputing.stackexchange.com/questions/3943/how-do-you-implement-the-toffoli-gate-using-only-single-qubit-and-cnot-gates
    # https://quantumcomputing.stackexchange.com/questions/2177/how-can-i-implement-an-n-bit-toffoli-gate
    controls = QuantumRegister(n, "ofc")
    target = QuantumRegister(1, "oft")
    oracle = QuantumCircuit(controls, target, name="Of")
    for i in range(2 ** n):
        rep = np.binary_repr(i, n)
        if f(rep) == "1":
            for j in range(n):
                if rep[j] == "0":
                    oracle.x(controls[j])
            oracle.mct(controls, target[0], None, mode='noancilla')
            for j in range(n):
                if rep[j] == "0":
                    oracle.x(controls[j])
            # oracle.barrier()
    return oracle

def make_circuit(n:int,f) -> QuantumCircuit:
    # circuit begin
    input_qubit = QuantumRegister(n,"qc")
    classical = ClassicalRegister(n, "qm")
    prog = QuantumCircuit(input_qubit, classical)
    prog.x(input_qubit[4]) # number=1
    prog.h(input_qubit[1]) # number=4
    prog.h(input_qubit[2]) # number=5
    prog.h(input_qubit[3]) # number=6
    prog.h(input_qubit[4]) # number=7
    prog.h(input_qubit[0]) # number=3

    oracle = build_oracle(n-1, f)
    prog.append(oracle.to_gate(),[input_qubit[i] for i in range(n-1)]+[input_qubit[n-1]])
    prog.h(input_qubit[1])  # number=8
    prog.h(input_qubit[2])  # number=9
    prog.h(input_qubit[3])  # number=10
    prog.h(input_qubit[4])  # number=11
    prog.h(input_qubit[0])  # number=2

    # circuit end

    for i in range(n):
        prog.measure(input_qubit[i], classical[i])


    return prog



if __name__ == '__main__':

    a = "1111"
    b = "0"
    f = lambda rep: bitwise_xor(bitwise_dot(a, rep), b)
    prog = make_circuit(5,f)
    backend = BasicAer.get_backend('qasm_simulator')

    info = execute(prog, backend=backend, shots=1024).result().get_counts()

    print(info)
    writefile = open("../../data/startQiskit0.csv","w")
    pprint(info,writefile)
    writefile.close()