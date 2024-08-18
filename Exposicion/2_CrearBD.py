import mysql.connector

# Crear la conexión con la BD
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    # Verificar la conexión
    if conexion.is_connected():
        print("Se creó la conexión con éxito")
    else:
        print("No fue posible hacer la conexión")

    # Crear un objeto para ejecutar las instrucciones
    micursor = conexion.cursor()

    # Crear la BD desde Python
    sql = "CREATE DATABASE IF NOT EXISTS inventario_productos"
    micursor.execute(sql)

    # Verificar que se creó la BD
    if micursor:
        print("Se creó la BD exitosamente")

    # Mostrar las BD que existen en el servidor de MySQL
    micursor.execute("SHOW DATABASES")
    for db in micursor:
        print(db)

    # Usar la base de datos creada
    micursor.execute("USE inventario_productos")

    # Crear la tabla de productos
    sql_tabla = """
    CREATE TABLE IF NOT EXISTS productos (
        id INT(25) AUTO_INCREMENT NOT NULL,
        nombre VARCHAR(100) NOT NULL,
        descripcion MEDIUMTEXT,
        precio DECIMAL(10, 2) NOT NULL,
        cantidad INT NOT NULL,
        categoria VARCHAR(100),
        CONSTRAINT pk_productos PRIMARY KEY (id)
    ) ENGINE=InnoDB;
    """
    micursor.execute(sql_tabla)
    print("Tabla 'productos' creada exitosamente")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    print(f"Tipo de error: {type(err).__name__}")
    print("Ocurrió un problema con el servidor... por favor intenta más tarde")

finally:
    if conexion.is_connected():
        micursor.close()
        conexion.close()
        print("La conexión se ha cerrado")