#FUNCIONES DE LIMPIAR PANTALLA Y ESPERAR TECLA

import msvcrt #biblioteca estándar de C en Windows
import os #módulo estándar que permite realizar operaciones relacionadas con el sistema de archivos
import platform #accede a la información sobre el sistema operativo en el que se esta trabajando

def esperarTecla():
    print("") #un espacio para separarlo de letreros
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch() #espera que presione una teclita

def limpiarPantalla():
    #esto hará que ejecute a alguien con Linux
    if platform.system() == "Windows": 
        os.system("cls")  # Limpiar pantalla en Windows
    else:
        os.system("clear")  # Limpiar pantalla en Unix/Linux
    
    