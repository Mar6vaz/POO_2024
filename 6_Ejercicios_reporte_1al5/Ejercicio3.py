# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

#Utilizando un bucle while
contador = 1
while contador <= 60:
    cuadrado = contador ** 2
    print("El cuadrado de", contador, "es:", cuadrado)
    contador += 1

    

# Utilizando un bucle for
for contador in range(1, 61):
    cuadrado = contador ** 2
    print("El cuadrado de", contador, "es:", cuadrado)