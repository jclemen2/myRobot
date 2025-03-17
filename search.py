from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os

# Create an instance of HILL_CLIMBER
phc = PARALLEL_HILL_CLIMBER()

# Run the evolutionary process
phc.Evolve()

# Show the best solution in GUI mode
phc.Show_Best()

# def main():
#     # Loop to generate and simulate robots twice
#     for i in range(5):
#         print(f"Iteration {i + 1}")
#
#         # Execute generate.py
#         os.system("python3 generate.py")
#
#         # Execute simulate.py
#         os.system("python3 simulate.py")
#
# if __name__ == "__main__":
#     main()
