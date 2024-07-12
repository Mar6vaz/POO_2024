from conexionBD2 import *
try:
 micursor=conexion.cursor()

 sql="update clientes set tel='6181112233' where id='4'"
 micursor.execute(sql)
 conexion.commit()


except:
 print(f"Ocurrio un problema con el servidor... por favor intenta mas tarde")
else:  
 print(f"Registro Insertado Correctamente")
