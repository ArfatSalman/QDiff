# qubit number=4
# total number=58
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin

    prog += H(0) # number=1

    prog += H(1) # number=2
    prog += H(2) # number=3
    prog += H(3)  # number=4
    prog += H(0) # number=7
    prog += Y(2) # number=12
    prog += CZ(1,0) # number=8
    prog += H(1) # number=39
    prog += CZ(0,1) # number=40
    prog += H(1) # number=41
    prog += H(1) # number=22
    prog += H(1) # number=51
    prog += CZ(0,1) # number=23
    prog += H(1) # number=24
    prog += H(1) # number=42
    prog += CZ(0,1) # number=43
    prog += H(1) # number=44
    prog += X(1) # number=32
    prog += H(1) # number=55
    prog += CZ(0,1) # number=56
    prog += H(1) # number=57
    prog += Y(3) # number=37
    prog += H(1) # number=28
    prog += CZ(0,1) # number=29
    prog += H(1) # number=30
    prog += H(1) # number=25
    prog += CZ(0,1) # number=26
    prog += H(1) # number=27
    prog += H(0) # number=9
    prog += CNOT(1,0) # number=45
    prog += H(0) # number=52
    prog += CZ(1,0) # number=53
    prog += H(0) # number=54
    prog += Z(1) # number=49
    prog += CNOT(1,0) # number=50
    prog += CNOT(1,0) # number=47
    prog += Y(1) # number=13
    prog += CNOT(1,0) # number=6
    prog += Y(2) # number=36
    prog += SWAP(3,0) # number=17
    prog += Y(3) # number=38
    prog += SWAP(3,0) # number=18
    prog += CNOT(2,0) # number=34
    prog += CNOT(2,0) # number=35
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
    qvm = get_qc('4q-qvm')

    results = qvm.run_and_measure(prog,1024)
    bitstrings = np.vstack([results[i] for i in qvm.qubits()]).T
    bitstrings = [''.join(map(str, l)) for l in bitstrings]
    writefile = open("../data/startPyquil479.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()

