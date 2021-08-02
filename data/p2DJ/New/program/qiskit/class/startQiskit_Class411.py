# qubit number=1
# total number=22
import cirq
import qiskit

from qiskit import IBMQ
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import BasicAer, execute, transpile
from pprint import pprint
from qiskit.test.mock import FakeVigo
from math import log2,floor, sqrt, pi
import numpy as np
import networkx as nx

def build_oracle(n: int) -> QuantumCircuit:
    # implement the oracle O_f^\pm
    # NOTE: use U1 gate (P gate) with \lambda = 180 ==> CZ gate
    # or multi_control_Z_gate (issue #127)

    controls = QuantumRegister(n, "ofc")
    oracle = QuantumCircuit(controls, name="Zf")

    for i in range(2 ** n):
        rep = np.binary_repr(i, n)
        if f(rep) == "1":
            for j in range(n):
                if rep[j] == "0":
                    oracle.x(controls[j])

            # oracle.h(controls[n])
            if n >= 2:
                oracle.mcu1(pi, controls[1:], controls[0])

            for j in range(n):
                if rep[j] == "0":
                    oracle.x(controls[j])
            # oracle.barrier()

    return oracle


def make_circuit(n:int) -> QuantumCircuit:
    # circuit begin
    input_qubit = QuantumRegister(n,"qc")
    classical = ClassicalRegister(n, "qm")
    prog = QuantumCircuit(input_qubit, classical)
    prog.x(input_qubit[0]) # number=1
    prog.x(input_qubit[0]) # number=6
    prog.h(input_qubit[0]) # number=2


    prog.y(input_qubit[0]) # number=3
    prog.h(input_qubit[0]) # number=7
    prog.rx(1.7844246272390027,input_qubit[0]) # number=17
    prog.h(input_qubit[0]) # number=15
    prog.rx(0.634601716025138,input_qubit[0]) # number=5
    prog.y(input_qubit[0]) # number=4
    prog.x(input_qubit[0]) # number=8
    prog.x(input_qubit[0]) # number=9
    prog.y(input_qubit[0]) # number=14
    prog.h(input_qubit[0]) # number=16
    prog.y(input_qubit[0]) # number=10
    prog.x(input_qubit[0]) # number=19
    prog.y(input_qubit[0]) # number=11
    prog.y(input_qubit[0]) # number=12
    prog.y(input_qubit[0]) # number=13
    prog.z(input_qubit[0]) # number=18
    prog.y(input_qubit[0]) # number=20
    prog.y(input_qubit[0]) # number=21
    # circuit end



    return prog




if __name__ == '__main__':

    prog = make_circuit(1)
    backend = BasicAer.get_backend('statevector_simulator')
    sample_shot =1974

    info = execute(prog, backend=backend).result().get_statevector()
    qubits = round(log2(len(info)))
    info = {
        np.binary_repr(i, qubits): round((info[i]*(info[i].conjugate())).real,3)
        for i in range(2 ** qubits)
    }

    backend = FakeVigo()
    circuit1 = transpile(prog,backend)

    writefile = open("../data/startQiskit_Class411.csv","w")
    print(info,file=writefile)
    print("results end", file=writefile)
    print(circuit1.depth(),file=writefile)
    print(circuit1,file=writefile)
    writefile.close()
