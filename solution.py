import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(4, 8)
        self.weights = self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        command = f"python simulate.py {directOrGUI} {self.myID} 2>&1 &"
        os.system(command)

        fitnessFileName = f"fitness{str(self.myID)}.txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        with open(fitnessFileName, "r") as fitnessFile:
            self.fitness = float(fitnessFile.read())

        with open("fitness_log.txt", "a") as log:
            log.write(f"ID: {self.myID}, Fitness: {self.fitness}\n")

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        command = f"python simulate.py {directOrGUI} {self.myID} 2>&1 &"
        os.system(command)

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = f"fitness{str(self.myID)}.txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        with open(fitnessFileName, "r") as fitnessFile:
            self.fitness = float(fitnessFile.read())

        os.system(f"rm {fitnessFileName}")

    def Mutate(self):
        noise_strength = 0.95  # adjust if needed
        noise = numpy.random.normal(loc=0.0, scale=noise_strength, size=self.weights.shape)
        self.weights += noise
        self.weights = numpy.clip(self.weights, -1, 1)

        # randomRow = random.randint(0, 3)
        # randomColumn = random.randint(0, 7)
        # self.weights[randomRow, randomColumn] = random.uniform(-1,1) * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[4, 2, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body1.urdf")
        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0.0, 0.0, 1.0], size=[1, 1, 1])

        # Front leg
        # Upper leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        # Lower leg
        pyrosim.Send_Joint(name="FrontLeg_Lower", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")  # Rotates forward-backward
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # Back Leg
        # Upper
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="-1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        # Lower
        pyrosim.Send_Joint(name="BackLeg_Lower", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="-1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # Left Leg
        # Upper
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        # Lower
        pyrosim.Send_Joint(name="LeftLeg_Lower", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # Right leg
        # Upper
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 -1 0")  # Rotates forward-backward
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        # Lower
        pyrosim.Send_Joint(name="RightLeg_Lower", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 -1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        # Finalize the URDF file
        pyrosim.End()

    def Generate_Brain(self):
        brainFileName = f"brain{self.myID}.nndf"
        pyrosim.Start_NeuralNetwork(brainFileName)

        for i, link in enumerate(["FrontLowerLeg", "BackLowerLeg", "LeftLowerLeg", "RightLowerLeg"]):
            pyrosim.Send_Sensor_Neuron(name=i, linkName=link)

        motorJoints = ["Torso_BackLeg", "Torso_FrontLeg", "Torso_LeftLeg", "Torso_RightLeg",
                       "FrontLeg_Lower", "BackLeg_Lower", "LeftLeg_Lower", "RightLeg_Lower"]

        for i, joint in enumerate(motorJoints):
            pyrosim.Send_Motor_Neuron(name=i + 4, jointName=joint)

        for r in range(4):
            for c in range(8):
                pyrosim.Send_Synapse(sourceNeuronName=r, targetNeuronName=c + 4, weight=self.weights[r][c])

        pyrosim.End()