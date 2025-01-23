import numpy
import matplotlib.pyplot as plt

from simulate import backLegSensorValues
from simulate import frontLegSensorValues
from simulate import motorTargetAngles_backLeg
from simulate import motorTargetAngles_frontLeg

# Load the sensor values from the file.
data_backLeg = numpy.load("data/backLegSensorValues.npy")
data_frontLeg = numpy.load("data/frontLegSensorValues.npy")
data_motorTargetAngles_backLeg = numpy.load("data/motorTargetAngles_backLeg.npy")
data_motorTargetAngles_frontLeg = numpy.load("data/motorTargetAngles_frontLeg.npy")

# Plot sensor data
plt.figure(1)
plt.plot(backLegSensorValues, label="Back Leg", linewidth=5)
plt.plot(frontLegSensorValues, label="Front Leg")

# Plot motor target angle
plt.figure(2)
plt.plot(motorTargetAngles_frontLeg, label="Front leg motor values", linewidth=5)
plt.plot(motorTargetAngles_backLeg, label="Back leg motor values")
plt.title("Motor Commands")
plt.xlabel("Steps")
plt.ylabel("Value in Radians")

# Annotate Graph
plt.legend()
plt.show()


