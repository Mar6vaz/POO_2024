#CLASE PARA LOS AUTOS
from conexionBd import obtener_conexion
from funciones import *

class Autos:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif


        #FUNCIONES PARA LOS AUTOS
    
    def insertar(self):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO autos (matricula, marca, modelo, color, nif) VALUES (%s, %s, %s, %s, %s)", 
                (self.matricula, self.marca, self.modelo, self.color, self.nif)
            )
            conexion.commit()
            limpiarPantalla()
            print("Auto agregado exitosamente.")
        except Exception as e:
            limpiarPantalla()
            print(f"Ocurrió un error al agregar un auto: {e}")  # Muestra el mensaje de error
        finally:
            cursor.close()
            conexion.close()



    def consultar(self):
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("select * from autos")
            for (matricula, marca, modelo, color, nif) in cursor: #iterar para imprimir bonito
                print("")
                print(f"Matricula: {matricula}\n Modelo: {modelo} \n Color: {color} \n NIF Cliente: {nif} ")
            cursor.close()
            conexion.close()
        else:
            print("No se pudo establecer la conexión a la base de datos.")



    def actualizar(self, auto):
        # Verificar si el empleado existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            
            # Mostrar el auto que eligió
            cursor.execute("SELECT * FROM autos WHERE matricula = %s", (auto,))
            resultado = cursor.fetchone() #una fila de datos en una tupla

            if not resultado:
                limpiarPantalla()
                print(f"No existe el auto con la matricula {auto}.")
            else:
            
                matricula_actual, marca_actual, modelo_actual, color_actual, nif_actual = resultado
            
                # Solicitar nuevos datos
                limpiarPantalla()
                print("Presione Enter para dejar sin cambios")
                marca = input(f"Marca ({marca_actual}): ") or marca_actual
                modelo = input(f"Modelo ({modelo_actual}): ") or modelo_actual
                color = input(f"Color ({color_actual}): ") or color_actual
                nif = input(f"NIF ({nif_actual}): ") or nif_actual

                cursor.execute("""
                    UPDATE autos
                    SET  marca = %s, modelo = %s, color = %s, nif = %s
                    WHERE matricula = %s
                """, (marca, modelo, color, nif, auto))
                
                conexion.commit()
                limpiarPantalla()
                print(f"Registros del auto con matricula {auto} actualizados correctamente.")
                
        except Exception as e:
            limpiarPantalla()
            print(f"Ocurrió un error al actualizar los registros del auto: {e}") #pipipipi
        finally:
            if conexion:
                cursor.close()
                conexion.close() #cierra todo, es buena practica mana
            



    def eliminar(self, matricula):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Verificar si el auto existe
            cursor.execute("SELECT COUNT(*) FROM autos WHERE matricula = %s", (matricula,))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                print(f"No existe el auto con la matricula {matricula}.")
            else:
                # Confirmar la eliminación
                seguri = True  # Salida segura para no usar break
                while seguri:
                    respuesta = input("¿Seguro que quiere eliminar el registro de este auto? (sí/no): ").upper()
                    if respuesta in ['SI', 'YES', 'S']:
                        # Proceder a eliminar
                        cursor.execute("DELETE FROM autos WHERE matricula = %s", (matricula,))
                        conexion.commit()
                        limpiarPantalla()
                        print(f"Registro de auto con matricula {matricula} eliminada correctamente.")
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


