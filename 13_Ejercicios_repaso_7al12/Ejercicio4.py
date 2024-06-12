# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista = [1, 2, 3]
cadena = "Hola, mundo"
entero = 42
logico = True

def imprimir_tipo(variable):
    try:
        if isinstance(variable, list):
            print("La variable es una lista y su contenido es:", variable)
        elif isinstance(variable, str):
            print("La variable es una cadena y su contenido es:", variable)
        elif isinstance(variable, int):
            print("La variable es un entero y su valor es:", variable)
        elif isinstance(variable, bool):
            print("La variable es un booleano y su valor es:", variable)
        else:
            print("Tipo de variable no reconocido.")
    except ValueError:
        print(f"Ha ocurrido un error al determinar el tipo de la variable: ")

# Llamar a la función para cada variable
imprimir_tipo(lista)
imprimir_tipo(cadena)
imprimir_tipo(entero)
imprimir_tipo(logico)