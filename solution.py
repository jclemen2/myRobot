import numpy
import random
import os
import pyrosim.pyrosim as pyrosim
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID

        # Generate a 3-row x 2-column matrix with random values in [0,1]
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        # Scale to [-1, 1]
        self.weights = self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        command = f"python3 simulate.py {directOrGUI} {self.myID} 2>&1 &"
        os.system(command)

        # fitnessFile = open("fitness.txt", "r")
        # self.fitness = float(fitnessFile.read())
        # fitnessFile.close()

        fitnessFileName = f"fitness{str(self.myID)}.txt"

        # Wait for the simulation to finish and the file to be created
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)  # Wait 10ms before checking again

        # Read fitness once file is available
        with open(fitnessFileName, "r") as fitnessFile:
            self.fitness = float(fitnessFile.read())

        print(f"Solution {self.myID} fitness: {self.fitness}")

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        command = f"python3 simulate.py {directOrGUI} {self.myID} &"
        os.system(command)

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = f"fitness{str(self.myID)}.txt"

        # Wait for the simulation to finish and the file to be created
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)  # Wait 10ms before checking again

        # Read fitness once file is available
        with open(fitnessFileName, "r") as fitnessFile:
            self.fitness = float(fitnessFile.read())

        #print(f"Solution {self.myID} fitness: {self.fitness}")

        # Delete fitness file to keep directory clean
        os.system(f"rm {fitnessFileName}")

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)

        old_value = self.weights[randomRow, randomColumn]  # store the old weight
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1  # assign new random value

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID

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

        # Create Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        # Create back leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0],
                          size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Lower_BackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5],
                          size=[0.2, 0.2, 1])

        # Create front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0],
                          size=[0.2, 1, 0.2])

        # Create left leg
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")  # Rotates forward-backward
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        # Create right leg
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")  # Rotates forward-backward
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])


        # Finalize the URDF file
        pyrosim.End()

    def Generate_Brain(self):
        brainFileName = f"brain{self.myID}.nndf"  # Unique filename for each solution
        # Start generating the URDF file
        pyrosim.Start_NeuralNetwork(brainFileName)

        # Name neurons with numbers
        # Create sensor neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LowerBackLeg")

        # Create motor neurons
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Lower_BackLeg")

        # # Create synapses
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3,
        #                      weight=1.0)  # this connects neuron 1 to neuron 3 with a synaptic with weight 1.0.
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3,
        #                      weight=1.0)  # this connects neuron 2 to neuron 3 with a synaptic with weight 1.0.
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4,
        #                      weight=0.5)  # this connects neuron 1 to neuron 4 with a synaptic with weight 1.0.
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4,
        #                      weight=0.0)  # this connects neuron 2 to neuron 4 with a synaptic with weight 1.0.

        # Create synapses using nested loops
        for currentRow in range(c.numSensorNeurons):  # Iterate over sensor neurons 0, 1, 2, 4
            for currentColumn in range(c.numMotorNeurons):  # Iterate over motor neurons 3, 4, 5, 6
                random_weight = random.uniform(-1, 1)  # Generate a random weight between -1 and 1
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        #print(f"ID {self.myID} weights:\n{self.weights}")

        # Finalize the URDF file
        pyrosim.End()
