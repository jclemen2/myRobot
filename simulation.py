from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
    def __init__(self):
        # Connect to physics simulation
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.grav_x, c.grav_y, c.grav_z)

        # Initialize world and robot
        self.world = WORLD()
        self.robot = ROBOT()

        # Prepare to simulate the robot
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()


    def Run(self):
        for t in range(c.simulation_time):
            # print(t)
            p.stepSimulation()

            # Enable sensing in the robot and pass the current time steep
            self.robot.Sense(t)

            #
            # # Get sensor values
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #
            # # Simulate motor
            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex=robotId, # What robot should the motor be attached to
            # jointName="Torso_BackLeg",  # What joint should the motor be attached to
            # controlMode=p.POSITION_CONTROL,  # How the motor will attempt to control the motion of the joint
            # targetPosition=motorTargetAngles_backLeg[i],  # Desired position
            # maxForce=c.force_motor_backleg)  # Total torque
            #
            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex=robotId,  # What robot should the motor be attached to
            # jointName="Torso_FrontLeg",  # What joint should the motor be attached to
            # controlMode=p.POSITION_CONTROL,  # How the motor will attempt to control the motion of the joint
            # targetPosition=motorTargetAngles_frontLeg[i],  # Desired position
            # maxForce=c.force_motor_frontleg)  # Total torque
            #
            # # Slow the simulation
            time.sleep(c.sleep)

    def __del__(self):
        p.disconnect() # Disconnect physics client when the simulation ends