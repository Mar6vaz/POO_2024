# CLASES DE LAS PERSONAS

from conexionBD import obtener_conexion
from funciones import * 

class Personas:
    def __init__(self, identificador, nombre, direccion, telefono):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    # GETTER Y SETTER
    def getIdentificador(self):
        return self.__identificador

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        self.__telefono = telefono

    # FUNCION DE LA PERSONA
    def actualizar_datos(self, cursor, **kwargs):
        pass
        #query = "UPDATE personas SET nombre = %s, direccion = %s, telefono = %s WHERE id_persona = %s"
        #values = (kwargs.get('nombre', self.nombre), 
                  #kwargs.get('direccion', self.direccion), 
                  #kwargs.get('telefono', self.telefono), 
                  #self.id_persona)
        #cursor.execute(query, values)
        

class Clientes(Personas):
    def __init__(self, identificador, nombre, direccion, telefono, tipo):
        super().__init__(identificador, nombre, direccion, telefono)
        self.__tipo = tipo

    # GETTER Y SETTER
    def getIdentificador(self):
        return self.__identificador

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
        self.__tipo = tipo

    # FUNCION PARA CLIENTES

    def actualizar_datos(self, id_cliente):
        # Verificar si el empleado existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            
            # Mostrar el cliente que eligió
            cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
            resultado = cursor.fetchone() #una fila de datos en una tupla

            if not resultado:
                limpiarPantalla()
                print(f"No existe el cliente con el ID {id_cliente}.")
            else:
                #evita la necesidad de acceder a los elementos por índice en el resto del código.
                nombre_actual, direccion_actual, telefono_actual, tipo_actual = resultado[1:]

                # Solicitar nuevos datos
                limpiarPantalla()
                print("Presione Enter para dejar sin cambios")
                nombre = input(f"Nombre ({nombre_actual}): ") or nombre_actual
                direccion = input(f"Dirección ({direccion_actual}): ") or direccion_actual
                telefono = input(f"Teléfono ({telefono_actual}): ") or telefono_actual
                tipo = input(f"Puesto ({tipo_actual}): ") or tipo_actual

                # Proceder a actualizar los detalles del cliente
                #AQUI VAMOOOS
                cursor.execute("""
                    UPDATE clientes
                    SET nombre = %s, direccion = %s, telefono = %s, tipo = %s
                    WHERE id = %s
                """, (nombre, direccion, telefono, tipo, id_cliente))
                
                conexion.commit()
                limpiarPantalla()
                print(f"Datos del cliente con ID {id_cliente} actualizados correctamente.")
                
        except Exception as e:
            limpiarPantalla()
            print(f"Ocurrió un error al actualizar los datos del cliente: {e}") #pipipipi
        finally:
            if conexion:
                cursor.close()
                conexion.close() #cierra todo, es buena practica mana
            



    def mostrar_cliente(id_cliente):
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("select * from clientes")
            for (id_cliente, nombre, direccion, telefono, tipo) in cursor: #iterar para imprimir bonito
                print("")
                print(f"ID: {id_cliente}\n Nombre: {nombre} \n Dirección: {direccion} \n Teléfono: {telefono}\n Tipo: {tipo} ")
            cursor.close()
            conexion.close()
        else:
            print("No se pudo establecer la conexión a la base de datos.")

    
        

    def agregar_animal(self, nombre, especie, raza, edad, cliente_id):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO animales (nombre, especie, raza, edad, cliente_id) VALUES (%s, %s, %s, %s, %s)", 
                (nombre, especie, raza, edad, cliente_id)
            )
            conexion.commit()
            limpiarPantalla()
            print("Mascota agregada exitosamente.")
        except:
            limpiarPantalla()
            print("Ocurrió un error al agregar la mascota:")
        finally:
            cursor.close()
            conexion.close()


    def eliminar_animal(self, id_animal):
        # Verificar si el animal existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Verificar si el animal existe
            cursor.execute("SELECT COUNT(*) FROM animales WHERE id = %s", (id_animal,))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                print(f"No existe el animal con el ID {id_animal}.")
            else:
                # Confirmar la eliminación
                seguri = True  # Salida segura para no usar break
                while seguri:
                    respuesta = input("¿Seguro que quiere eliminar a esta mascota? (sí/no): ").upper()
                    if respuesta in ['SI', 'YES', 'SIMON']:
                        # Proceder a eliminar
                        cursor.execute("DELETE FROM animales WHERE id = %s", (id_animal,))
                        conexion.commit()
                        print(f"Mascota con ID {id_animal} eliminada correctamente.")
                        seguri = False
                    elif respuesta in ['NO', 'NOPE']: #otra forma de condicionar, creo que es mejor 
                        print("Eliminación cancelada.")
                        seguri = False
                    else:
                        print("Opción no válida. Responda sí o no.")
        except:
            print("Ocurrió un error al eliminar la mascota: ")
        finally:
            if conexion:
                cursor.close()
                conexion.close()



