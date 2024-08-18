#CONEXION MYSQL EN PITÓN
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
            #print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
#La funcion crea la conexion asi es mas facil usarlo, y returnea 'conexion'

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        #print("Conexión cerrada") #se ve feo si lo imprimes




