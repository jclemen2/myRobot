# Creating new file for class simulation

# Imports
import pybullet as p
import pybullet_data
import constants as c
import time
# Import pyrosim
# Importing other class files
from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        #self.robot = ROBOT(self.solutionID)

        # Initialize the simulation based on the mode
        if self.directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)  # Heads-up mode
        else:
            self.physicsClient = p.connect(p.DIRECT)  # Blind mode

        # Set the search path for assets
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Add gravity
        p.setGravity(0, 0, c.GRAVITY)

        # Create world and robot instances
        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)

    def __del__(self):
        try:
            p.disconnect()
        except:
            pass  # ignore if already disconnected


    def Run(self, steps=c.TIMESTEPS, time_step=c.FRAME_RATE):
        for t in range(steps):
            p.stepSimulation()
            self.robot.Sense(t)  # Robot senses environment
            self.robot.Think()
            self.robot.Act(t)  # Robot acts on environment
            time.sleep(time_step)  # Slow down to visualize steps

            # Slow the simulation
            if self.directOrGUI == "GUI":
                time.sleep(1 / 240)
            else:
                time.sleep(c.FRAME_RATE)

    def Get_Fitness(self):
        self.robot.Get_Fitness()