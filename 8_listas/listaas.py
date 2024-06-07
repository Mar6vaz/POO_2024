"""
Listas (Array)
Son collecciones o conjunto de datos/valores bajoun mismo nombre, para acceder a los valores se hace con un indice numerico 

Nota: sus balores si son modificables 
la lista es una coleccion ordenada y modificable. permite mienbros duplicados.
"""


# #Ekemplo 1 crear un lista de numeros e imprimir contenido

# numeros=[23,34]
# print(numeros)

# #Recorrer la lista con siclo for
# for i in numeros:
#     print(i)

# #Recorrefr la lista con siclo while 
# i=0
# while i<=len(numeros)-1:
#     print(numeros[i])
#     i+=1

#Ejemplo 2 Creatr un lista de palabras y posteriormente buscar la coincidencia de un palabra 

# palabra = ["hola","utd", "como", "estas", "naranja"]
# palabra_buscar = input("inserta palabra a buscar: ")

# if palabra_buscar in palabra:
#     for i, p in enumerate(palabra):
#         if p == palabra_buscar:
#             print(f"Encontré la palabra en la posición {i}")
# i=0
# while i<len(palabra):
#         if palabra[i] == palabra_buscar:
#             print(f"Encontré la palabra en la posición {i}")
#             encontro=True
#             i+=1
    
    
# else:
#     print("No encontré la palabra en la lista")

#Ejemplo 3 Agregar y Eliminar elementos de una lista 
#os.system("clear")

# numeros=[23,34,23]
# print(numeros)

#Agregar un elemento 
# numeros.append(100)
# print(numeros)
# numeros.insert(3,200)
# print(numeros)

#Eliminar un elemento
# numeros.remove(100)#indicar el elememeto a borrar
# print(numeros )
# numeros.pop(2)#Indicar la posocion del elemento a borrar 
# print(numeros)
 
#Ejemplo 4 Crear un alista multilinea (matriz) para agregar los nombre y numeros de telefono

# agenda=[
#      ["Carlos", 6181234567],
#      ["Leo", 6671234567]
#      ["Santiago", 6182341234]
#      ["Pedro", 6171236789]
# ]

# print(agenda) 

# for i in agenda:
#     print(f"{agenda.index(i)+1}, -{i}")

#Ejemplo 5 Crear un programa que permita Gestionar (administrar) pelicilas, colocar un menu de opciones para agregar, remover, consulatr peliculas
#Nota:
#1.-Utilizar funciones y mandar llamar desde otro archivo 
#utilizar listas para almacenar los nombres de las peliculas 

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

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

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
    elif opcion == "3":
        consultar_peliculas()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")