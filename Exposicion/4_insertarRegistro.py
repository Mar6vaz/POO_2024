from conexionBD import *  # Asegúrate de que `conexionBD2` contiene la conexión a la base de datos

try:
    micursor = conexion.cursor()

    # Inserta un nuevo producto en la tabla productos
    sql = """
    INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria) 
    VALUES (%s, %s, %s, %s, %s)
    """
    valores = ('Laptop', 'Laptop de 15', 1500.99, 3, 'Electrónica')
    micursor.execute(sql, valores)

    # Es necesario para que al final se complete el execute(sql) y finalice la consulta SQL
    conexion.commit()

except Exception as e:
    print(f"Error: {e}")
    print("Ocurrió un problema con el servidor... por favor intenta más tarde")

else:
    print("Registro insertado correctamente")
finally:
    micursor.close()
    conexion.close()

    





 
