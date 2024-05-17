#El for es una estructura de control repetitiva o ciclica que funciona con interaciones X veces de acuerto a los valores numericos enteros que contenga 

#Sintaxi:

#for variable in elemento_interable(list, range, etc.):
#     bloque instrucciones

#Ejemplo 1 Crea r un programa que imprima 5 veces el caracter @ 

for contador in range(1,6):
    print("@")

#Ejemplo 2 Crea r un programa que imprima los numeros del 1 al 5 los sume e imprima la suma al final

suma=0
contador=1
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
print(f"La suma es: {suma}")


#Ejemplo 3 crear un programa que solicite un numero y apartir de este numero genere e imprima la tabla de multiplicar correspondiente 

numero=int(input("Ingrese un numero: "))

multi=0
i=1
while i<=10:
    multi=numero*i
    print(f"{numero} x {i} = {multi}")
    i+=1
