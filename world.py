import pybullet as p

class WORLD: # name of the class
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")# Constructor
        p.loadSDF("world.sdf")