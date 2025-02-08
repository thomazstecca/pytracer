from vec3 import *
from color import * 

class ray:
    def __init__(self, origin: vec3 = 0, direction: vec3 = 0):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return (self.origin + (self.direction * t))