class Empleados(Personas):
    def __init__(self, identificador, nombre, direccion, telefono, puesto, salario, id_veterinaria):
        super().__init__(identificador, nombre, direccion, telefono)
        self.__puesto = puesto
        self.__salario = salario
        self.__id_veterinaria=id_veterinaria

    # GETTER Y SETTER
    def getPuesto(self):
        return self.__puesto

    def setPuesto(self, puesto):
        self.__puesto = puesto

    def getSalario(self):
        return self.__salario

    def setSalario(self, salario):
        self.__salario = salario

    def getIdVeterinaria(self):
        return self.__id_veterinaria

    # FUNCIONES DE EMPLEADOS
    def atender_cita(self, cita): #aqui que o que
        pass

    def actualizar_datos(self, id_empleado):
        # Verificar si el empleado existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            
            # Mostrar el empleado que eligió
            cursor.execute("SELECT * FROM empleados WHERE id = %s", (id_empleado,))
            resultado = cursor.fetchone()

            if not resultado:
                limpiarPantalla()
                print(f"No existe el empleado con el ID {id_empleado}.")
            else:
                # Almacenar el salario actual
                nombre_actual, direccion_actual, telefono_actual, puesto_actual, salario_actual, id_veterinaria_actual = resultado[1:]

                # Solicitar nuevos datos
                limpiarPantalla()
                print("Presione Enter para dejar sin cambios")
                nombre = input(f"Nombre ({nombre_actual}): ") or nombre_actual
                direccion = input(f"Dirección ({direccion_actual}): ") or direccion_actual
                telefono = input(f"Teléfono ({telefono_actual}): ") or telefono_actual
                puesto = input(f"Puesto ({puesto_actual}): ") or puesto_actual

                salario_input = input(f"Salario ({salario_actual}): ")
                if salario_input:
                    try:
                        salario = float(salario_input) #lo convierte a flotante si agrego numeros 
                    except ValueError:
                        limpiarPantalla()
                        print("Error: El salario debe ser un número válido. Se mantendrá el salario actual.") #no agregaste numeros
                        salario = salario_actual #entonces se mantiene actual
                else:
                    salario = salario_actual #ni no se agrega nada se mantiene igual

                id_veterinaria_input = input(f"Ingrese el ID de la veterinaria ({id_veterinaria_actual}): ") #aqui tambien
                if id_veterinaria_input:
                    try:
                        id_veterinaria = int(id_veterinaria_input) #lo convierte entero si agrego numeros
                    except ValueError:
                        limpiarPantalla()
                        print("Error: El ID de la veterinaria debe ser un número válido. Se mantendrá el ID de la veterinaria actual.")
                        id_veterinaria = id_veterinaria_actual #guarda e actual
                else:
                    id_veterinaria = id_veterinaria_actual #si presiona enter se mantiene con la id actual
                    #todo esto pasa cuando manejamos valores tipo INT y al presionar enter manda error
                    # ya sabes, quiere recibir valores numericos y el enter no ayuda

                # Proceder a actualizar los detalles del empleado
                #AQUI VAMOOOS
                cursor.execute("""
                    UPDATE empleados
                    SET nombre = %s, direccion = %s, telefono = %s, puesto = %s, salario = %s, veterinaria_id = %s
                    WHERE id = %s
                """, (nombre, direccion, telefono, puesto, salario, id_veterinaria, id_empleado))
                
                conexion.commit()
                limpiarPantalla()
                print(f"Datos del empleado con ID {id_empleado} actualizados correctamente.")
                
        except Exception as e:
            limpiarPantalla()
            print(f"Ocurrió un error al actualizar los datos del empleado: {e}") #pipipipip
        finally:
            if conexion:
                cursor.close()
                conexion.close() #cierra todo, es buena practica mana

                


    def mostrar_empleados(self):
        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("select * from empleados")
            for (id_empleado, nombre, direccion, telefono, puesto, salario, id_veterinaria) in cursor: #iterar para imprimir bonito
                print("")
                print(f"ID: {id_empleado},\n Nombre: {nombre} \n Dirección: {direccion} \n Teléfono: {telefono}\n Puesto: {puesto} \n Salario: {salario} \n Veterinaria: {id_veterinaria} ")
            cursor.close()
            conexion.close()
        else:
            print("No se pudo establecer la conexión a la base de datos.")
