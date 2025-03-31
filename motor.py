# Creating new file for class motor
# Imports
#from pybullet_envs.deep_mimic.env.testLaikago import jointIndex
#from pybullet_examples.humanoidMotionCapture import targetPosition

import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName # Store the joint name



    def Set_Value(self, robot, desiredAngle):
        """Apply motor control using precomputed values."""

        jointIndex = pyrosim.jointNamesToIndices[self.jointName]
        (p.setJointMotorControl2
            (bodyIndex=robot.robotId,
             jointIndex=jointIndex,
             controlMode=p.POSITION_CONTROL,
             targetPosition=desiredAngle,
             force=c.MAX_FORCE))