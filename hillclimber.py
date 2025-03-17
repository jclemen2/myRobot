from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER: # name of the class
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        print("Parent Weights Before Mutation:\n", self.parent.weights)
        print("Child Weights Before Mutation:\n", self.child.weights)

        self.child.Mutate()  # Perform mutation

        print("Child Weights After Mutation:\n", self.child.weights)

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(f"Parent Fitness: {self.parent.fitness}, Child Fitness: {self.child.fitness}")

