import numpy
import matplotlib.pyplot as plt

from simulate import backLegSensorValues
from simulate import frontLegSensorValues

# Load the sensor values from the file
data_backLeg = numpy.load("data/backLegSensorValues.npy")
data_frontLeg = numpy.load("data/frontLegSensorValues.npy")

# Plot data
plt.plot(backLegSensorValues, label="Back Leg", linewidth=3.5)
plt.plot(frontLegSensorValues, label="Front Leg")

# Annotate Graph
plt.legend()
plt.show()


