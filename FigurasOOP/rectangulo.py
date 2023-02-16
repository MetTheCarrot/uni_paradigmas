from utils import menu, pauseOS, clearOS, floatInput
from math import sqrt

class rectangulo:
    def __init__(self, x : float, z : float):
        self.x = x
        self.z = z
    
    def area(self):
        return self.x * self.z
    
    def perimetro(self):
        return 2 * (self.x + self.z)
    
    def diagonal(self):
        return sqrt(self.x ** 2 + self.z ** 2)    
