# Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

# Definir la lista de 8 números enteros
numeros = [5, 8, 2, 9, 1, 7, 4, 3]

# Recorrer la lista y mostrarla
def mostrar_lista(lista):
    print("Lista:")
    for numero in lista:
        print(numero, end=' ')
    print()

print(" Recorrer la lista y mostrarla:")
try:
    mostrar_lista(numeros)
except ValueError:
    print(f"Error al mostrar la lista:")

# Hacer una función que recorra la lista de números y devuelva un string
def lista_a_string(lista):
    try:
        return ' '.join(map(str, lista))
    except ValueError:
        return f"Error al convertir la lista a string: "

print(" Convertir la lista a string:")
try:
    string_lista = lista_a_string(numeros)
    print(string_lista)
except:
    print(f"Error al convertir la lista a string: ")

#  Ordenarla y mostrarla
print(" Lista ordenada:")
try:
    numeros_ordenados = sorted(numeros)
    mostrar_lista(numeros_ordenados)
except ValueError:
    print(f"Error al ordenar la lista:")

#  Mostrar su longitud
print("Longitud de la lista:")
try:
    longitud = len(numeros)
    print(longitud)
except ValueError:
    print(f"Error al obtener la longitud de la lista:")

# Buscar algún elemento que el usuario pida por teclado
def buscar_elemento(lista, elemento):
    try:
        if elemento in lista:
            return f"El elemento {elemento} se encuentra en la lista."
        else:
            return f"El elemento {elemento} no se encuentra en la lista."
    except ValueError:
        return f"Error al buscar el elemento en la lista:"

print( "Buscar un elemento en la lista")
try:
    elemento_buscado = int(input("Ingrese el número que desea buscar: "))
    resultado_busqueda = buscar_elemento(numeros, elemento_buscado)
    print(resultado_busqueda)
except ValueError:
    print("Error: Debe ingresar un número entero.")
except TypeError:
    print(f"Error al buscar el elemento en la lista:")