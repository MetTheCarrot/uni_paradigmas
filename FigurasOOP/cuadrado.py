class cuadrado:
    def __init__(self, lado : float):
        self.lado = lado

    def area(self):
        return round(self.lado ** 2, 2)
    
    def perimetro(self):
        return round(self.lado * 4, 2)
    
    def diagonal(self):
        from math import sqrt
        return round(self.lado * sqrt(2), 2)    
    