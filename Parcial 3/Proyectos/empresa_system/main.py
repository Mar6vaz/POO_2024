import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='mi_empresa',
            user='root',
            password=''
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

def crear_empleado(conexion, nombre, puesto, salario):
    cursor = conexion.cursor()
    query = "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)"
    valores = (nombre, puesto, salario)
    cursor.execute(query, valores)
    conexion.commit()
    print("Empleado creado exitosamente")

def leer_empleados(conexion):
    cursor = conexion.cursor()
    query = "SELECT * FROM empleados"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]}")

def actualizar_empleado(conexion, id, nombre, puesto, salario):
    cursor = conexion.cursor()
    query = "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s"
    valores = (nombre, puesto, salario, id)
    cursor.execute(query, valores)
    conexion.commit()
    print("Empleado actualizado exitosamente")

def eliminar_empleado(conexion, id):
    cursor = conexion.cursor()
    query = "DELETE FROM empleados WHERE id = %s"
    valor = (id,)
    cursor.execute(query, valor)
    conexion.commit()
    print("Empleado eliminado exitosamente")

def menu():
    conexion = crear_conexion()
    if conexion:
        while True:
            print("\n--- Menú de Opciones ---")
            print("1. Crear empleado")
            print("2. Leer empleados")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                nombre = input("Nombre: ")
                puesto = input("Puesto: ")
                salario = input("Salario: ")
                crear_empleado(conexion, nombre, puesto, salario)
            elif opcion == '2':
                leer_empleados(conexion)
            elif opcion == '3':
                id = input("ID del empleado a actualizar: ")
                nombre = input("Nuevo nombre: ")
                puesto = input("Nuevo puesto: ")
                salario = input("Nuevo salario: ")
                actualizar_empleado(conexion, id, nombre, puesto, salario)
            elif opcion == '4':
                id = input("ID del empleado a eliminar: ")
                eliminar_empleado(conexion, id)
            elif opcion == '5':
                cerrar_conexion(conexion)
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if _name_ == "_main_":
    menu()