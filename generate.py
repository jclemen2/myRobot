# Import pyrosim
import pyrosim.pyrosim as pyrosim
import random

def Create_World():
    # Tell pyrosim the name of the file where the world will be stored
    pyrosim.Start_SDF("world.sdf")

    # Store box position and parameters
    pyrosim.Send_Cube(name="Box", pos=[-10,0,0.5], size=[1,1,1])

    # End the SDF generation
    pyrosim.End()


def Generate_Body():
    # Start creating the robot description in URDF format
    pyrosim.Start_URDF("body.urdf")

    # Block dimensions
    length = 1
    width = 1
    height = 1

    # Create the root cube (Torso)
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])

    # Create Joint between Torso and BackLeg
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.5, 0, 1])

    # Create BackLeg
    pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

    # Create joint between Torso and FrontLeg
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[-0.5, 0, 1])

    # Create FrontLeg
    pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])

    # End the URDF generation
    pyrosim.End()

    # CAN ADD IN WORLD.SDF IF NEED TO ADD THE EXTRA BOX BUT IT IS BUILT INTO WORLD FILE ALREADY



def Generate_Brain():
    # Start creating the brain neural network
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    # Generate a synapse
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1)
    # Generate second synapse
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=1)

    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=0.5)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=0.0)

    # Generate synapses using nested loops
    for i in range(3):  # Sensor neurons (0, 1, 2)
        for j in range(3, 5):  # Motor neurons (3, 4)
            weight = random.uniform(-1, 1)  # Generate a random weight in [-1,1]
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=weight)

    # End the URDF generation
    pyrosim.End()