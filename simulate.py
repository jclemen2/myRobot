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