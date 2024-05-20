 #Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado


num1 = float(input("Ingrese el primer número: "))


num2 = float(input("Ingrese el segundo número: "))


suma = num1 + num2
print("Suma:", suma)


resta = num1 - num2
print("Resta:", resta)


multiplicacion = num1 * num2
print("Multiplicación:", multiplicacion)


if num2 != 0:
    division = num1 / num2
    print("División:", division)
else:
    print("No se puede dividir entre cero")