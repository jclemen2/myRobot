import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
from math import pi
import random
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("box.sdf")
pyrosim.Prepare_To_Simulate(robotId)

# Create array to store sensor values
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

for i in range (1000):
    p.stepSimulation()

    # Get sensor values
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Simulate motor
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId, # What robot should the motor be attached to
        jointName="Torso_BackLeg",  # What joint should the motor be attached to
        controlMode=p.POSITION_CONTROL,  # How the motor will attempt to control the motion of the joint
        targetPosition=-pi/4.0,  # Desired position
        maxForce=500)  # Total torque

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,  # What robot should the motor be attached to
        jointName="Torso_FrontLeg",  # What joint should the motor be attached to
        controlMode=p.POSITION_CONTROL,  # How the motor will attempt to control the motion of the joint
        targetPosition=pi/4.0,  # Desired position
        maxForce=500)  # Total torque

    # Slow the simulation
    time.sleep(1/100)

# Define the full path to the data directory
data_dir = "/Users/justineclement/PycharmProjects/myRobot/data"

# Define the full path for the file
file_path_backLeg = os.path.join(data_dir, "backLegSensorValues.npy")
file_path_frontLeg = os.path.join(data_dir, "frontLegSensorValues.npy")

# Save the array to the file
numpy.save(file_path_backLeg, backLegSensorValues)
numpy.save(file_path_frontLeg, frontLegSensorValues)

p.disconnect()

