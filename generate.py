from ctypes import c_int32
import pyrosim.pyrosim as pyrosim

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

    # set variables size and position for link0
    length_link0 = 1
    width_link0 = 1
    height_link0 = 1
    x_link0 = 0
    y_link0 = 0
    z_link0 = 0.5

    # set variables size and position for link1
    length_link1 = 1
    width_link1 = 1
    height_link1 = 1
    x_link1 = 0
    y_link1 = 0
    z_link1 = 0.5

    # set variables size and position for link2
    length_link2 = 1
    width_link2 = 1
    height_link2 = 1
    x_link2 = 0
    y_link2 = 0
    z_link2 = 0.5

    # set variables size and position for link3
    length_link3 = 1
    width_link3 = 1
    height_link3 = 1
    x_link3 = 0
    y_link3 = 0.5
    z_link3 = 0

    # set variables size and position for link4
    length_link4 = 1
    width_link4 = 1
    height_link4 = 1
    x_link4 = 0
    y_link4 = 0.5
    z_link4 = 0

    # set variables size and position for link5
    length_link5 = 1
    width_link5 = 1
    height_link5 = 1
    x_link5 = 0
    y_link5 = 0
    z_link5 = -0.5

    # set variables size and position for link6
    length_link6 = 1
    width_link6 = 1
    height_link6 = 1
    x_link6 = 0
    y_link6 = 0
    z_link6 = -0.5

    pyrosim.Send_Cube(name="Link0", pos=[x_link0, y_link0, z_link0], size=[length_link0, width_link0, height_link0])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, 0, 1.0])
    pyrosim.Send_Cube(name="Link1", pos=[x_link1, y_link1, z_link1], size=[length_link1, width_link1, height_link1])
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0, 0, 1.0])
    pyrosim.Send_Cube(name="Link2", pos=[x_link2, y_link2, z_link2], size=[length_link2, width_link2, height_link2])
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[0, 0.5, 0.5])
    pyrosim.Send_Cube(name="Link3", pos=[x_link3, y_link3, z_link3], size=[length_link3, width_link3, height_link3])
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[0, 1.0, 0])
    pyrosim.Send_Cube(name="Link4", pos=[x_link4, y_link4, z_link4], size=[length_link4, width_link4, height_link4])
    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0, 0.5, -0.5])
    pyrosim.Send_Cube(name="Link5", pos=[x_link5, y_link5, z_link5], size=[length_link5, width_link5, height_link5])
    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0, 0, -1.0])
    pyrosim.Send_Cube(name="Link6", pos=[x_link6, y_link6, z_link6], size=[length_link6, width_link6, height_link6])

    # Finalize the URDF file
    pyrosim.End()

Create_World()
Create_Robot()
