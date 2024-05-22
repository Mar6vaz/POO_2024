#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

inicio = int(input("Ingrese el primer número: "))


fin = int(input("Ingrese el segundo número: "))


if inicio < fin:
    
    print("Los números entre", inicio, "y", fin, "son:")
    for i in range(inicio, fin + 1):
        print(f"El siguiente numero es: {i}") 
else:
    print("El primer número debe ser menor que el segundo número.")