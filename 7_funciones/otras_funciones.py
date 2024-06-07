# def solicitarNumeros():
#   global n1,n2  
#   n1=int(input("Numero #1: "))
#   n2=int(input("Numero #2: "))
  

# def operacionAritmetica(num1,num2,opcion):  
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#       return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#      return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#      return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
#      return f"{n1}/{n2}={n1/n2}" 
     
# def esperarTecla():
#  print("Oprima cualquier tecla para continuar: ")
#  input()
# opcion=True    
# while opcion:
 
#  print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
#  opcion=input("\t Elige una opción: ").upper()
#  if opcion!="5":

#    solicitarNumeros()
#    print(operacionAritmetica(n1,n2,opcion))
#    esperarTecla()
#  else:  
#    opcion=False  
#    print("Terminaste la ejecucion del SW") 


peliculas = []
def agregar_pelicula():
    pelicula = input("Ingrese el nombre de la película que desea agregar: ")
    peliculas.append(pelicula)
    print(f"Película '{pelicula}' agregada con éxito.")

def remover_pelicula():
    pelicula = input("Ingrese el nombre de la película que desea remover: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"Película '{pelicula}' removida con éxito.")
    else:
        print(f"Película '{pelicula}' no encontrada en la lista.")

def consultar_peliculas():
    if peliculas:
        print("Listado de películas:")
        for pelicula in peliculas:
            print(f"- {pelicula}")
    else:
        print("No hay películas en la lista.")

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

