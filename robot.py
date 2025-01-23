from sensor import SENSOR
import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")

        # Dictionaries to store sensors and motors
        self.motor = {}

    def Prepare_To_Sense(self):
        # Initialize the sensors dictionary
        self.sensors = {}

        # Print link names to identify sensor placements
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        # Update sensor values for each sensor and store at the t-th index
        for linkName, sensor in self.sensors.items():
            sensor.Get_Value(t)  # Pass time step t to Get_Value method
