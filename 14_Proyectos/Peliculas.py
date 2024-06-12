from Funciones import*

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

while True:

    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_pelicula()
    
    elif opcion == "2":
        remover_pelicula()
    elif opcion == "2":
        remover_pelicula()
    elif opcion == "3":
        consultar_peliculas()
    elif opcion =="4":
        vaciar_peliculas()
    elif opcion == "5":
        print("Saliendo del programa...")
       
        break
    else:
        print("Opción no válida, por favor intente nuevamente.")