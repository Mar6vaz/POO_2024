import mysql.connector


try: 

#Conectar con la BD MySQL
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_python'
    )

except Exception as e:
    print(f"Error: {e}")
    print(f"tipo error: {type(e).name}")
    print(f"Ocurrio un problema con el servidor...porfavor intentalo mas tarde...")

else:
# verificar la conexion a la BD
    print(f"Se creo la conexion con la BD exitosamente")