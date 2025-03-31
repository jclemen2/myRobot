# -*- coding: utf-8 -*-
# Cole Richardson

# Imports
import pybullet_data
import pybullet as p
import time
import numpy
# Import pyrosim
import pyrosim.pyrosim as pyrosim
# Import os
import os
# Import constants and simulation file
import constants as c
from simulation import SIMULATION
import sys

# Extract the argument
directOrGUI = sys.argv[1]
solutionID = int(sys.argv[2])

simulation = SIMULATION(directOrGUI, solutionID)  # Create an instance of the SIMULATION class
simulation.Run()  # Call the Run method to start the simulation

# Import from simulation
simulation.Get_Fitness()  # This will call the Get_Fitness() method


# from simulation import SIMULATION
# import sys
#
# directOrGUI = sys.argv[1] #extract command-line argument to determine mode (GUI or direct)
# solutionID = sys.argv[2] # The unique solution ID
#
# # Create a simulation instance
# simulation = SIMULATION(directOrGUI, solutionID)
# simulation.Run()
# simulation.Get_Fitness()
