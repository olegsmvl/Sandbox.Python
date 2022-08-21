# https://proglib.io/p/pishem-neyroset-na-python-s-nulya-2020-10-07

import numpy as np
from neuron import Neuron

class NeuralNetwork():
    def __init__(self):
        weights = np.array([0,1])
        bias = 0

        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)


def test1():
    weights = np.array([0, 1])
    bias = 4

    n = Neuron(weights, bias)

    inputs = np.array([2, 3])
    print(n.feedforward(inputs))

def test2():


def main():
    test2()


if __name__ == "__main__":
    main()