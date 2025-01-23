from simulation import SIMULATION

# Create a simulation instance
simulation = SIMULATION()

# Run the simulation
simulation.Run()


# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import os
# from math import pi
# import constants as c
# import time
#
# # Create array to store sensor values
# backLegSensorValues = numpy.zeros(c.simulation_time)
# frontLegSensorValues = numpy.zeros(c.simulation_time)
#
# # Create array to store sinusoidal motor values
# num_iterations = c.simulation_time
# time_values = numpy.linspace(c.start, c.step * pi, num_iterations)
# motorTargetAngles_backLeg = c.amplitude_backLeg * numpy.sin(c.frequency_backLeg * time_values + c.phaseOffset_backLeg)
# motorTargetAngles_frontLeg = c.amplitude_frontLeg * numpy.sin(c.frequency_frontLeg * time_values + c.phaseOffset_frontLeg)
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#
# p.setGravity(c.grav_x,c.grav_y,c.grav_z)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)
#
# for i in range (c.simulation_time):
#     p.stepSimulation()
#
#     # Get sensor values
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#
#     # Simulate motor
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId, # What robot should the motor be attached to
#         jointName="Torso_BackLeg",  # What joint should the motor be attached to
#         controlMode=p.POSITION_CONTROL,  # How the motor will attempt to control the motion of the joint
#         targetPosition=motorTargetAngles_backLeg[i],  # Desired position
#         maxForce=c.force_motor_backleg)  # Total torque
#
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,  # What robot should the motor be attached to
#         jointName="Torso_FrontLeg",  # What joint should the motor be attached to
#         controlMode=p.POSITION_CONTROL,  # How the motor will attempt to control the motion of the joint
#         targetPosition=motorTargetAngles_frontLeg[i],  # Desired position
#         maxForce=c.force_motor_frontleg)  # Total torque
#
#     # Slow the simulation
#     time.sleep(c.sleep)
#
# # Define the full path to the data directory
# data_dir = "/Users/justineclement/PycharmProjects/myRobot/data"
#
# # Define the full path for the file
# file_path_backLeg = os.path.join(data_dir, "backLegSensorValues.npy")
# file_path_frontLeg = os.path.join(data_dir, "frontLegSensorValues.npy")
# file_path_motorTargetAngles_backLeg = os.path.join(data_dir, "motorTargetAngles_backLeg.npy")
# file_path_motorTargetAngles_frontLeg = os.path.join(data_dir, "motorTargetAngles_frontLeg.npy")
#
# # Save the array to the file
# numpy.save(file_path_backLeg, backLegSensorValues)
# numpy.save(file_path_frontLeg, frontLegSensorValues)
# numpy.save(file_path_motorTargetAngles_backLeg, motorTargetAngles_backLeg)
# numpy.save(file_path_motorTargetAngles_frontLeg, motorTargetAngles_frontLeg)
#
# p.disconnect()
