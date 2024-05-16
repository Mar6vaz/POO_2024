#Convertir los tipos de datos

#Nota:Solo es posible en una concatenacion concatenar entre tipos de datos iguales

texto="Soy una cadena"
numero=23

print(texto)
print(numero)

print(texto+" y soy una cadena2")
print(numero+34)

#convertir un tipo de dato int a str
numero_str=str(numero)
print(texto+" "+numero_str)

#otra manera print(texto+""+str(numero)) mas comun
#ES LA MAS COMUN PARA MOSTRAR UNA CAdeNA CON UN NUMERO

#CONVERTIR UN STRING A INT
n1=33
suma=int('23')+n1
print("suma: "+str(suma))

#COnvertir UN FLOAT A INT
n1=33
n2=int(33.99)

suma=n1+n2
print(suma)

#CONVERTIR UN INT A FLOAT
n1=3
n2=4

suma=float(n1+n2)

print(f"La suma es: {suma}")
print("la suma es: "+str(suma))