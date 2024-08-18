#CLASES PARA LOS EMPLEADOS

from conexion import crear_conexion, cerrar_conexion
from funciones import *

class Empleados:
    def __init__(self, id, nombre, puesto, salario):
        self.__id = id
        self.__nombre = nombre
        self.puesto = puesto          #2 privadas y 2 publicas para practicar
        self.salario = salario

    # GETTER Y SETTER
    def getIdentificador(self): #nomas get porque si le hechas set modificas algo inmodificable como una id
        return self.__identificador

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre


    # FUNCIONES DE LOS EMPLEADOS
    def crear_empleado(self, nombre, puesto, salario):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
        valores = (nombre, puesto, salario)
        cursor.execute(query, valores)
        conexion.commit()
        print("Empleado creado exitosamente")

    def leer_empleados(self):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        query = "SELECT * FROM empleados"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]}")

    def actualizar_empleado(self, id, nombre, puesto, salario):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
        valores = (nombre, puesto, salario, id)
        cursor.execute(query, valores)
        conexion.commit()
        print("Empleado actualizado exitosamente")

    def eliminar_empleado(self, id):
        conexion = crear_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM empleados WHERE id = %s"
        valor = (id,)
        cursor.execute(query, valor)
        conexion.commit()
        print("Empleado eliminado exitosamente")
