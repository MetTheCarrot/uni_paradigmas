class circulo:
    def __init__(self, radio : float):
        from math import pi
        self.pi = pi
        self.radio = radio

    def area(self):
        return round(self.pi * self.radio**2, 2)

    def perimetro(self):
        return round(2 * self.pi * self.radio, 2)
        
    def diametro(self):
        return round(2 * self.radio, 2)

    def arco(self, angulo : float):
        return round((2*self.pi*self.radio*angulo)/360, 2)
        