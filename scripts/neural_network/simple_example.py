# https://proglib.io/p/pishem-neyroset-na-python-s-nulya-2020-10-07

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

def main():
    var = np.zeros([3,3])
    print(var)


if __name__ == "__main__":
    main()