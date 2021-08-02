# qubit number=2
# total number=37
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(0)  # number=1
    prog += CNOT(0,2) # number=11
    prog += CNOT(0,2) # number=31
    prog += CNOT(0,2) # number=34
    prog += X(2) # number=35
    prog += CNOT(0,2) # number=36
    prog += CNOT(0,2) # number=33
    prog += H(2) # number=25
    prog += CZ(0,2) # number=26
    prog += H(2) # number=27
    prog += H(1) # number=7
    prog += CZ(2,1) # number=8
    prog += RX(-0.3989822670059037,1) # number=30
    prog += H(1) # number=9
    prog += H(1) # number=18
    prog += CZ(2,1) # number=19
    prog += H(1) # number=20
    prog += Y(1) # number=14
    prog += H(1) # number=22
    prog += CZ(2,1) # number=23
    prog += H(1) # number=24
    prog += Z(2) # number=3
    prog += X(1) # number=17
    prog += Y(2) # number=5
    prog += X(2) # number=21

    prog += CNOT(1,0) # number=15
    prog += CNOT(1,0) # number=16
    prog += X(2) # number=28
    prog += X(2) # number=29
    # circuit end

    return prog

def summrise_results(bitstrings) -> dict:
    d = {}
    for l in bitstrings:
        if d.get(l) is None:
            d[l] = 1
        else:
            d[l] = d[l] + 1

    return d

if __name__ == '__main__':
    prog = make_circuit()
    qvm = get_qc('1q-qvm')

    results = qvm.run_and_measure(prog,1024)
    bitstrings = np.vstack([results[i] for i in qvm.qubits()]).T
    bitstrings = [''.join(map(str, l)) for l in bitstrings]
    writefile = open("../data/startPyquil201.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()

