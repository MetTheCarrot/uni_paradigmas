from utils import menu, pauseOS, clearOS, floatInput
from circulo import circulo
from cuadrado import cuadrado
from triangulo import triangulo
from rectangulo import rectangulo

class interfaz:
    def __init__(self):
        self.circulo, self.cuadrado, self.triangulo, self.rectangulo = None, None, None, None        

    # Menú principal

    def menu(self):
        opc = menu("""
        Mi programa, seleccione las opciones

        [1] Circulo
        [2] Cuadrado
        [3] Triangulo
        [4] Rectángulo

        [0] Salir
        """, maxOptions=4)
        self.opciones(opc)

    def opciones(self, opc : int):
        clearOS()
        match opc:
            case 0:
                print("Saliendo...")
                exit() # Salir del programa
            case 1: # Circulo
                self.submenu_circulo()
            case 2: # Cuadrado
                self.submenu_cuadrado()
            case 3: # Triangulo
                self.submenu_triangulo()
            case 4: # Rectangulo
                self.submenu_rectangulo()
            case _:
                print("Opcion no valida")
                pauseOS()
        self.menu()
    
    # Figura: Circulo

    def submenu_circulo(self):
        opc = menu("""
        --- Menú Circulo ---
        [1] Cambiar radio
        [2] Calcular área
        [3] Calcular perímetro
        [4] Calcular diametro
        [5] Calcular arco

        [0] Volver
        """, maxOptions = 5)
        self.opciones_circulo(opc)

    def esta_creado_instancia_circulo(self):
        if(self.circulo == None):
            print("No se han ingresado los valores")
            return False
        return True

    def opciones_circulo(self, opc : int):
        match opc:
            case 1:
                self.circulo = circulo(
                    floatInput("Ingrese el valor del radio: ")
                )
            case 2:
                print("El área del circulo es: " + str(self.circulo.area())) if self.esta_creado_instancia_circulo() else None
            case 3:
                print("El perímetro del circulo es: " + str(self.circulo.perimetro())) if self.esta_creado_instancia_circulo() else None
            case 4:
                print("El diametro del circulo es: " + str(self.circulo.diametro())) if self.esta_creado_instancia_circulo() else None
            case 5:
                print("El arco del circulo es: " + str(self.circulo.arco(floatInput("Ingrese el ángulo: ")))) if self.esta_creado_instancia_circulo() else None
            case 0:
                clearOS()
                print("Volviendo...")
                return
        pauseOS()
        self.submenu_circulo()

    # Figura: Cuadrado

    def submenu_cuadrado(self):
        opc = menu("""
        --- Cuadrado ---
        [1] Cambiar lado
        [2] Calcular área
        [3] Calcular perímetro
        [4] Calcular diagonal

        [0] Volver
        """, maxOptions = 4)
        self.opciones_cuadrado(opc)    

    def esta_creado_instancia_cuadrado(self):
        if(self.cuadrado == None):
            print("No se han ingresado los valores")
            return False
        return True

    def opciones_cuadrado(self, opc : int):
        match opc:
            case 1:
                self.cuadrado = cuadrado(
                    floatInput("Ingrese el valor del lado: ")
                )
            case 2:
                print("El área del cuadrado es: " + str(self.cuadrado.area())) if self.esta_creado_instancia_cuadrado() else None
            case 3:
                print("El perímetro del cuadrado es: " + str(self.cuadrado.perimetro())) if self.esta_creado_instancia_cuadrado() else None
            case 4:
                print("La diagonal del cuadrado es: " + str(self.cuadrado.diagonal())) if self.esta_creado_instancia_cuadrado() else None
            case 0:
                clearOS()
                print("Volviendo...")
                return
        pauseOS()
        self.submenu_cuadrado()
    
    # Figura: Triangulo

    def submenu_triangulo(self):
        opc = menu("""
               --- Menú Triángulo ---
        [1] Ingresa los valores de los lados
        [2] Calcular área
        [3] Calcular perímetro
        [4] Calcular base
        [5] Calcular altura
        [6] Conocer tipo de triángulo

        [0] Volver
        """, maxOptions = 6)
        self.opciones_triangulo(opc)

    def esta_creado_instancia_triangulo(self):
        if(self.triangulo == None):
            print("No se han ingresado los valores")
            return False
        return True
    
    def opciones_triangulo(self, opc : int):
        match opc:
            case 1:
                self.triangulo = triangulo(
                    floatInput("Ingrese el valor del lado a: "),
                    floatInput("Ingrese el valor del lado b: "),
                    floatInput("Ingrese el valor del lado c: ")
                )
            case 2:
                print("El área del triángulo es: " + str(self.triangulo.area())) if self.esta_creado_instancia_triangulo() else None
            case 3:
                print("El perímetro del triángulo es: " + str(self.triangulo.perimetro())) if self.esta_creado_instancia_triangulo() else None
            case 4:
                print("La base del triángulo es: " + str(self.triangulo.base())) if self.esta_creado_instancia_triangulo() else None
            case 5:
                print("La altura del triángulo es: " + str(self.triangulo.altura())) if self.esta_creado_instancia_triangulo() else None
            case 6:
                print("El triángulo es: " + str(self.triangulo.tipo_lado())) if self.esta_creado_instancia_triangulo() else None
            case 0:
                clearOS()
                print("Volviendo...")
                return
        pauseOS()
        self.submenu_triangulo()
    
    # Figura: Rectangulo

    def submenu_rectangulo(self):
        opc = menu("""
        --- Menú Rectángulo ---
        [1] Cambiar valores de x y z
        [2] Área
        [3] Perímetro
        [4] Diagonal
        [0] Volver
        """, maxOptions=4)
        self.opciones_rectangulo(opc)
    
    def esta_creado_instancia_rectangulo(self):
        if(self.rectangulo == None):
            print("No se han ingresado los valores")
            return False
        return True

    def opciones_rectangulo(self, opc : int):
        match opc:
            case 1:
                self.rectangulo = rectangulo(
                    floatInput("Ingrese el valor de x: "),
                    floatInput("Ingrese el valor de y: ")
                )
            case 2:
                print(f"Área: {self.rectangulo.area()}") if self.esta_creado_instancia_rectangulo() else None
            case 3:
                print(f"Perímetro: {self.rectangulo.perimetro()}") if self.esta_creado_instancia_rectangulo() else None
            case 4:
                print(f"Diagonal: {self.rectangulo.diagonal()}") if self.esta_creado_instancia_rectangulo() else None
            case 0:
                clearOS()
                print("Volviendo...")
                return
        pauseOS()
        self.submenu_rectangulo()
