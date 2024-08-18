# CLASES PARA VETERINARIA Y SUS SERVICIOS

from conexionBD import obtener_conexion
from funciones import *
from datetime import datetime, timedelta #es que porque pones agregar cita aqui mana
#timedelta es una clase de modulo datetime y representa una duracion o diferencias entre fechas y horas

class Veterinarias:
    def __init__(self, id_veterinaria, nombre, direccion, tel):
        self.__id_veterinaria = id_veterinaria
        self.__nombre = nombre
        self.__direccion = direccion
        self.__tel = tel

    # GETTER Y SETTER
    def getIdVeterinaria(self):
        return self.__id_veterinaria

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getTel(self):
        return self.__tel

    def setTel(self, tel):
        self.__tel = tel

    # FUNCIONES DE LA VETERINARIA
    def mostrar_detalles(self):
        # Código para mostrar detalles de la veterinaria
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM veterinarias")
            for (id_veterinaria, nombre, direccion, telefono) in cursor: #iterar para que se vea bonito
                print(f"ID: {id_veterinaria}\n Nombre: {nombre} \n Dirección: {direccion} \n Teléfono: {telefono}")
                print(" ")
            cursor.close()
            conexion.close()
        else:
            print("No se pudo establecer la conexión a la base de datos.")


    def actualizar_detalles(self, id_veterinaria):
        # Verificar si la veterinaria existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM veterinarias WHERE id = %s", (id_veterinaria,))
            veterinaria = cursor.fetchone()

            if not veterinaria:
                limpiarPantalla()
                print(f"No existe una veterinaria con el ID {id_veterinaria}.")
            else:
                limpiarPantalla()
                #evita la necesidad de acceder a los elementos por índice en el resto del código.
                nombre_actual, direccion_actual, telefono_actual = veterinaria[1:]

                # Solicitar nuevos datos
                print("Presione Enter para dejar sin cambios")
                nombre = input(f"Nombre ({nombre_actual}): ") or nombre_actual
                direccion = input(f"Dirección ({direccion_actual}): ") or direccion_actual
                telefono = input(f"Teléfono ({telefono_actual}): ") or telefono_actual

                # Actualizar los detalles de la veterinaria
                cursor.execute("""
                    UPDATE veterinarias
                    SET nombre = %s, direccion = %s, telefono = %s
                    WHERE id = %s
                """, (nombre or veterinaria[1], direccion or veterinaria[2], telefono or veterinaria[3], id_veterinaria))
                conexion.commit()
                limpiarPantalla()
                print(f"Datos de la veterinaria con ID {id_veterinaria} actualizados correctamente.")
                
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        finally:
            if conexion:
                cursor.close()
                conexion.close()
            

    

    def agregar_cliente(self, nombre, direccion, telefono, tipo):
        # Código para agregar un cliente a la veterinaria
        conexion = obtener_conexion()
        try:
            if conexion:
                cursor=conexion.cursor()
                # Insertar el nuevo cliente en la base de datos
                cursor.execute(
                    "INSERT INTO clientes (nombre, direccion, telefono, tipo) VALUES (%s, %s, %s, %s)",
                    (nombre, direccion, telefono, tipo)
                )
                # Obtener el ID del cliente recién agregado
                conexion.commit()
                cliente_id = cursor.lastrowid  # Obtener el ID del último registro insertado
                print(f"Cliente agregado con éxito con ID: {cliente_id}")
                return cliente_id
            else:
                    limpiarPantalla()
                    print("No se pudo establecer la conexión a la base de datos.")
                    return None

        except:
            print("Error al agregar el cliente: ")
            return None
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()


    def agregar_servicio(self, nombre, descripcion, costo, id_veterinaria):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Verificar si la veterinaria existe
            cursor.execute("SELECT COUNT(*) FROM veterinarias WHERE id = %s", (id_veterinaria,))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                print(f"No existe la veterinaria con el ID {id_veterinaria}.")
                return  # Salir de la función si la veterinaria no existe

            # Validar que el costo sea un número positivo
            while True:
                try:
                    costo = float(costo)  # Convertir el costo a un número flotante
                    if costo <= 0:
                        print("El costo debe ser un número positivo.")
                        costo = input("Ingrese un costo válido: ")  # Solicitar nuevamente el costo
                    else:
                        break  # Salir del bucle si el costo es válido
                except ValueError:
                    print("El costo debe ser un número válido.")
                    costo = input("Ingrese un costo válido: ")  # Solicitar nuevamente el costo

            # Insertar el nuevo servicio
            cursor.execute(
                "INSERT INTO servicios (nombre, descripcion, costo, veterinaria_id) VALUES (%s, %s, %s, %s)",
                (nombre, descripcion, costo, id_veterinaria)
            )
            conexion.commit()
            print(f"Servicio '{nombre}' agregado correctamente.")

        except Exception as e:
            print(f"Error al agregar el servicio: {e}")
        
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def eliminar_servicio(self, id_servicio):
        # Verificar si el servicio existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Mostrar el servicio que eligió
            cursor.execute("SELECT nombre FROM servicios WHERE id = %s", (id_servicio,)) 
            resultado = cursor.fetchone()

            if not resultado:
                print(f"No existe el servicio con el ID {id_servicio}.")
            else:
                # Proceder a eliminar el servicio encontrado
                nombre_servicio = resultado[0]  # En esta posición está el nombre del servicio
                seguri = True
                while seguri:
                    respuesta = input(f"¿Seguro que quiere eliminar '{nombre_servicio}'? (si/no): ").upper()
                    if respuesta in ['SI', 'YES', 'SIMON']:
                        # Proceder a eliminar
                        cursor.execute("DELETE FROM servicios WHERE id = %s", (id_servicio,))
                        conexion.commit()
                        print(f"Servicio '{nombre_servicio}' eliminado correctamente.")
                        seguri = False
                    else:
                        seguri = False       
        except Exception as e:
            print(f"Ocurrió un error al verificar la existencia del servicio: {e}")
        finally:
            if conexion:
                cursor.close()
                conexion.close()


        

    def eliminar_empleado(self, id_empleado):
        # Verificar si el empleado existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            
            # Mostrar el empleado que eligió
            cursor.execute("SELECT COUNT(*) FROM empleados WHERE id = %s", (id_empleado,))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                limpiarPantalla()
                print(f"No existe el empleado con el ID {id_empleado}.")
            else:
                # Confirmar la eliminación
                seguri = True
                while seguri:
                    respuesta = input("¿Seguro que quiere eliminar a este empleado? (SI/NO) ").strip().upper()
                    if respuesta=='SI' or respuesta=='YES' or respuesta=='SIMON':
                        # Proceder a eliminar
                        cursor.execute("""
                            DELETE FROM empleados
                            WHERE id = %s
                        """, (id_empleado,))
                        conexion.commit()
                        limpiarPantalla()
                        print(f"Empleado con ID {id_empleado} eliminado correctamente.")
                        seguri = False
                    elif respuesta in ['NO', 'N']: #otra forma de condicionar respuestas
                        print("Eliminación cancelada.")
                        seguri = False
                    else:
                        print("Respuesta no válida. Por favor, responda con 'SI' o 'NO'.")
                        
        except Exception as e:
            limpiarPantalla()
            print(f"Ocurrió un error al eliminar el empleado: {e}")
        finally:
            if conexion:
                cursor.close()
                conexion.close()


            
    def agregar_empleado(self, nombre, direccion, telefono, puesto, salario, id_veterinaria):
        # Verificar si la veterinaria existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()

            # Verificar si la veterinaria existe
            cursor.execute("SELECT COUNT(*) FROM veterinarias WHERE id = %s", (id_veterinaria,))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                limpiarPantalla()
                print(f"No existe la veterinaria con ID {id_veterinaria}.")
                return

            # Agregar el empleado
            cursor.execute(
                "INSERT INTO empleados (nombre, direccion, telefono, puesto, salario, veterinaria_id) VALUES (%s, %s, %s, %s, %s, %s)",
                (nombre, direccion, telefono, puesto, salario, id_veterinaria)
            )
            conexion.commit()
            limpiarPantalla()
            print(f"Empleado '{nombre}' agregado correctamente a la veterinaria con ID {id_veterinaria}.")
        except Exception as e:
            limpiarPantalla()
            print(f"Error al agregar el empleado: {e}")
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def eliminar_cliente(self, id_cliente):
        conexion = obtener_conexion()
        cursor = None
        try:
            if conexion:
                cursor = conexion.cursor()
                # Verificar si el cliente existe
                cursor.execute("SELECT COUNT(*) FROM clientes WHERE id = %s", (id_cliente,))
                resultado = cursor.fetchone()

                if resultado[0] == 0:
                    print(f"No existe el cliente con el ID {id_cliente}.")
                else:
                    # Confirmar eliminación
                    respuesta = input("¿Seguro que quiere eliminar a este cliente? (si/no): ").lower()
                    if respuesta in ('si', 'yes', 's'): #condicion mucho mejor
                        # Eliminar cliente
                        cursor.execute("""
                            DELETE FROM clientes 
                            WHERE id = %s
                        """, (id_cliente,))
                        conexion.commit()
                        print(f"Cliente con ID {id_cliente} eliminado correctamente.")
                    else:
                        print("No se logró eliminar al cliente.")
                        
        except:
            print(f"Ocurrió un error al eliminar el cliente: ")
            
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

        
         
      


