from math import pi

# Variables Time of Simulation
SIMULATION_TIME = 100

# Variables robot
AMPLITUDE_BACKLEG   = pi/4
FREQUENCY_BACKLEG = 20
PHASEOFFSET_BACKLEG = 0

AMPLITUDE_FRONTLEG = 0
FREQUENCY_FRONTLEG = 0
PHASEOFFSET_FRONTLEG = 0

AMPLITUDE = pi/4
FREQUENCY = 20
PHASEOFFSET = 0

# Variables gravity
GRAV_X = 0
GRAV_Y = 0
GRAV_Z = -9.8

# Variables Array
START = 0
STEP = 2 * pi

# Variables Motor force
FORCE_MOTOR = 50

# Variables sleeping time of simulation
SLEEP = 1/100

numberOfGenerations = 1
populationSize = 1

numSensorNeurons = 6
numMotorNeurons = 5