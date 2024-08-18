import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='inventario_productos'
    )
    print("Se creó la conexión con la BD exitosamente")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    print(f"Tipo de error: {type(err).__name__}")
    print("Ocurrió un problema con el servidor... por favor intenta más tarde")