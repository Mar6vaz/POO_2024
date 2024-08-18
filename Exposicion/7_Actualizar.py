from conexionBD import *

try:
    micursor = conexion.cursor()

   
    sql = "UPDATE productos SET precio = %s, cantidad = %s WHERE id = %s"

    nuevo_precio= 1600
    nuevo_cantidad=11
    product_id = 11

    micursor.execute(sql, ( nuevo_precio, nuevo_cantidad, product_id,))
    conexion.commit()

except Exception as e:
    print(f"Error: {e}")
    print("Ocurrió un problema con el servidor... por favor intenta más tarde")

else:
    print("Registro actualizado")

