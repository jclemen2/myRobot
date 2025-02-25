import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import os

# Define the full path to the data directory
data_dir = "/Users/justineclement/PycharmProjects/myRobot/data"
os.makedirs(data_dir, exist_ok=True)  # Ensure the directory exists

class MOTOR: # name of the class
    def __init__(self, jointName):  # Constructor
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        """Prepares the motor by initializing its parameters."""
        # Set different frequency based on the motor type
        if self.jointName == "Torso_BackLeg":
            self.amplitude = c.AMPLITUDE
            self.frequency = c.FREQUENCY  # Original frequency
            self.offset = c.PHASEOFFSET
        elif self.jointName == "Torso_FrontLeg":
            self.amplitude = c.AMPLITUDE
            self.frequency = c.FREQUENCY / 2  # Half the frequency
            self.offset = c.PHASEOFFSET
        else:
            # Default values if an unknown joint is encountered
            self.amplitude = c.AMPLITUDE_BACKLEG
            self.frequency = c.FREQUENCY_BACKLEG
            self.offset = c.PHASEOFFSET_BACKLEG

        time_values = numpy.linspace(c.START, c.STEP, c.SIMULATION_TIME)
        self.motorValues = self.amplitude * numpy.sin(self.frequency * time_values + self.offset)

    def Set_Value(self, robot, desiredAngle):
        # Sets the motor's value at time step t
        targetPosition = desiredAngle  # Determine the correct element for this time step
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot.robotId,  # Attach motor to the correct robot
            jointName=self.jointName,  # Attach motor to the correct joint
            controlMode=p.POSITION_CONTROL,  # Control the joint's motion
            targetPosition=targetPosition,  # Set target position
            maxForce=c.FORCE_MOTOR)  # Apply maximum force

    def Save_Values(self):
        """Saves motor values to a file."""
        file_path = os.path.join(data_dir, f"motorTargetAngles_{self.jointName}.npy")
        numpy.save(file_path, self.motorValues)
        print(f"Saved motor data: {file_path}")