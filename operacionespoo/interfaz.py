from operaciones import operaciones

class interfaz:
    def __init__(self):
        self.operaciones = None

    def menu(self):
        self.clearOS()
        print("""
        Bienvenidos a mi programa
        #########################
        Seleccione una opción:
        [1] Ingresar números
        [2] Sumar
        [3] Restar
        [4] Multiplicar
        [5] Dividir
        #########################
        [0] Salir
        """)
        opc = self.intInput("Ingrese una opción: ")
        self.opciones(opc)
    
    def checkOperaciones(self, opc : int):
        """_summary_ : Función para validar que se hayan ingresado los números"""
        if(opc == 1): # Opción para ingresar los números
            return 
        if self.operaciones == None:
            print("Debe ingresar los números primero")
            self.pauseOS()
            self.menu()
            return

    def opciones(self, opc : int):
        """_summary_ : Función para validar las opciones del menú"""
        self.clearOS()
        if(opc == 0):
            print("Gracias por utilizar mi programa")
            return # Salir del programa
        self.checkOperaciones()
        match opc:
            case 1:
                self.operaciones = operaciones(
                    self.intInput("Ingrese el primer número: "), 
                    self.intInput("Ingrese el segundo número: ")
                    )
            case 2:
                print(f'La suma es: {self.operaciones.sumar()}')
            case 3:
                print(f'La resta es: {self.operaciones.restar()}')
            case 4:
                print(f'La multiplicación es: {self.operaciones.multiplicar()}')
            case 5:
                print(f'La división es: {self.operaciones.dividir()}')
            case _:
                print("Opción incorrecta")
        self.pauseOS()      
        self.menu()
    
    def intInput(self, msg : str):
        """_summary_ : Función para validar que el usuario ingrese un número entero

        Args:
            msg (str): _Descripción del mensaje de solicitud_

        Returns:
            _int_: _retorna un numero tipo int, no podra ser otro_
        """
        while True:
            try:
                x = int(input(msg))
                return x
            except ValueError:
                print("Error: Debe ingresar un número entero.")    
    
    def clearOS(self):
        """_summary_ : Función para limpiar la pantalla
        """
        from os import system as cmd
        from platform import system as os
        if os() == "Windows":
            cmd("cls")
        else:
            cmd("clear")

    def pauseOS(self):
        """_summary_ : Función para pausar la ejecución del programa
        """
        from os import system as cmd
        from platform import system as os
        if os() == "Windows":
            cmd("pause")
        else:
            cmd("read -p 'Presione una tecla para continuar...' var")
