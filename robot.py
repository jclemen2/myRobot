from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import time
import numpy as np

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        #GB()

        # Loads the robot body and prepares it for simulation.
        self.robotId = p.loadURDF("body1.urdf")  # Load robot URDF

        # Prepare robot for simulation
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Prepare sensors for all links
        self.Prepare_To_Sense()

        # Prepare motors
        self.Prepare_To_Act()

        brain_filename = f"brain{solutionID}.nndf"
        self.nn = NEURAL_NETWORK(brain_filename)

        # Delete the brain file after it has been read
        if os.name == "nt":  # Windows
            os.system(f"del {brain_filename}")
        else:  # Mac/Linux
            os.system(f"rm {brain_filename}")

    def Prepare_To_Sense(self):
        """Initialize the dictionary for sensors."""
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)   # Create SENSOR instance

    def Prepare_To_Act(self):
        '''Initialize the dictionary for motors'''
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)  # Create MOTOR instance

    def Sense(self, t):
        for sensor in self.sensors.values():  # Iterate over all SENSOR instances
            sensor.Get_Value(t)  # Call Get_Value() on each sensor to update its values

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                # Extract the value (desired angle) for this motor neuron
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange

                # Ensure the jointName is a decoded string, in case it's a byte string
                decoded_joint_name = jointName.decode("utf-8") if isinstance(jointName, bytes) else jointName

                # Apply extension bias and boost force for lower legs
                if "Lower" in decoded_joint_name:
                    desiredAngle += 0.5  # Push toward straight (adjust as needed)
                    self.motors[decoded_joint_name].Set_Value(self, desiredAngle, max_force=200)
                else:
                    self.motors[decoded_joint_name].Set_Value(self, desiredAngle)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        # Final Project Code

        # --- Leg Height Component ---
        lower_leg_links = [
            "FrontLowerLeg",
            "BackLowerLeg",
            "LeftLowerLeg",
            "RightLowerLeg"
        ]

        z_values = []
        for link_name in lower_leg_links:
            try:
                link_index = pyrosim.linkNamesToIndices[link_name]
                z = p.getLinkState(self.robotId, link_index)[0][2]
                z_values.append(z)
            except KeyError:
                z_values.append(0.0)
        leg_lift_component = sum(z_values) / len(z_values)

        # --- Torso Low Component ---
        torso_z = p.getBasePositionAndOrientation(self.robotId)[0][2]
        torso_low_component = max(0.0, 1.5 - torso_z)

        # --- Leg Extension Component ---
        leg_lower_joints = [
            "FrontLeg_Lower",
            "BackLeg_Lower",
            "LeftLeg_Lower",
            "RightLeg_Lower"
        ]

        extension_scores = []
        for joint_name in leg_lower_joints:
            try:
                joint_index = pyrosim.jointNamesToIndices[joint_name]
                joint_angle = abs(p.getJointState(self.robotId, joint_index)[0])  # radians
                score = 1.0 - min(joint_angle, np.pi) / np.pi  # normalized: 1 = straight
                extension_scores.append(score)
            except KeyError:
                extension_scores.append(0.0)

        leg_extension_component = sum(extension_scores) / len(extension_scores)

        # --- Final Fitness ---
        finalFitness = (
                1.0 * leg_lift_component +
                3.0 * torso_low_component +
                1.0 * leg_extension_component  # Boost extension influence
        )

        # Debug info
        print(
            f"Fitness Breakdown -> Leg Height: {leg_lift_component:.2f}, Torso Low: {torso_low_component:.2f}, Leg Extension: {leg_extension_component:.2f}")

        # 6. Save to file
        tmp_fitness_file = f"tmp{self.solutionID}.txt"
        with open(tmp_fitness_file, "w") as file:
            file.write(str(finalFitness))

        time.sleep(0.01)
        import os
        os.rename(tmp_fitness_file, f"fitness{self.solutionID}.txt")

        # Normal Quadruped Code
        # # Get the state of the first link (link zero)
        # basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        #
        # # Get the state of the first link (link zero)
        # basePosition = basePositionAndOrientation[0]
        #
        # # Extract the x coordinate (first element) from positionOfLinkZero
        # xCoordinateOfLinkZero = basePosition[0]
        #
        # # Write the x coordinate to a file (fitness.txt)
        # tmp_fitness_file = f"tmp{self.solutionID}.txt"
        # with open(tmp_fitness_file, "w") as file:
        #     file.write(str(xCoordinateOfLinkZero))  # Convert to string and write to file
        # time.sleep(0.01)
        #
        # os.rename("tmp" + str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")






    # def Get_Fitness(self):
    #     # Final Project Code
    #
    #     # Time-averaged components
    #     legsUpComponent = self.legs_no_touch_frames / c.TIMESTEPS
    #     torsoLowComponent = self.torso_on_ground_frames / c.TIMESTEPS
    #
    #     # Final fitness
    #     finalFitness = legsUpComponent + torsoLowComponent
    #
    #     # Optional: print debug info
    #     print(f"Fitness Breakdown -> Legs Up (Time): {legsUpComponent:.2f}, Torso Low (Time): {torsoLowComponent:.2f}")
    #
    #     # Save to file
    #     tmp_fitness_file = f"tmp{self.solutionID}.txt"
    #     with open(tmp_fitness_file, "w") as file:
    #         file.write(str(finalFitness))
    #
    #     time.sleep(0.01)
    #     os.rename(tmp_fitness_file, f"fitness{self.solutionID}.txt")

        # Milestone 2: Extreme Fitness Function
        # Component	Behavior Encouraged
            # Leg Height	              Raise legs vertically
            # Leg Extension	              Stretch legs far from body
            # Torso Lowered (Final Z)	  End low posture
            # Torso On Ground (Z Time)	  Stay low for many timesteps
            # Legs Up (No Touch)	      Keep legs lifted (not touching ground)
            # Torso Touch (Touch = 1)	  Physically press torso to ground (sit)
        # lower_leg_links = [
        #     "FrontLowerLeg",
        #     "BackLowerLeg",
        #     "LeftLowerLeg",
        #     "RightLowerLeg"
        # ]
        #
        # z_foot_values = []
        # extension_scores = []
        #
        # torso_pos = p.getBasePositionAndOrientation(self.robotId)[0]
        # torso_z = torso_pos[2]
        #
        # for link_name in lower_leg_links:
        #     try:
        #         link_index = pyrosim.linkNamesToIndices[link_name]
        #         leg_pos = p.getLinkState(self.robotId, link_index)[0]
        #
        #         # 1. Foot height
        #         z_foot_values.append(leg_pos[2])
        #
        #         # 2. Extension from torso center
        #         dist = np.linalg.norm(np.array(leg_pos) - np.array(torso_pos))
        #         extension_scores.append(dist)
        #
        #     except KeyError:
        #         z_foot_values.append(0.0)
        #         extension_scores.append(0.0)
        #
        # # --- Snapshot Components ---
        # legHeightComponent = sum(z_foot_values) / len(z_foot_values)
        # legExtensionComponent = sum(extension_scores) / len(extension_scores)
        # torsoLoweredComponent = max(0.0, 1.2 - torso_z)
        #
        # # --- Time-Averaged Components ---
        # torsoLowComponent = self.torso_on_ground_frames / c.TIMESTEPS
        # legsUpComponent = self.legs_no_touch_frames / c.TIMESTEPS
        # torsoTouchComponent = self.torso_touch_frames / c.TIMESTEPS
        #
        # # Combine all components
        # finalFitness = (
        #         1.0 * legHeightComponent +
        #         1.0 * legExtensionComponent +
        #         1.0 * torsoLoweredComponent +
        #         1.0 * torsoLowComponent +
        #         1.0 * legsUpComponent +
        #         1.0 * torsoTouchComponent
        # )
        #
        # # Optional debug
        # print(f"Fitness Breakdown -> Leg Height: {legHeightComponent:.2f}, Extension: {legExtensionComponent:.2f}, "
        #       f"Torso Low (Final): {torsoLoweredComponent:.2f}, Torso Down (Time): {torsoLowComponent:.2f}, "
        #       f"Legs Up (Time): {legsUpComponent:.2f}, Torso Touch (Time): {torsoTouchComponent:.2f}")
        #
        # # Save to file
        # tmp_fitness_file = f"tmp{self.solutionID}.txt"
        # with open(tmp_fitness_file, "w") as file:
        #     file.write(str(finalFitness))
        #
        # time.sleep(0.01)
        # os.rename(tmp_fitness_file, f"fitness{self.solutionID}.txt")




        # Normal Quadruped Code
        # # Get the state of the first link (link zero)
        # basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        #
        # # Get the state of the first link (link zero)
        # basePosition = basePositionAndOrientation[0]
        #
        # # Extract the x coordinate (first element) from positionOfLinkZero
        # xCoordinateOfLinkZero = basePosition[0]
        #
        # # Write the x coordinate to a file (fitness.txt)
        # tmp_fitness_file = f"tmp{self.solutionID}.txt"
        # with open(tmp_fitness_file, "w") as file:
        #     file.write(str(xCoordinateOfLinkZero))  # Convert to string and write to file
        # time.sleep(0.01)
        #
        # os.rename("tmp" + str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")