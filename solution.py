import numpy
import random
import os
import pyrosim.pyrosim as pyrosim

class SOLUTION:
    def __init__(self):
        # Generate a 3-row x 2-column matrix with random values in [0,1]
        self.weights = numpy.random.rand(3, 2)
        # Scale to [-1, 1]
        self.weights = self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        os.system(f"python3 simulate.py {directOrGUI}")

        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0,1)

        old_value = self.weights[randomRow, randomColumn]  # store the old weight
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1  # assign new random value

    def Create_World(self):
        # Start generating the SDF file
        pyrosim.Start_SDF("world.sdf")

        # set variables size and position
        length = 1
        width = 1
        height = 1
        x = 4
        y = 2
        z = 0.5

        # Create Object
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        # Finalize the SDF file
        pyrosim.End()

    def Generate_Body(self):
        # Start generating the URDF file
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5],
                          size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5],
                          size=[1, 1, 1])

        # Finalize the URDF file
        pyrosim.End()

    def Generate_Brain(self):
        # Start generating the URDF file
        pyrosim.Start_NeuralNetwork("brain.nndf")

        # Name neurons with numbers
        # Create sensor neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        # Create motor neurons
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # Create synapses
        pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3,
                             weight=1.0)  # this connects neuron 1 to neuron 3 with a synaptic with weight 1.0.
        pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3,
                             weight=1.0)  # this connects neuron 2 to neuron 3 with a synaptic with weight 1.0.
        pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4,
                             weight=0.5)  # this connects neuron 1 to neuron 4 with a synaptic with weight 1.0.
        pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4,
                             weight=0.0)  # this connects neuron 2 to neuron 4 with a synaptic with weight 1.0.

        # Create synapses using nested loops
        for currentRow in range(3):  # Iterate over sensor neurons 0, 1, 2
            for currentColumn in range(2):  # Iterate over motor neurons 3, 4
                random_weight = random.uniform(-1, 1)  # Generate a random weight between -1 and 1
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3., weight=self.weights[currentRow][currentColumn])

        # Finalize the URDF file
        pyrosim.End()