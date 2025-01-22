from ctypes import c_int32
import pyrosim.pyrosim as pyrosim

# Start generating the SDF file
pyrosim.Start_SDF("box.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

def Create_World():
    # Start generating the SDF file
    pyrosim.Start_SDF("box.sdf")

    # set variables size and position
    length = 1
    width = 1
    height = 1
    x = 0
    y = 0
    z = 0.5

    # Create Object
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

    # Finalize the SDF file
    pyrosim.End()

def Create_Robot():
    # Start generating the URDF file
    pyrosim.Start_URDF("body.urdf")

    # set variables size and position
    length = 1
    width = 1
    height = 1
    x = 2
    y = -2
    z = 0.5

    pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])

    # Finalize the URDF file
    pyrosim.End()


Create_World()
Create_Robot()
