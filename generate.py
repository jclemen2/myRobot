from ctypes import c_int32
import pyrosim.pyrosim as pyrosim

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

# def Create_Robot():
#     # Start generating the URDF file
#     pyrosim.Start_URDF("body.urdf")
#
#     # Set size and position for Torso
#     length_Torso = 1
#     width_Torso = 1
#     height_Torso = 1
#     x_Torso = 1.5
#     y_Torso = 0
#     z_Torso = 1.5
#
#     # Set size and position for BackLeg
#     length_BackLeg = 1
#     width_BackLeg = 1
#     height_BackLeg = 1
#     x_BackLeg = -0.5
#     y_BackLeg = 0
#     z_BackLeg = -0.5
#
#     # Set size and position for FrontLeg
#     length_FrontLeg = 1
#     width_FrontLeg = 1
#     height_FrontLeg = 1
#     x_FrontLeg = 0.5
#     y_FrontLeg = 0
#     z_FrontLeg = -0.5
#
#     pyrosim.Send_Cube(name="Torso", pos=[x_Torso, y_Torso, z_Torso], size=[length_Torso, width_Torso, height_Torso])
#     pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
#     pyrosim.Send_Cube(name="BackLeg", pos=[x_BackLeg, y_BackLeg, z_BackLeg], size=[length_BackLeg, width_BackLeg, height_BackLeg])
#     pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
#     pyrosim.Send_Cube(name="FrontLeg", pos=[x_FrontLeg, y_FrontLeg, z_FrontLeg], size=[length_FrontLeg, width_FrontLeg, height_FrontLeg])
#
#     # Finalize the URDF file
#     pyrosim.End()

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
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    # Finalize the URDF file
    pyrosim.End()


Create_World()
#Create_Robot()
Generate_Body()
Generate_Brain()