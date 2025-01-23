import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        # Store the link name
        self.linkName = linkName

        # Initialize a vector of zeros for sensor values
        self.values = numpy.zeros(c.simulation_time)

    def Get_Value(self, t):
        # Fetch the sensor value for the specific link and store it in the t-th index
        value = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if len(self.values) <= t:
            self.values.append(value)  # Add the value if it's the first time this index is being used
        else:
            self.values[t] = value  # Update the value at the t-th index

        # If this is the last time step, print the final sensor vector
        if t == c.simulation_time - 1:
            print(self.values)

