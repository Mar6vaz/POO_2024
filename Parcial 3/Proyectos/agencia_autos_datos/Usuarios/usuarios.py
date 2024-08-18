from conexionBd import obtener_conexion
from funciones import * 
import hashlib
import datetime
from mysql.connector import Error



class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos=apellidos
        self.email=email
        self.contrasena = self.hash_password(password)


    #FUNCIONES PARA UN USUARIO



    def hash_password(self, contrasena):
        if contrasena:  # Asegúrate de que contrasena no sea None
            return hashlib.sha256(contrasena.encode()).hexdigest()
        return None


    def verificar_password(self, password_ingresada, password_almacenada):
        return self.hash_password(password_ingresada) == password_almacenada

    @staticmethod
    def registrar(nombre, apellidos, email, contrasena):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            fecha = datetime.datetime.now()
            cursor.execute(
                "INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s)",
                (nombre, apellidos, email, contrasena, fecha)
            )
            conexion.commit()
            print("Usuario registrado exitosamente.")
            return True
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return False    

    @staticmethod
    def iniciar_sesion(email, contrasena):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            contrasena = hashlib.sha256(contrasena.encode()).hexdigest()
            # Asegúrate de pasar una tupla en lugar de una cadena para los parámetros de la consulta.
            cursor.execute(
                "SELECT * FROM usuarios WHERE email=%s AND password=%s",
                (email, contrasena)  # Parámetros como una tupla
            )
            usuario = cursor.fetchone()
            if usuario:
                print("Inicio de sesión exitoso.")
                return usuario
            else:
                print("Email y/o contraseña incorrectas... vuelva a intentarlo.")
                return None      
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return None
