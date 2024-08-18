from conexionBD import* 

try: 
    micursor= conexion.cursor()

    sql = "SELECT nombre, descripcion, precio, categoria FROM productos "
    micursor.execute(sql)
    resultados= micursor. fetchall()

    if len(resultados) > 0:
        print(f"Registro de la tabla: {len(resultados)}")   
        for productos in resultados: 
            print(productos)
    else: 
        print("No hay registros en la tabla")

except Exception as e:
    print(f"Error: {e}")
    print("Ocurrió un problema con el servidor... por favor intenta más tarde")


else: 
    print("Registro insertado correctamente")

finally: 
    micursor.close()
    conexion.close()
  