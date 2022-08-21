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
    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
        our_o1 = self.o1.feedforward(np.array(out_h1, out_h2))
        return our_o1

def mse_loss(y_true, y_pred):
    return ((y_true - y_pred)** 2).mean()


def test1():
    weights = np.array([0, 1])
    bias = 4

    n = Neuron(weights, bias)

    inputs = np.array([2, 3])
    print(n.feedforward(inputs))

def test2():
    network = NeuralNetwork()
    x = np.array([2,3])
    print(network.feedforward(x))

def main():
    test2()

    y_true = np.array([1, 0, 0, 1])
    y_pred = np.array([0, 0, 0, 0])

    print(mse_loss(y_true, y_pred))


if __name__ == "__main__":
    main()