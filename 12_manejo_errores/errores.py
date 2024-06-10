#Los errores de ejecuciuon en un lenguaje de programacion se precentan cuando existe una anomalia dentro de la ejcucion del codogo lo cual provoca 
#que se detenga la ejecucion del SW con el control y manejo de expreciones sera posible minimizar o evitar la interrupcion del programa devido a una exepcion 

#Ejemplo uno cuando una variable no se genera

# try:
#     nombre=input("Introduce el nombre completo de una persona: ")
#     if len(nombre)>0:

#      nombre_usuario="El nombre del completo del usuario es: "+nombre
#      print(nombre_usuario)

# except:
#     print("Es necesario introducir un nombre de usuario...verifica porfavor")


#Ejemplo 2 cuando se solicita un numero y se ingresa otra cosa 

# try:
#     numero=int(input("Ingres un numero entero:"))
#     if numero>0:
#        print("Soy un numero entero positivo")
#     elif numero==0:
#       print("Soy un numero entero neutro")
#     else:
#        print("Soy un numero negativi positivo")    
# except ValueError:
#     print("Introduce un numero porfavor")  


#Ejemplo 3 cuando se generan multiples exepciones 
try:
    numero=int(input("Introduce un numero: "))

    print("El cuadrado del numero es: "+str(numero*numero)) 
except ValueError:
    print("Introduce un valor numerico entero")
except TypeError:
    print("Se deve convertir el numero a entero")

else:
    print("No se precentaron errores de ejecucion")
finally:
    print("Termine la ejecicion ")

