from math import sqrt

class rectangulo:
    def __init__(self, x : float, z : float):
        self.x = x
        self.z = z
    
    def area(self):
        return round(self.x * self.z, 2)
    
    def perimetro(self):
        return round(2 * (self.x + self.z), 2)
    
    def diagonal(self):
        return round(sqrt(self.x ** 2 + self.z ** 2),2)