class Citas:
    def __init__(self, id_cita, id_cliente, id_animal, id_empleado, id_servicio, estado):
        self.__id_cita = id_cita
        self.__id_cliente = id_cliente
        self.__id_animal = id_animal
        self.__id_empleado = id_empleado
        self.__id_servicio = id_servicio
        self.estado=estado

    # METODOS GET PARA ACCEDER A ELLOS
    @property
    def id_cita(self):
        return self.__id_cita

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def id_animal(self):
        return self.__id_animal

    @property
    def id_empleado(self):
        return self.__id_empleado

    @property
    def id_servicio(self):
        return self.__id_servicio

    # FUNCIONES DE LAS CITAS
    def confirmar(self, id_cita):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Verificar si la cita existe
            cursor.execute("SELECT COUNT(*) FROM citas WHERE id = %s", (id_cita,))
            resultado = cursor.fetchone() #guardar el resultado en una tupla

            if resultado[0] == 0:
                print(f"Lo sentimos... esta cita no se ha programado.")
            else:
                respuesta = input("¿Seguro que confirmará esta cita? (si/no): ").upper()
                if respuesta in ['SI', 'YES', 'S']:  # Condición mejorada
                    cursor.execute(
                        "UPDATE citas SET estado = %s WHERE id = %s", 
                        ('Confirmada', id_cita)
                    )
                    conexion.commit()
                    limpiarPantalla()
                    print(f"Cita con ID {id_cita} confirmada.")
                    
                    # Obtener y mostrar la fecha de la cita
                    cursor.execute("SELECT fecha FROM citas WHERE id = %s", (id_cita,))
                    fecha = cursor.fetchone()
                    
                    if fecha:
                        fecha_formateada = fecha[0]  # Extrae la fecha de la tupla
                        print(f"Cita confirmada para el {fecha_formateada}.")
                    else:
                        print("No se pudo recuperar la fecha de la cita.")
                else:
                    limpiarPantalla()
                    print("La confirmación ha sido cancelada.")
        except Exception as e:
            limpiarPantalla()
            print(f"Error al confirmar la cita: {e}")
        finally:
            if conexion:
                cursor.close()
                conexion.close()


    

    def programar_cita(self, id_cliente, id_animal, id_empleado, id_servicio):
        # Obtener la fecha y hora actuales y agregar 2 días
        fecha_programada = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")
        #datetime.now Obtiene la fecha y hora actuales del sistema
        # despues rea un objeto timedelta que representa un intervalo de 2 días de diferencia a ahora
        #timedelta se utiliza para sumar o restar tiempos como fechas o las horas, segundos, etc.abs
        #datetime.now() + timedelta(days=2) suma 2 fechas más a hoy, o mas bien a la hora que se programe la cita
        #.strftime("%Y-%m-%d") Convierte el objeto datetime resultante en una cadena de texto (string) con un formato específico.
        #esto convertirá 2024-08-05 14:30:00 en 2024-08-05
        #aprendi algo nuevo hoooooy
        
        # Conexión a la base de datos
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Insertar datos en la base de datos
            cursor.execute("""
                INSERT INTO citas (fecha, servicio_id, cliente_id, empleado_id, animal_id, estado)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (fecha_programada, id_servicio, id_cliente, id_empleado, id_animal, 'Programada'))
            conexion.commit()
            print("Cita agregada correctamente.")
        except Exception as e:
            limpiarPantalla()
            print(f"Error al agregar la cita: {e}")
        finally:
            if conexion:
                cursor.close()
                conexion.close()



    def cancelar_cita(self, id_cita):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Verificar si la cita existe
            cursor.execute("SELECT COUNT(*) FROM citas WHERE id = %s", (id_cita,))
            resultado = cursor.fetchone() #guardar el resultado en una tupla

            if resultado[0] == 0:
                print(f"Lo sentimos... esta cita no se ha programado.")
            else:
                respuesta = input("¿Seguro que cancelará esta cita? (si/no): ").upper() #convierte en mayusculas
                if respuesta in ['SI', 'YES', 'S']:  # Condición mejorada
                    cursor.execute(
                        "UPDATE citas SET estado = %s WHERE id = %s", 
                        ('Cancelada', id_cita)
                    )
                    conexion.commit()
                    print(f"Cita con ID {id_cita} cancelada.")
                    
                elif respuesta in ['NO', 'N', 'NOPE']: #si pone un NO
                    print("La operación para cancelar no fue ejecutada.") 
        except Exception as e:
            print(f"Error al cancelar la cita: {e}")    
        finally:
            if conexion:
                cursor.close()
                conexion.close()



    def mostrar_citas(self, id_cliente):
        # Conectar a la base de datos
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Consultar todas las citas del cliente
            cursor.execute("""
                SELECT id, cliente_id, animal_id, empleado_id, servicio_id, estado, fecha
                FROM citas
                WHERE cliente_id = %s
            """, (id_cliente,))
            
            resultados = cursor.fetchall()  # Obtener todos los resultados en una tupla
            
            if resultados:
                print(f"Citas para el cliente ID {id_cliente}:")
                for resultado in resultados:  # Iterar para imprimir
                    id_cita, id_cliente, id_animal, id_empleado, id_servicio, estado, fecha = resultado
                    # Imprimir los detalles de cada cita
                    print(f"\nCita ID: {id_cita}")
                    print(f"Cliente ID: {id_cliente}")
                    print(f"Animal ID: {id_animal}")
                    print(f"Empleado ID: {id_empleado}")
                    print(f"Servicio ID: {id_servicio}")
                    print(f"Estado: {estado}")
                    print(f"Fecha: {fecha}")
            else:
                print(f"No se encontraron citas para el cliente con ID {id_cliente}.")
            
        except Exception as e:
            print(f"Error al mostrar las citas: {e}")
        finally:
            if conexion:
                cursor.close()
                conexion.close()



class Servicios:
    def __init__(self, id_servicio, nombre, descripcion, costo, id_veterinaria):
        self.__id_servicio = id_servicio
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__costo = costo
        self.__id_veterinaria=id_veterinaria

    # GET Y SET
    def getId(self):
        return self.__id_servicio

    def getIdVeterinaria(self):
        return self.__id_veterinaria

    def setId(self, id_servicio):
        self.__id_servicio = id_servicio

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def getCosto(self):
        return self.__costo

    def setCosto(self, costo):
        self.__costo = costo

    # FUNCIONES PARA LOS SERVICIOS
    def actualizar_costo(self, id_servicio):
        # Verificar si el servicio existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre FROM servicios WHERE id = %s", (id_servicio,))
            resultado = cursor.fetchone()  # Obtener el resultado como una tupla

            if not resultado:
                limpiarPantalla()
                print(f"No existe el servicio con el ID {id_servicio}.")
            else:
                nombre_servicio = resultado[0] # Obtener nombre del servicio
                # Pedir nuevo costo
                nuevo_costo = input(f"Ingrese el costo nuevo para '{nombre_servicio}': ")
                
                try:
                    nuevo_costo = float(nuevo_costo)
                    if nuevo_costo <= 0:
                        print("El costo debe ser un número positivo.")
                        return
                    
                    # Proceder a actualizar el costo del servicio
                    cursor.execute(
                        "UPDATE servicios SET costo = %s WHERE id = %s",
                        (nuevo_costo, id_servicio)
                    )
                    conexion.commit()
                    limpiarPantalla()
                    print(f"El costo del servicio '{nombre_servicio}' ha sido actualizado a {nuevo_costo} pesos.")
                except ValueError:
                    limpiarPantalla()
                    print("El costo ingresado no es un número válido.")
        except Exception as e:
            limpiarPantalla()
            print(f"Error al actualizar el costo: {e}")
        finally:
            if conexion:
                cursor.close()
                conexion.close()



    def mostrar_servicios(self):
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM servicios")
            for (id_servicio, nombre, descripcion, costo, id_veterinaria) in cursor: #iterar para que se vea bonito
                print("")
                print(f"\nID: {id_servicio}\n Nombre: {nombre} \n Descripcion: {descripcion} \n Precio: {costo}\n Veterinaria: {id_veterinaria} ")
            cursor.close()
            conexion.close()
        else:
            print("No se pudo establecer la conexión a la base de datos.")
