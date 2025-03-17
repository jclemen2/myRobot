from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER: # name of the class
    def __init__(self):
        self.parents = {}

        # Create multiple parent solutions
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION()  # Assign a new random solution

    def Evolve(self):
        # Evaluate each parent one after another in GUI mode
        for key in self.parents:
            print(f"Evaluating Parent {key} in GUI mode...")
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
        print("Parent Weights Before Mutation:\n", self.parent.weights)
        print("Child Weights Before Mutation:\n", self.child.weights)

        self.child.Mutate()  # Perform mutation

        print("Child Weights After Mutation:\n", self.child.weights)

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(f"Parent Fitness: {self.parent.fitness}, Child Fitness: {self.child.fitness}")

    def Show_Best(self):
        pass
        # print("\nRe-evaluating the best solution with GUI...")
        # self.parent.Evaluate("GUI")  # Re-evaluate final parent with GUI

