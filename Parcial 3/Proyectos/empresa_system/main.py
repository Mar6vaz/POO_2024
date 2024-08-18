#AQUI SE ENCUENTRA EL MENU 
#parece ser mas corto, solo gestiona empleados
#PROGRAMACION SECUENCIAL MODULAR ERA HACE RATO

from Empleados import empleados
from funciones import *
from conexion import crear_conexion, cerrar_conexion

def menu():
    conexion = crear_conexion()
    if conexion:
        while True:
            limpiarPantalla()
            print("\n--- Menú de Opciones ---")
            print("1. Crear empleado")
            print("2. Leer empleados")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("5. Salir")
            opcion = input("Elige una opción: ").upper()

            if opcion == '1' or opcion == 'CREAR':
                limpiarPantalla()
                nombre = input("Nombre: ")
                puesto = input("Puesto: ")
                salario = input("Salario: ")
                #crear instancia de la clase empleados
                obj_empleado=empleados.Empleados(None, None, None, None)
                obj_empleado.crear_empleado(nombre, puesto, salario)
                esperarTecla() #perimite que el usuario lea todos los letreros, se van como rayo makuin y no los lee


            elif opcion == '2' or opcion == 'LEER':
                limpiarPantalla()
                #crear instancia de la clase empleados
                obj_empleado=empleados.Empleados(None, None, None, None)
                obj_empleado.leer_empleados()
                esperarTecla() 


            elif opcion == '3' or opcion == 'ACTUALIZAR':
                limpiarPantalla()
                id = input("ID del empleado a actualizar: ")
                nombre = input("Nuevo nombre: ")
                puesto = input("Nuevo puesto: ")
                salario = input("Nuevo salario: ")
                #crear instancia de la clase empleados
                obj_empleado=empleados.Empleados(None, None, None, None)
                obj_empleado.actualizar_empleado(id, nombre, puesto, salario)
                esperarTecla()

            elif opcion == '4' or opcion == 'ELIMINAR':
                limpiarPantalla()
                id = input("ID del empleado a eliminar: ")
                #crear instancia de la clase empleados
                obj_empleado=empleados.Empleados(None, None, None, None)
                obj_empleado.eliminar_empleado(id)
                esperarTecla()

            elif opcion == '5':
                limpiarPantalla()
                print("Haz salido del programa")
                cerrar_conexion(conexion)
                break #sale del bucle

            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__": #esto le dice al python que ejecute primero ese (si es que hay mas funciones aqui)
    menu()