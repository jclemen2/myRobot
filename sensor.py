import numpy
import constants as c
import pyrosim.pyrosim
import numpy

class SENSOR:
    def __init__(self, linkName):
        """Initialize sensor with the given link name."""
        self.linkName = linkName  # Store link name
        self.values = numpy.zeros(c.TIMESTEPS)  # Create a vector for sensor values

    def Get_Value(self, t):
        # Check if the index t is within bounds
        if t >= len(self.values):
            raise IndexError(f"Index {t} out of range for sensor {self.linkName}")

        sensor_value = pyrosim.pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        # Ensure we are not exceeding the index by extending self.values if necessary
        while len(self.values) <= t:
            self.values = numpy.append(self.values, 0)  # Extend with zeros if needed

        self.values[t] = sensor_value  # Store the value at the correct time step

    def Save_Values(self):
        """Save sensor values to a file."""
        numpy.save(f"data/sensor_{self.linkName}.npy", self.values)