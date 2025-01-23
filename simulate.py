import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
from math import pi
import random
import time

# Constant
SIMULATION_TIME = 1000

# Variables
amplitude_backLeg = pi/4
frequency_backLeg = 20
phaseOffset_backLeg = 0

amplitude_frontLeg = 0
frequency_frontLeg = 0
phaseOffset_frontLeg = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("box.sdf")
pyrosim.Prepare_To_Simulate(robotId)

# Create array to store sensor values
backLegSensorValues = numpy.zeros(SIMULATION_TIME)
frontLegSensorValues = numpy.zeros(SIMULATION_TIME)

# Create array to store sinusoidal motor values
num_iterations = SIMULATION_TIME
time_values = numpy.linspace(0, 2 * pi, num_iterations)
motorTargetAngles_backLeg = amplitude_backLeg * numpy.sin(frequency_backLeg * time_values + phaseOffset_backLeg)
motorTargetAngles_frontLeg = amplitude_frontLeg * numpy.sin(frequency_frontLeg * time_values + phaseOffset_frontLeg)

for i in range (SIMULATION_TIME):
    p.stepSimulation()

    # Get sensor values
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Simulate motor
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId, # What robot should the motor be attached to
        jointName="Torso_BackLeg",  # What joint should the motor be attached to
        controlMode=p.POSITION_CONTROL,  # How the motor will attempt to control the motion of the joint
        targetPosition=motorTargetAngles_backLeg[i],  # Desired position
        maxForce=50)  # Total torque

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,  # What robot should the motor be attached to
        jointName="Torso_FrontLeg",  # What joint should the motor be attached to
        controlMode=p.POSITION_CONTROL,  # How the motor will attempt to control the motion of the joint
        targetPosition=motorTargetAngles_frontLeg[i],  # Desired position
        maxForce=50)  # Total torque

    # Slow the simulation
    time.sleep(1/240)

# Define the full path to the data directory
data_dir = "/Users/justineclement/PycharmProjects/myRobot/data"

# Define the full path for the file
file_path_backLeg = os.path.join(data_dir, "backLegSensorValues.npy")
file_path_frontLeg = os.path.join(data_dir, "frontLegSensorValues.npy")
file_path_motorTargetAngles_backLeg = os.path.join(data_dir, "motorTargetAngles_backLeg.npy")
file_path_motorTargetAngles_frontLeg = os.path.join(data_dir, "motorTargetAngles_frontLeg.npy")

# Save the array to the file
numpy.save(file_path_backLeg, backLegSensorValues)
numpy.save(file_path_frontLeg, frontLegSensorValues)
numpy.save(file_path_motorTargetAngles_backLeg, motorTargetAngles_backLeg)
numpy.save(file_path_motorTargetAngles_frontLeg, motorTargetAngles_frontLeg)

p.disconnect()

