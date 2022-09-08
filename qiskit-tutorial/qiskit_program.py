import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit


def define_circuit():
    circ = QuantumCircuit(3)
    # Add a H gate on qubit 0, putting this qubit in superposition.
    circ.h(0)
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
    # the qubits in a Bell state.
    circ.cx(0, 1)
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 2, putting
    # the qubits in a GHZ state.
    circ.cx(0, 2)

    circ.draw('mpl')


if __name__ == '__main__' :
    define_circuit()
