from simulation import SIMULATION
import sys

# Extract the argument
directOrGUI = sys.argv[1]
solutionID = int(sys.argv[2])

simulation = SIMULATION(directOrGUI, solutionID)  # Create an instance of the SIMULATION class
simulation.Run()  # Call the Run method to start the simulation

# Import from simulation
simulation.Get_Fitness()  # This will call the Get_Fitness() method