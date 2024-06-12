# crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#   imprimir la información

# Definir la lista con el contenido de la tabla
tabla_lista = [
    ["ACCION", "TERROR", "DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

# Crear un diccionario a partir de la lista
tabla_diccionario = {}
try:
    # Obtener los encabezados de la tabla
    encabezados = tabla_lista[0]
    
    # Inicializar las listas en el diccionario
    for encabezado in encabezados:
        tabla_diccionario[encabezado] = []
    
    # Llenar el diccionario con los datos de la tabla
    for fila in tabla_lista[1:]:
        for i, valor in enumerate(fila):
            tabla_diccionario[encabezados[i]].append(valor)
except ValueError:
    print(f"Ha ocurrido un error al crear el diccionario: ")

# Imprimir la información de la lista
print("Contenido de la lista:")
try:
    for fila in tabla_lista:
        print(fila)
except:
    print(f"Ha ocurrido un error al imprimir la lista: ")

# Imprimir la información del diccionario
print("\nContenido del diccionario:")
try:
    for clave, valores in tabla_diccionario.items():
        print(f"{clave}: {valores}")
        
except ValueError:
    print(f"Ha ocurrido un error al imprimir el diccionario: ")