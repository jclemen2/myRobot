from world import WORLD
from robot import ROBOT

import pybullet as p
import pybullet_data
import constants as c
import time

class SIMULATION: # name of the class
    # Constructor
    def __init__(self):
        self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.GRAV_X, c.GRAV_Y, c.GRAV_Z)

        # Create a world instance
        self.world = WORLD()

        # Create a robot instance
        self.robot = ROBOT()

    # Destructor
    def __del__(self):
        p.disconnect()

    def Run(self, steps=c.SIMULATION_TIME, time_step=c.SLEEP):
        for t in range (steps):
            p.stepSimulation()
            self.robot.Sense(t)  # Robot senses environment
            self.robot.Think()
            self.robot.Act(t) # Robot acts on environment
            #time.sleep(time_step)  # Slow down to visualize steps

            # Slow the simulation
            time.sleep(c.SLEEP)

        # # Save sensor and motor values after simulation
        # for sensor in self.robot.sensors.values():
        #     sensor.Save_Values()
        #
        # for motor in self.robot.motors.values():
        #     motor.Save_Values()

    def Get_Fitness(self):
        self.robot.Get_Fitness()