from ctypes import c_int32
import pyrosim.pyrosim as pyrosim

# Start generating the SDF file
pyrosim.Start_SDF("boxes.sdf")

# Define parameters for the grid and towers
num_rows = 5  # Number of rows in the grid
num_columns = 5  # Number of columns in the grid
tower_height = 10  # Number of blocks in each tower
initial_size = 1.0  # Initial size of the bottom block
size_reduction = 0.9  # Factor by which each block's size decreases


# Generate the grid of towers
for row in range(num_rows):
    for column in range(num_columns):
        # Calculate the (x, y) position for this tower
        x = row
        y = column
        z = initial_size / 2  # Starting z position for the first block in the tower

        # Generate the tower at (x, y)
        block_size = initial_size
        for level in range(tower_height):
            # Add a block to the tower
            pyrosim.Send_Cube(name=f"Box_{row}_{column}_{level}",
                              pos=[x, y, z],
                              size=[block_size, block_size, block_size])
            # Update z position and block size for the next level
            z += block_size
            block_size *= size_reduction

# Finalize the SDF file
pyrosim.End()

