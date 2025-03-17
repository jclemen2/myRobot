from hillclimber import HILL_CLIMBER
import os

# Create an instance of HILL_CLIMBER
hc = HILL_CLIMBER()

# Run the evolutionary process
hc.Evolve()

# Show the best solution in GUI mode
hc.Show_Best()

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
