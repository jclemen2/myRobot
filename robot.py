from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

import pybullet as p
import pyrosim.pyrosim as pyrosim
import os

class ROBOT: # name of the class
    def __init__(self, solutionID):  # Constructor
        self.robotId = p.loadURDF("body.urdf")

        brainFileName = f"brain{solutionID}.nndf"
        self.nn = NEURAL_NETWORK(brainFileName)

        pyrosim.Prepare_To_Simulate(self.robotId)

        # Prepare sensors and motors
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        # Delete the brain file after reading it
        os.system(f"rm {brainFileName}")

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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName): # Only prints the motor neurons
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self, desiredAngle)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()


    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        # with open("fitness.txt", "w") as f:  # "w" mode overwrites the file, we want to write the fitness to a txt file
        #     f.write(str(xCoordinateOfLinkZero))  # Write as string

        f = open("fitness.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()


