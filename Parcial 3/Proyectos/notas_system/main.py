from usuarios import usuario
from notas import nota
import getpass
from funciones import *

def menu_principal():
    while True:    
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellidos=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            #Agregar codigo
            obj_usurio=usuario.Usuario(nombre,apellidos,email,password)
            resultado=obj_usurio.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...")  
            esperarTecla()      
        elif opcion == '2' or opcion=="LOGIN":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            #Agregar codigo 
            registro=usuario.Usuario.iniciar_sesion(email,password)
            if registro:
                menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")
                esperarTecla()    
        elif opcion == '3' or opcion=="SALIR":
            print("\n\t.. ¡Gracias Bye! ...")
            #opc=False
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Notas ::. 
                  1.- Crear 
                  2.- Mostrar
                  3.- Cambiar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="CREAR":
            borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            obj_nota=nota.Nota(usuario_id,titulo,descripcion)
            resultado=obj_nota.crear()
            if resultado:
                print(f"\n \t \t.::La Nota {titulo} se creo Correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible crear la nota ... vuelva a intentarlo **...") 
            esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            borrarPantalla()
            #Agregar codigo  
            registros=nota.Nota.mostrar(usuario_id)
            if len(registros)>0:
                print(f"\n\t {nombre} {apellidos}, tus notas son: ")
                num_notas=1
                for fila in registros:
                   print(f"\nNota: {num_notas} \nID: {fila[0]}.- Titulo: {fila[2]}         Fecha de Creación: {fila[4]} \nDescripción: {fila[3]}") 
                   num_notas+=1    
            else:
                print(f"\n \t \t** No existen notas para el usuario ... vuelva a intentarlo **...")
            esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            id = input("\t \t ID de la nota a actualizar: ")
            titulo = input("\t Nuevo título: ")
            descripcion = input("\t Nueva descripción: ")
            #Agregar codigo
            resultado=nota.Nota.actualizar(id,titulo,descripcion)
            if resultado:
                print(f"\n \t \t.::Nota Actualizada Correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible actualizar la nota ... vuelva a intentarlo **...")  
            esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            id = input("\t \t ID de la nota a eliminar: ")
            #Agregar codigo
            resultado=nota.Nota.eliminar(id)
            if resultado:
                print(f"\n \t \t.::Nota Eliminada Correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible eliminar la nota ... vuelva a intentarlo **...")  
            esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
  menu_principal()

