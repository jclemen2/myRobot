from solution import SOLUTION

import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        pass
        self.parents = {} # generates an empty dictionary
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION()

    def Evolve(self):
        for key in self.parents:
            self.parents[key].Evaluate("GUI")

        # print("Evaluating initial random solution...")
        # self.parent.Evaluate("GUI")  # Show the first solution visually
        #
        # print("\nStarting evolution process...\n")
        # self.parent.Evaluate("DIRECT")  # Evaluate initial solution in DIRECT mode
        #
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child  # if the child is better replace the parent value with the child value

    def Print(self):
        print(f"Parent Fitness: {self.parent.fitness}, Child Fitness: {self.child.fitness}")

    def Show_Best(self):
        pass
        # print("\nRe-evaluating the best solution with GUI...")
        # self.parent.Evaluate("GUI")  # show the best evolved solution