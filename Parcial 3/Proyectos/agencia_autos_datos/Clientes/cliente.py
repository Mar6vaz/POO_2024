#CLASE PARA LOS CLIENTES
from conexionBd import obtener_conexion
from funciones import *

class Clientes:
    def __init__( self, nif, nombre, direccion, ciudad, tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel


    #FUNCIONES PARA CLIENTES

    def insertar(self):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO clientes (nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)", 
                (self.nif, self.nombre, self.direccion, self.ciudad, self.tel)
            )
            conexion.commit()
            limpiarPantalla()
            print("Cliente agregado exitosamente.")
        except Exception as e:
            limpiarPantalla()
            print(f"Ocurrió un error al agregar al cliente: {e}")  # Muestra el mensaje de error
        finally:
            cursor.close()
            conexion.close()
        

    def consultar(self):
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("select * from clientes")
            for (nif, nombre, direccion, ciudad, tel) in cursor: #iterar para imprimir bonito
                print("")
                print(f"NIF: {nif}\n Nombre: {nombre} \n Dirección: {direccion} \n Ciudad: {ciudad} \n Telefono: {tel}")
            cursor.close()
            conexion.close()
        else:
            print("No se pudo establecer la conexión a la base de datos.")



    def actualizar(self, cliente):
        # Verificar si el empleado existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            
            # Mostrar el cliente que eligió
            cursor.execute("SELECT * FROM clientes WHERE nif = %s", (cliente,))
            resultado = cursor.fetchone() #una fila de datos en una tupla

            if not resultado:
                limpiarPantalla()
                print(f"No existe el cliente con NIF {cliente}.")
            else:
                #evita la necesidad de acceder a los elementos por índice en el resto del código.
                nombre_actual, direccion_actual, ciudad_actual, telefono_actual = resultado[1:] #desglose del 1 hasta el final de la tupla
                #resultado[] es una subtupla con elementos especificos eeeeeh

                # Solicitar nuevos datos
                limpiarPantalla()
                print("Presione Enter para dejar sin cambios")
                nombre = input(f"Nombre ({nombre_actual}): ") or nombre_actual
                direccion = input(f"Dirección ({direccion_actual}): ") or direccion_actual
                ciudad = input(f"Ciudad ({ciudad_actual}): ") or ciudad_actual
                telefono = input(f"Teléfono ({telefono_actual}): ") or telefono_actual
                

                # Proceder a actualizar los detalles del cliente
                #AQUI VAMOOOS
                cursor.execute("""
                    UPDATE clientes
                    SET nombre = %s, direccion = %s, ciudad = %s, telefono = %s
                    WHERE nif = %s
                """, (nombre, direccion, ciudad, telefono, cliente))
                
                conexion.commit()
                limpiarPantalla()
                print(f"Datos del cliente con NIF {cliente} actualizados correctamente.")
                
        except Exception as e:
            limpiarPantalla()
            print(f"Ocurrió un error al actualizar los datos del cliente: {e}") #pipipipi
        finally:
            if conexion:
                cursor.close()
                conexion.close() #cierra todo, es buena practica mana


            
    def eliminar(self, nif):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Verificar si el cliente existe
            cursor.execute("SELECT COUNT(*) FROM clientes WHERE nif = %s", (nif,))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                print(f"No existe el cliente con NIF {nif}.")
            else:
                # Confirmar la eliminación
                seguri = True  # Salida segura para no usar break
                while seguri:
                    respuesta = input("¿Seguro que quiere eliminar el registro de este auto? (sí/no): ").upper()
                    if respuesta in ['SI', 'YES', 'S']:
                        # Proceder a eliminar
                        cursor.execute("DELETE FROM clientes WHERE nif = %s", (nif,))
                        conexion.commit()
                        limpiarPantalla()
                        print(f"Registro de cliente con NIF {nif} eliminada correctamente.")
                        seguri = False
                    elif respuesta in ['NO', 'NOPE', 'N']: #otra forma de condicionar, creo que es mejor 
                        print("Eliminación cancelada.")
                        seguri = False
                    else:
                        print("Opción no válida. Responda sí o no.")
        except:
            print("Ocurrió un error al eliminar el registro: ")
        finally:
            if conexion:
                cursor.close()
                conexion.close()
