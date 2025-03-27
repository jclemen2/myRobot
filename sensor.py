import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
import os

# Define the full path to the data directory
data_dir = "/Users/justineclement/PycharmProjects/myRobot/data"
os.makedirs(data_dir, exist_ok=True)

class SENSOR: # name of the class
    def __init__(self, linkName):  # Constructor
        self.linkName = linkName
        # Create array to store sensor values
        self.values = numpy.zeros(c.SIMULATION_TIME)

    def Get_Value(self, t):
        # Get sensor values
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        """Saves sensor values to a file."""
        file_path = os.path.join(data_dir, f"{self.linkName}SensorValues.npy")
        numpy.save(file_path, self.values)
        #print(f"Saved sensor data: {file_path}")
























