from conexionBD import* 

try: 
    micursor= conexion.cursor()

    sql= "DELATE FROM productos WHERE id = %s"
    product_id= 10 

    micursor.execute(sql, (product_id))
    conexion.commit()
except Exception as e:
    print(f"Error: {e}")
    print("Ocurrió un problema con el servidor... por favor intenta más tarde")

else: 
    print("Registro eliminado correctamente")

finally: 
    micursor.close()
    conexion.close()


    
  

