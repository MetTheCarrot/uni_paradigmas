from operaciones import operaciones

class interfaz:
    def __init__(self):
        self.opr = None
    
    def menu(self):
        salir = False
        opc = 0
        while salir is False:
            print("Bienvenidos a mi programa")
            print("##########################")
            print("Seleccione una de las siguientes opciones")
            print("1. Ingresar los valores.")
            print("2. Sumar valores.")
            print("3. Restar valores.")
            print("4. Multiplicar valores.")
            print("5. Dividir valores.")
            print("##########################")
            print("0. Para salir del programa :'(.")
            opc = input()
            
            try:
                opc = int(opc)
            except:
                opc = 6
            if opc > 5:
                print("Valor de opcion  no valida")
            elif opc == 0:
                salir = True
            else:
                self.opciones(opc)
                
                
    
    def opciones(self, opc):
        match opc:
            case 1:
                print("Por favor escriba el valor de a")
                a = int(input())
                print("Por favor escriba el valor de b")
                b = int(input())
                self.opr = operaciones(a, b)
            case 2:
                if self.opr is None:
                    print("Pör favor ingrese los valores primero")
                else:
                    print("El resultado de la suma es:")
                    print(self.opr.sumar())
            case 3:
                if self.opr is None:
                    print("Pör favor ingrese los valores primero")    
                else:
                    print("El resultado de la resta es:")
                    print(self.opr.restar())
            case 4:
                if self.opr is None:
                    print("Pör favor ingrese los valores primero")    
                else:
                    print("El resultado de la multiplicacion es:")
                    print(self.opr.multiplicar())
            case 5:
                if self.opr is None:
                    print("Pör favor ingrese los valores primero")    
                else:    
                    print("El resultado de la division es:")
                    print(self.opr.dividir())
                
        pass