class triangulo:
    def __init__(self, lado1 : float, lado2 : float, lado3 : float):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def base(self):
        tipo_lado = self.tipo_lado()
        match tipo_lado:
            case 'equilátero':
                return self.lado1 # Si es equilatero, todos los lados son iguales
            case 'isósceles':
                # Si es isosceles, dos lados son iguales, la base es el lado diferente
                if(self.lado1 == self.lado2):
                    return self.lado3
                elif (self.lado1 == self.lado3):
                    return self.lado2
                else:
                    return self.lado1
            case 'escaleno':
                # Si es escaleno, todos los lados son diferentes
                # La base es el lado mayor, fuentes: el tablero de la clase
                return max(self.lado1, self.lado2, self.lado3)

    def lados(self):
        base = self.base()
        match base:
            case self.lado1:
                return self.lado2, self.lado3
            case self.lado2:
                return self.lado1, self.lado3
            case _:
                return self.lado1, self.lado2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        from math import sqrt
        # Heron's formula
        s = self.perimetro() / 2
        return round(sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)),2)

    def altura(self):
        from math import sqrt
        tipo = self.tipo_lado()
        base = self.base()
        lado_1, lado_2 = self.lados()
        match tipo:
            case 'escaleno':
                return round(2 * self.area() / base, 2)
            case _:
                return round(sqrt(lado_1 ** 2 - (base / 2) ** 2),2)
    
    def tipo_lado(self):
        if self.lado1 == self.lado2 == self.lado3:
            return 'equilátero'
        elif (self.lado1 == self.lado2) or (self.lado1 == self.lado3) or (self.lado2 == self.lado3):
            return 'isósceles'
        else:
            return 'escaleno'
