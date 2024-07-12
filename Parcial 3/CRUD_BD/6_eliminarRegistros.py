from conexionBD2 import *
try:
 
 micursor=conexion.cursor()
 sql="delete from clientes where id=1"

 micursor.execute(sql)
 conexion.commit()

except:
 
 print(f"Ocurrio un problema con el servidor... por favor intenta mas tarde")
else:  
 print(f"Registro Insertado Correctamente")
