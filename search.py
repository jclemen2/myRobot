from hillclimber import HILL_CLIMBER
import os

hc = HILL_CLIMBER()

hc.Evolve()
hc.Show_Best()

# robot = 5
# for i in range(robot):
#     os.system("python generate.py")
#     os.system("python simulate.py")
