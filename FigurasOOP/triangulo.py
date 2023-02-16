import math

class triangulo:
    def __init__(self, lado1 : float, lado2 : float, lado3 : float):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    #     self.informacion_triangulo()

    # def informacion_triangulo(self):
    #     lado1, lado2 = self.lados()
    #     print(f"""
    #     Tipo de triángulo: {self.tipo_lado()}
    #     Lado 1: {lado1}
    #     Lado 2: {lado2}
    #     Base: {self.base()}
    #     """)
    #     input()

    def base(self):
        tipo_lado = self.tipo_lado()
        if(tipo_lado == 'equilátero'):
            return self.lado1 # Si es equilatero, todos los lados son iguales
        elif(tipo_lado == 'isósceles'):
            # Si es isosceles, dos lados son iguales
            if(self.lado1 == self.lado2):
                return self.lado3
            elif (self.lado1 == self.lado3):
                return self.lado2
            else:
                return self.lado1
        else:
            # Si es escaleno, todos los lados son diferentes
            # La base es el lado mayor, fuentes: el tablero de la clase
            return max(self.lado1, self.lado2, self.lado3)

    def lados(self):
        base = self.base()
        if(base == self.lado1):
            return self.lado2, self.lado3
        elif(base == self.lado2):
            return self.lado1, self.lado3
        else:
            return self.lado1, self.lado2    

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        from math import sqrt
        # Heron's formula
        s = self.perimetro() / 2
        return sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def altura(self):
        tipo = self.tipo_lado()
        base = self.base()
        lado_1 = self.lados()
        match tipo:
            case 'equilátero', 'isósceles':
                return math.sqrt(lado_1 ** 2 - (base / 2) ** 2)
            case 'escaleno':
                return 2 * self.area() / base
    
    def tipo_lado(self):
        if self.lado1 == self.lado2 == self.lado3:
            return 'equilátero'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return 'isósceles'
        else:
            return 'escaleno'
