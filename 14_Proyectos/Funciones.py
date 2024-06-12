opcion = True
while opcion:

    if opcion in ["1", "2", "3", "4", "5"]:
        n1 = float(input("Numero #1: "))
        n2 = float(input("Numero #2: "))
        if opcion == "1" or opcion == "+":
            print(f"{n1} + {n2} = {n1 + n2}")
        elif opcion == "2" or opcion == "-":
            print(f"{n1} - {n2} = {n1 - n2}")
        elif opcion == "3" or opcion == "*":
            print(f"{n1} * {n2} = {n1 * n2}")
        elif opcion == "4" or opcion == "/":
            if n2 != 0:
                print(f"{n1} / {n2} = {n1 / n2}")
            else:
                print("No se puede dividir por cero")
        elif opcion == "5":
            print(f"{n1} ^ {n2} = {n1 ** n2}")
    elif opcion == "6":
        n = float(input("Ingrese un número para calcular su raíz cuadrada: "))
        if n >= 0:
            print(f"Raiz cuadrada de {n} = {n ** 0.5}")
        else:
            print("No se puede calcular la raíz cuadrada de un número negativo")
    elif opcion == "7":
        print("Terminaste la ejecución del programa")
        opcion = False
    else:
        print("Opción no válida")



    

peliculas = []
import os 
opcion=True 

def agregar_pelicula():
    pelicula = input("Ingrese el nombre de la película que desea agregar: ")
    peliculas.append(pelicula)
    print(f"Película '{pelicula}' agregada con éxito.")
    esperarTecla()

def remover_pelicula():
    pelicula = input("Ingrese el nombre de la película que desea remover: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"Película '{pelicula}' removida con éxito.")
    else:
        print(f"Película '{pelicula}' no encontrada en la lista.")
        esperarTecla()

def consultar_peliculas():
    if peliculas:
        print("Listado de películas:")
        for pelicula in peliculas:
            print(f"- {pelicula}")
    else:
        print("No hay películas en la lista.")
        esperarTecla()

def vaciar_peliculas():
    peliculas.clear()
    print("La lista de películas ha sido vaciada.")
def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Vaciar")
    print("5. Salir")

def esperarTecla():
 print("Oprima cualquier tecla para continuar: ")
 input() 
os.system("Clear")  
