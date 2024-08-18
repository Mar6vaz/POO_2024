# ARCHIVO CON LA CONEXION A MYSQL EN PYTHON 
import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='agencia_autos_datos',
            
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

#Crea la conexion dentro de una funcion y si la conexion fue exitosa returnea 'conexion' para usarlo en otros archivos