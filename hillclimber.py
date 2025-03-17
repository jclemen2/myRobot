from solution import SOLUTION

class HILL_CLIMBER: # name of the class
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()