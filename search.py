from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()

# robot = 5
# for i in range(robot):
#     os.system("python generate.py")
#     os.system("python simulate.py")