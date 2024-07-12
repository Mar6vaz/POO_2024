import mysql.connector
try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
)
#Conectar con la BD MySQL

except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un problema con el servidor... por favor intenta mas tarde")
#verificar la conexion a la BD
else:
     print(f"Se creo la conexion con la BD exitosamente")
   