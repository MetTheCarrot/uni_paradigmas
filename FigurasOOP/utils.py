from os import system as cmd
from platform import system as os

def clearOS():
    if os() == "Windows":
        cmd("cls")
    else:
        cmd("clear")

def pauseOS():
    if os() == "Windows":
        cmd("pause")
    else:
        cmd("read -p 'Presione una tecla para continuar...' var")

def intInput(prompt : str):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def floatInput(prompt : str):
    while True:
        try:
            x = float(input(prompt))
            return x
        except ValueError:
            print("Error: Debe ingresar un número real.")

def menu(msg : str, maxOptions : int):
    while True:
        try:
            clearOS()
            print(msg)
            x = intInput("Ingrese una opción: ")
            if x < 0 or x > maxOptions:
                raise ValueError
            return x
        except ValueError:
            print("Error: Debe ingresar un número entero entre 0 y " + str(maxOptions) + ".")
            pauseOS()