import mysql.connector
from mysql.connector import Error
from conexionBD import conectar_bd
from datetime import datetime




class Agencias:
    def __init__(self, id, nombre, direccion, telefono, descripcion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.descripcion = descripcion


    @staticmethod
    def obtener_agencias():
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM agencias")  # Suponiendo que la tabla se llama 'agencias'
                resultados = cursor.fetchall()
                
                agencias = []
                for row in resultados:
                    agencia = Agencias(
                        id=row[0],
                        nombre=row[1],
                        direccion=row[2],
                        telefono=row[3],
                        descripcion=row[4]
                    )
                    agencias.append(agencia)
                
                return agencias

            except Exception as e:
                print(f"Error al consultar las agencias: {e}")
                return None
            finally:
                cursor.close()
                conexion.close()
        else:
            print("No se pudo establecer la conexión a la base de datos.")
            return None






class Citas:
    def __init__(self, id, fecha, id_cliente, id_empleado, id_solicitud, estado):
        self.id = id
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado
        self.id_solicitud = id_solicitud
        self.estado = estado

    @staticmethod
    def obtener_citas(cliente_id):
        conexion = conectar_bd()
        citas = []
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("""
                    SELECT id, fecha_cita, cliente_id, empleado_id, solicitud_id, estado 
                    FROM citas 
                    WHERE cliente_id = %s
                """, (cliente_id,))
                for row in cursor:
                    citas.append(Citas(*row))
            except Exception as e:
                print(f"Error al obtener citas: {e}")
            finally:
                cursor.close()
                conexion.close()
        return citas


    @staticmethod
    def actualizar_estado_cita(id_cita, nuevo_estado):
        conexion = conectar_bd()
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE citas SET estado = %s WHERE id = %s", (nuevo_estado, id_cita))
            conexion.commit()
            cursor.close()
        except Exception as e:
            print(f"Error al actualizar el estado de la cita: {e}")
        finally:
            if conexion:
                conexion.close()





class Servicios:
    def __init__(self, id_servicio, nombre, descripcion, empleado_id, agencia_id):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleado_id = empleado_id
        self.agencia_id = agencia_id



    @staticmethod
    def obtener_detalles_servicios():
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM servicios")
                detalles_servicios = []
                for (id_servicio, nombre, descripcion, empleado_id, agencia_id) in cursor:
                    detalles_servicios.append(f"ID: {id_servicio}\nNombre: {nombre}\nDescripción: {descripcion}\nProfesional a cargo: {empleado_id}\nAgencia: {agencia_id}\n")
                cursor.close()
            except Exception as e:
                detalles_servicios = [f"Error al recuperar datos: {e}"]
            finally:
                conexion.close()
        else:
            detalles_servicios = ["No se pudo establecer la conexión a la base de datos."]
        return detalles_servicios




# servicios.py

class Solicitudes:
    def __init__(self, servicio_id, empleado_id, cliente_id, agencia_id, fecha_solicitud, estado, documentos, comentarios):
        self.servicio_id = servicio_id
        self.empleado_id = empleado_id
        self.cliente_id = cliente_id
        self.agencia_id = agencia_id
        self.fecha_solicitud = fecha_solicitud
        self.estado = estado
        self.documentos = documentos
        self.comentarios = comentarios

    def insertar_solicitud(self):
        conexion = conectar_bd()  # Asegúrate de que esta función esté importada
        if conexion:
            try:
                cursor = conexion.cursor()
                query = """
                    INSERT INTO solicitudes
                    (servicio_id, empleado_id, cliente_id, agencia_id, fecha_solicitud, estado, documentos, comentarios)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (self.servicio_id, self.empleado_id, self.cliente_id, self.agencia_id, self.fecha_solicitud, self.estado, self.documentos, self.comentarios)
                cursor.execute(query, values)
                conexion.commit()
                cursor.close()
                conexion.close()
                return True
            except mysql.connector.Error as err:
                print(f"Error al insertar la solicitud: {err}")
                return False
        else:
            print("No se pudo conectar a la base de datos.")
            return False
