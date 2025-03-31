# Creating new file for class world

# Imports
import pybullet as p
import pybullet_data
import constants as c  # Import constants

class WORLD:

    def __init__(self):

        """Loads the world environment including the plane and other objects."""
        # Load floor plane
        self.planeId = p.loadURDF("plane.urdf")

        # Load the world with additional objects
        p.loadSDF("world.sdf")