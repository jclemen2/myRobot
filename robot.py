from sensor import SENSOR
from motor import MOTOR

import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT: # name of the class
    def __init__(self):  # Constructor
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Prepare sensors and motors
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        # Creates a sensor for each link in the robot
        self.sensors = {}  # Initialize sensors dictionary

        # Loop through all link names in the robot
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)  # Create sensor instance

    def Prepare_To_Act(self):
        # Creates a motor for each joint in the robot
        self.motors = {}  # Initialize sensors dictionary

        # Loop through all joint names in the robot
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)  # Create motor instance

    def Sense(self, t):
        # Reads sensor values for each link at time step t.
        for sensor in self.sensors.values():
            sensor.Get_Value(t)  # Pass t to the sensor's Get_Value()

    def Act(self, t):
        # Applies motor commands at time step t.
        for motor in self.motors.values():
            motor.Set_Value(self, t)  # Pass robot instance and time step t

    def Think(self):
        self.nn.Update()
        self.nn.Print()