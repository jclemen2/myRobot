from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1] #extract command-line argument to determine mode (GUI or direct)
solutionID = sys.argv[2] # The unique solution ID

# Create a simulation instance
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()


