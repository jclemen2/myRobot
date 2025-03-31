from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import time

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        #GB()

        # Loads the robot body and prepares it for simulation.
        self.robotId = p.loadURDF("body1.urdf")  # Load robot URDF

        # Prepare robot for simulation
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Prepare sensors for all links
        self.Prepare_To_Sense()

        # Prepare motors
        self.Prepare_To_Act()

        brain_filename = f"brain{solutionID}.nndf"
        self.nn = NEURAL_NETWORK(brain_filename)

        # Delete the brain file after it has been read
        if os.name == "nt":  # Windows
            os.system(f"del {brain_filename}")
        else:  # Mac/Linux
            os.system(f"rm {brain_filename}")

    def Prepare_To_Sense(self):
        """Initialize the dictionary for sensors."""
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)   # Create SENSOR instance

    def Prepare_To_Act(self):
        '''Initialize the dictionary for motors'''
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)  # Create MOTOR instance

    def Sense(self, t):
        for sensor in self.sensors.values():  # Iterate over all SENSOR instances
            sensor.Get_Value(t)  # Call Get_Value() on each sensor to update its values

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                # Extract the value (desired angle) for this motor neuron
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange

                # Ensure the jointName is a decoded string, in case it's a byte string
                decoded_joint_name = jointName.decode("utf-8") if isinstance(jointName, bytes) else jointName

                self.motors[decoded_joint_name].Set_Value(self, desiredAngle)
                #jointName= jointName.decode("utf-8")

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        # Final Project Code
        # List of lower leg link names to track
        lower_leg_links = [
            "FrontLowerLeg",
            "BackLowerLeg",
            "LeftLowerLeg",
            "RightLowerLeg"
        ]

        z_values = []

        for link_name in lower_leg_links:
            try:
                link_index = pyrosim.linkNamesToIndices[link_name]
                link_state = p.getLinkState(self.robotId, link_index)
                z = link_state[0][2]  # Extract the z-coordinate
                z_values.append(z)
            except KeyError:
                print(f"Warning: Link {link_name} not found in simulation.")
                z_values.append(0.0)  # Default to 0.0 if the link isn't found

        # Compute average or max height of lower legs
        fitness = sum(z_values) / len(z_values)

        # Save fitness to file
        tmp_fitness_file = f"tmp{self.solutionID}.txt"
        with open(tmp_fitness_file, "w") as file:
            file.write(str(fitness))

        time.sleep(0.01)
        os.rename(tmp_fitness_file, f"fitness{self.solutionID}.txt")

        # Normal Quadruped Code
        # # Get the state of the first link (link zero)
        # basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        #
        # # Get the state of the first link (link zero)
        # basePosition = basePositionAndOrientation[0]
        #
        # # Extract the x coordinate (first element) from positionOfLinkZero
        # xCoordinateOfLinkZero = basePosition[0]
        #
        # # Write the x coordinate to a file (fitness.txt)
        # tmp_fitness_file = f"tmp{self.solutionID}.txt"
        # with open(tmp_fitness_file, "w") as file:
        #     file.write(str(xCoordinateOfLinkZero))  # Convert to string and write to file
        # time.sleep(0.01)
        #
        # os.rename("tmp" + str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")