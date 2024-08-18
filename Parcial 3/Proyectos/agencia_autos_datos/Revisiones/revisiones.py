#CLASES PARA REVISIONES
from conexionBd import obtener_conexion
from funciones import *

class Revisiones:
    def __init__( self, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otro, matricula):
        self.no_revision = no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otro = otro
        self.matricula = matricula


    #FUNCIONES PARA LOS AUTOS

    def insertar(self):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO revisiones (cambiofiltro, cambioaceite, cambiofrenos, otros, matricula) VALUES (%s, %s, %s, %s, %s)", 
                (self.no_revision, self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otro, self.matricula)
            )
            conexion.commit()
            limpiarPantalla()
            print("Revision agregada exitosamente.")
        except Exception as e:
            limpiarPantalla()
            print(f"Ocurrió un error al agregar las revisiones: {e}")  # Muestra el mensaje de error
        finally:
            cursor.close()
            conexion.close()



    def consultar(self):
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("select * from revisiones")
            for (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otro, matricula) in cursor: #iterar para imprimir bonito
                print("")
                print(f"Número de revision: {no_revision}\n Cambio filtro: {cambiofiltro} \n Cambio aceite: {cambioaceite} \n Cambio frenos: {cambiofrenos} \n Otros: {otro}\n Matricula: {matricula}")
            cursor.close()
            conexion.close()
        else:
            print("No se pudo establecer la conexión a la base de datos.")



    def actualizar(self, revision):
        # Verificar si el empleado existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            
            # Mostrar el auto que eligió
            cursor.execute("SELECT * FROM revicion WHERE no_revision = %s", (revision,))
            resultado = cursor.fetchone() #una fila de datos en una tupla

            if not resultado:
                limpiarPantalla()
                print(f"No existe la revision con el número {revision}.")
            else:
            
                cambiofiltro_actual, cambioaceite_actual, cambiofrenos_actual, otro_actual, matricula_actual = resultado[1:]
            
                # Solicitar nuevos datos
                limpiarPantalla()
                print("Presione Enter para dejar sin cambios")
                cambiofiltro = input(f"Cambio filtro ({cambiofiltro_actual}): ") or cambiofiltro_actual
                cambioaceite = input(f"Cambio aceite ({cambioaceite_actual}): ") or cambioaceite_actual
                cambiofrenos = input(f"Cambio frenos ({cambiofrenos_actual}): ") or cambiofrenos_actual
                otro = input(f"Otros:({otro_actual}): ") or otro_actual
                matricula = input(f"Matricula ({matricula_actual}): ") or matricula_actual

                cursor.execute("""
                    UPDATE autos
                    SET  cambiofiltro = %s, cambioaceite = %s, cambiofrenos = %s, otros = %s, matricula = %s
                    WHERE no_revision = %s
                """, (cambiofiltro, cambioaceite, cambiofrenos, otro, matricula, revision))
                
                conexion.commit()
                limpiarPantalla()
                print(f"Registros la recvision con numero {revision} actualizados correctamente.")
                
        except Exception as e:
            limpiarPantalla()
            print(f"Ocurrió un error al actualizar llas revisiones: {e}") #pipipipi
        finally:
            if conexion:
                cursor.close()
                conexion.close() #cierra todo, es buena practica mana
            



    def eliminar(self, revision):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Verificar si el auto existe
            cursor.execute("SELECT COUNT(*) FROM revisiones WHERE no_revision = %s", (revision,))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                print(f"No existe la revisión con el número {revision}.")
            else:
                # Confirmar la eliminación
                seguri = True  # Salida segura para no usar break
                while seguri:
                    respuesta = input("¿Seguro que quiere eliminar la revision? (sí/no): ").upper()
                    if respuesta in ['SI', 'YES', 'S']:
                        # Proceder a eliminar
                        cursor.execute("DELETE FROM revisiones WHERE no_revision = %s", (revision,))
                        conexion.commit()
                        limpiarPantalla()
                        print(f"Revision de auto con número {revision} eliminada correctamente.")
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


