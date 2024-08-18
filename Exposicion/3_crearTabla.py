import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='inventario_productos'
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")
    print("Ocurrió un problema con el servidor... por favor intenta más tarde")
else:
    # Crear una tabla dentro de una BD existente
    sql = """
    CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        descripcion MEDIUMTEXT,
        precio DECIMAL(10, 2) NOT NULL,
        cantidad INT NOT NULL,
        categoria VARCHAR(100)
    )
    """
    micursor = conexion.cursor()
    try:
        micursor.execute(sql)
        print("Se creó la tabla 'productos' con éxito")
    except mysql.connector.Error as err:
        print(f"Error al crear la tabla: {err}")
    finally:
        micursor.close()
        conexion.close()