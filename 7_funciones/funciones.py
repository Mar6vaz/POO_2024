
#Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple un funcion especifica. La funcion se puede reutilizar con sinple escho de invocarla es decir mandarla llamar

#Sintaxis

#def nombredeMifuncion(parametros):
    #bloque o conjunto de instrucciones 

#nombredeMifuncion(parametros)

#La funcion puede ser de 4 tipos 

#1.-Funcion que no recibe parametros y no regresa valor 
#2.-Funcion que no recibe parametros y regresa valor 
#3.-Funcion que recibe parametros y no regresa valor 
#4.-Funcion que recibe parametros y regresa valor


#Ejercicio 1: Crear un funcion para imprimir nombres de personas 
#1.-Funcion que no recibe parametros y no regresa valor
def solicitarNombre():
    nombre=input("Ingresa el nombre completo: ")

solicitarNombre()
#Ejemplo 2 suma dos numeros 

def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()

#Ejepmos 3 sumar dos numeros 
#2.-Funcion que no recibe parametros y regresa valor 
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma 

resultado_suma=suma()
print(f"La suma es: {resultado_suma}")

#Ejepmos 4 sumar dos numeros 
#3.-Funcion que recibe parametros y no regresa valor 
def suma(n1,n2):
    suma=n1+n2
    print(f"La suma es: {suma}")

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Ejepmos 5 sumar dos numeros 
#4.-Funcion que recibe parametros y regresa valor
def suma(n1,n2):
    suma=n1+n2
    return suma 

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
rssultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")

#Ejemplo 6 Crear un programa que solicite atraves de un funcion la siguinte informacio: Nombre del paciente, edad, estatura, Tipo de sangre. Utilizar los cuatro tipos de funcion

#1.-Funcion que no recibe parametros y no regresa valor
def solicitar_informacion_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    estatura = float(input("Ingrese la estatura del paciente (en metros): "))
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
    mostrar_informacion_paciente(nombre, edad, estatura, tipo_sangre)

# Función que recibe parámetros y no regresa valor
def mostrar_informacion_paciente(nombre, edad, estatura, tipo_sangre):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Estatura: {estatura} metros")
    print(f"Tipo de Sangre: {tipo_sangre}")

# Función que no recibe parámetros y regresa valor
def obtener_informacion_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    estatura = float(input("Ingrese la estatura del paciente (en metros): "))
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
    return nombre, edad, estatura, tipo_sangre

# Función que recibe parámetros y regresa valor
def crear_resumen_paciente(nombre, edad, estatura, tipo_sangre):
    resumen = f"Paciente {nombre}, de {edad} años, con estatura de {estatura} metros y tipo de sangre {tipo_sangre}."
    return resumen

# Usar la función que no recibe parámetros y no regresa valor
solicitar_informacion_paciente()

# Usar la función que no recibe parámetros y regresa valor
nombre, edad, estatura, tipo_sangre = obtener_informacion_paciente()


