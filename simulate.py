from simulation import SIMULATION
import sys

# Extract command-line argument
directOrGUI = sys.argv[1] if len(sys.argv) > 1 else "DIRECT"

# Create a simulation instance
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()

