import numpy

class SOLUTION:
    def __init__(self):
        # Generate a 3-row x 2-column matrix with random values in [0,1]
        self.weights = numpy.random.rand(3, 2)
        # Scale to [-1, 1]
        self.weights = self.weights * 2 - 1
