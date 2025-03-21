from solution import SOLUTION

import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # Clean up leftover brain and fitness files
        os.system("rm brain*.txt")
        os.system("rm fitness*.txt")

        self.nextAvailableID = 0
        self.parents = {} # generates an empty dictionary
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}  # Create an empty dictionary to store children

        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])  # Copy parent
            self.children[key].Set_ID(self.nextAvailableID)  # Assign new unique ID
            self.nextAvailableID += 1  # Increment for the next one

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        # if self.child.fitness < self.parent.fitness:
        #     self.parent = self.child  # if the child is better replace the parent value with the child value

        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print()  # Print an empty line at the beginning
        for key in self.parents:
            print(f"Parent Fitness: {self.parents[key].fitness:.4f} | Child Fitness: {self.children[key].fitness:.4f}")
        print()  # Print an empty line at the end

    def Show_Best(self):
        # print("\nRe-evaluating the best solution with GUI...")
        # self.parent.Evaluate("GUI")  # show the best evolved solution

        bestParent = None
        bestFitness = float('inf')

        for key in self.parents:
            if self.parents[key].fitness < bestFitness:
                bestFitness = self.parents[key].fitness
                bestParent = self.parents[key]

        print(f"\nBest Fitness: {bestFitness} (Showing best parent in GUI mode...)")
        bestParent.Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT")

        # Wait for all simulations to complete and read fitness
        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()
            # print(f"Parent {key} fitness: {solutions[key].fitness}")
            # print("Fitness:", solutions[key].fitness)  # Optional: debugging

