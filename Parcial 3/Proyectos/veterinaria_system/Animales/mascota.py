

from conexionBD import obtener_conexion
from funciones import *
class Animales:
    def __init__(self, id_animal, nombre, especie, raza, edad, id_cliente):
        self.__id_animal=id_animal
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__id_cliente = id_cliente

    # GETTER Y SETTER
    def getIdanimal (self):
        return self.__id_animal

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEspecie(self):
        return self.__especie

    def setEspecie(self, especie):
        self.__especie = especie

    def getRaza(self):
        return self.__raza

    def setRaza(self, raza):
        self.__raza = raza

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    def getIdCliente(self):
        return self.__id_cliente

    def setIdCliente(self, id_cliente):
        self.__id_cliente = id_cliente

   
    def mostrar_historial(self, cliente_id):
        # Conexion a la BD
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()  
            # Consulta para obtener todos los animales del cliente
            cursor.execute("""
                SELECT id, nombre, especie, raza, edad
                FROM animales
                WHERE cliente_id = %s
            """, (cliente_id,))
            
            animales = cursor.fetchall()

            if animales:
                limpiarPantalla()
                print(f"Animales para el cliente con ID {cliente_id}:")
                for animal in animales: #itera para imprimir bonito
                    print("")
                    print(f"ID: {animal[0]} \n Nombre: {animal[1]} \n Especie: {animal[2]} \n Raza: {animal[3]} \n Edad: {animal[4]}")
            else:
                print(f"No se encontraron animales para el cliente con ID {cliente_id}.")
        
        except:
            print("Error al obtener animales: ")
        
        finally:
            if conexion:
                cursor.close()
                conexion.close()
        

    def actualizar_historial(self, id_animal):
        # Verificar si el animal existe
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            # Extrae datos
            cursor.execute("SELECT nombre, especie, raza, edad FROM animales WHERE id = %s", (id_animal,))
            resultado = cursor.fetchone()

            if not resultado:
                print(f"No existe la mascota con el ID {id_animal}.")
            else:
                # Evitar la necesidad de acceder a los elementos por índice en el resto del código.
                nombre_actual, especie_actual, raza_actual, edad_actual = resultado
                # Solicitar nuevos datos
                limpiarPantalla()
                print("Presione Enter para dejar sin cambios")
                nombre = input(f"Nombre ({nombre_actual}): ") or nombre_actual
                especie = input(f"Especie ({especie_actual}): ") or especie_actual
                raza = input(f"Raza ({raza_actual}): ") or raza_actual
                edad = input(f"Edad ({edad_actual}): ") or edad_actual
            
                # Proceder a actualizar los detalles del animal
                cursor.execute("""
                    UPDATE animales
                    SET nombre = %s, especie = %s, raza = %s, edad = %s
                    WHERE id = %s
                """, (nombre, especie, raza, edad, id_animal))  # Usar id_animal aquí
                conexion.commit()
                print(f"Datos del animal con ID {id_animal} actualizados correctamente.")
                
        except Exception as e:
            print(f"Ocurrió un error al verificar la existencia de la mascota: {e}")
        finally:
            if conexion:
                cursor.close()
                conexion.close()  # Cierra la conexión y el cursor como buena práctica
