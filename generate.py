from ctypes import c_int32
import pyrosim.pyrosim as pyrosim
import random

def Create_World():
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

def Generate_Body():
    # Start generating the URDF file
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5],
                      size=[1,1,1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5],
                      size=[1,1,1])

    # Finalize the URDF file
    pyrosim.End()

def Generate_Brain():
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

    # # Create synapses
    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3,
    #                      weight=1.0) # this connects neuron 1 to neuron 3 with a synaptic with weight 1.0.
    # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3,
    #                      weight=1.0)  # this connects neuron 2 to neuron 3 with a synaptic with weight 1.0.
    # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4,
    #                      weight=0.5)  # this connects neuron 1 to neuron 4 with a synaptic with weight 1.0.
    # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4,
    #                      weight=0.0)  # this connects neuron 2 to neuron 4 with a synaptic with weight 1.0.

    # Create synapses using nested loops
    for sensor_neuron in range(3):  # Iterate over sensor neurons 0, 1, 2
        for motor_neuron in range(3, 5):  # Iterate over motor neurons 3, 4
            random_weight = random.uniform(-1,1)  # Generate a random weight between -1 and 1
            pyrosim.Send_Synapse(sourceNeuronName=sensor_neuron, targetNeuronName=motor_neuron, weight=random_weight)

    # Finalize the URDF file
    pyrosim.End()


Create_World()
#Create_Robot()
Generate_Body()
Generate_Brain()