#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

inicio= int(input("Ingrese el primer numero: "))
fin = int(input("Ingrese el segundo numero: "))

print("Números impares entre", inicio, "y", fin, "son:")

for num in range(inicio + 1, fin):
    if num % 2 != 0:
        print(num, end=" ")
    