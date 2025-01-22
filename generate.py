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

# Finalize the SDF file
pyrosim.End()

