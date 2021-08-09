# qubit number=4
# total number=12
import pyquil
from pyquil.api import local_forest_runtime, QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

conn = QVMConnection()

def make_circuit()-> Program:

    prog = Program() # circuit begin



    prog += H(1)  # number=2
    prog += H(2)  # number=3
    prog += H(3)  # number=4
    prog += Y(3) # number=5
    prog += SWAP(1,0) # number=6
    prog += SWAP(1,0) # number=7
    prog += SWAP(2,0) # number=8
    prog += SWAP(2,0) # number=9
    prog += X(0) # number=10
    prog += X(0) # number=11
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
    writefile = open("../data/startPyquil369.csv","w")
    print(summrise_results(bitstrings),file=writefile)
    writefile.close()

