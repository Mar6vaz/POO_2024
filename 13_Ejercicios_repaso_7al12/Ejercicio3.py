# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

lista = []
if not lista:
    print("La lista está vacía. Puedes añadir palabras o frases.")
    while True:
        try:
            entrada = input("Introduce una palabra o frase (o escribe 'salir' para terminar): ")
            if entrada.lower() == 'salir':
                break
            lista.append(entrada)
        except ValueError:
            print(f"Ha ocurrido un error:")

# Imprimir el contenido de la lista en mayúsculas
print("Contenido de la lista en mayúsculas:")
for item in lista:
    try:
        print(item.upper())
        # Si item no es una cadena, manejar el error
    except ValueError:
        print(f"Error al convertir '{item}' a mayúsculas:")