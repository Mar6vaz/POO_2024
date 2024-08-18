import hashlib
from tkinter import messagebox
import mysql.connector
from conexionBD import conectar_bd

class Personas:
    def __init__(self, usuario, nombre, apellidos, edad, telefono, correo, password, direccion=None):
        self.usuario = usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono
        self.correo = correo
        self.contrasena = password  # Guarda la contraseña en texto claro para comparar en inicio de sesión
        self.direccion = direccion

    def hash_password(self, contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def verificar_password(self, password_ingresada, password_almacenada):
        return self.hash_password(password_ingresada) == password_almacenada


    def iniciar_sesion(self):
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()

                # Consultar en la tabla de clientes
                cursor.execute("SELECT id, nombre, apellidos, edad, tel, email, password, direccion FROM clientes WHERE email = %s", (self.correo,))
                cliente_data = cursor.fetchone()
                if cliente_data:
                    password_almacenada = cliente_data[6]
                    if self.verificar_password(self.contrasena, password_almacenada):
                        cliente = Clientes(*cliente_data)
                        return 'cliente', cliente.usuario  # Devolver el ID del cliente

                # Consultar en la tabla de empleados
                cursor.execute("SELECT id, nombre, apellidos, edad, fecha_nacimiento, telefono, email, password, puesto, titulo, salario, agencia_id FROM empleados WHERE email = %s", (self.correo,))
                empleado_data = cursor.fetchone()
                if empleado_data:
                    password_almacenada = empleado_data[7]
                    if self.verificar_password(self.contrasena, password_almacenada):
                        empleado = Empleados(*empleado_data)
                        return 'empleado', empleado.usuario  # Devolver el ID del empleado

                return None, None

            except Exception as e:
                print(f"Error al iniciar sesión: {e}")
            finally:
                cursor.close()
                conexion.close()
        return None, None





class Clientes(Personas):
    def __init__(self, usuario, nombre=None, apellidos=None, edad=None, telefono=None, correo=None, password=None, direccion=None):
        # Inicializa con el ID del cliente y opcionalmente otros parámetros
        super().__init__(usuario, nombre, apellidos, edad, telefono, correo, password, direccion)
        
        # Solo cargar datos desde la base de datos si los parámetros opcionales no están dados
        if nombre is None and apellidos is None and edad is None:
            self.cargar_datos()
    
    def cargar_datos(self):
        datos = self.obtener_datos()
        if datos:
            self.nombre, self.apellidos, self.edad, self.telefono, self.direccion, self.correo = datos

    def registrar(self):
        conexion = conectar_bd()
        try:
            if conexion:
                cursor = conexion.cursor()
                hashed_password = self.hash_password(self.contrasena) if self.contrasena else None
                cursor.execute(
                    "INSERT INTO clientes (nombre, apellidos, edad, tel, direccion, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (self.nombre, self.apellidos, self.edad, self.telefono, self.direccion, self.correo, hashed_password)
                )
                conexion.commit()
                cliente_id = cursor.lastrowid
                return "Cliente registrado con éxito", None
            else:
                return None, "No se pudo establecer la conexión a la base de datos."
        except Exception as e:
            return None, f"Error al registrar el cliente: {e}"
        finally:
            if conexion:
                cursor.close()
                conexion.close()

    def obtener_datos(self):
        conexion = conectar_bd()
        datos = None  # Inicializa 'datos' para evitar el UnboundLocalError
        if conexion:
            try:
                cursor = conexion.cursor()
                print(f"Consultando datos para usuario: {self.usuario}")  # Debugging
                cursor.execute("SELECT nombre, apellidos, edad, tel, direccion, email FROM clientes WHERE id = %s", (self.usuario,))
                datos = cursor.fetchone()
                print(f"Datos obtenidos: {datos}")  # Debugging
            except Exception as e:
                print(f"Error al obtener datos: {e}")
            finally:
                cursor.close()
                conexion.close()
        return datos

    def actualizar_datos(self, nombre, apellidos, edad, tel, direccion, email):
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("""
                    UPDATE clientes SET
                    nombre = COALESCE(NULLIF(%s, ''), nombre),
                    apellidos = COALESCE(NULLIF(%s, ''), apellidos),
                    edad = COALESCE(NULLIF(%s, ''), edad),
                    tel = COALESCE(NULLIF(%s, ''), tel),
                    direccion = COALESCE(NULLIF(%s, ''), direccion),
                    email = COALESCE(NULLIF(%s, ''), email)
                    WHERE id = %s
                """, (nombre, apellidos, edad, tel, direccion, email, self.usuario))
                conexion.commit()
            except Exception as e:
                print(f"Error al actualizar los datos: {e}")
            finally:
                cursor.close()
                conexion.close()

            
    def obtener_solicitudes(self):
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM solicitudes WHERE cliente_id = %s", (self.usuario,))
            solicitudes = cursor.fetchall()
            cursor.close()
            return solicitudes
        return []


class Empleados(Personas):
    def __init__(self, usuario, nombre=None, apellidos=None, edad=None, telefono=None, correo=None, password=None, puesto=None, titulo=None, salario=None, fecha_nacimiento=None, id_agencia=None):
        # Inicializa con el ID del empleado y opcionalmente otros parámetros
        super().__init__(usuario, nombre, apellidos, edad, telefono, correo, password)
        
        self.puesto = puesto
        self.titulo = titulo
        self.salario = salario
        self.fecha_nacimiento = fecha_nacimiento
        self.id_agencia = id_agencia

        # Solo cargar datos desde la base de datos si los parámetros opcionales no están dados
        if nombre is None and apellidos is None and edad is None:
            self.cargar_datos()

    def cargar_datos(self):
        datos = self.obtener_datos()
        if datos:
            self.nombre, self.apellidos, self.edad, self.telefono, self.correo, self.puesto, self.titulo, self.salario, self.fecha_nacimiento, self.id_agencia = datos

    def obtener_datos(self):
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("""
                    SELECT nombre, apellidos, edad, telefono, email, puesto, titulo, salario, fecha_nacimiento, agencia_id
                    FROM empleados
                    WHERE id = %s
                """, (self.usuario,))
                datos = cursor.fetchone()
                return datos
            except Exception as e:
                print(f"Error al obtener datos: {e}")
                return None
            finally:
                cursor.close()
                conexion.close()




    def aceptar_solicitud(self, solicitud_id):
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()

                # Obtener el cliente_id de la solicitud
                cursor.execute("SELECT cliente_id FROM solicitudes WHERE id = %s", (solicitud_id,))
                resultado = cursor.fetchone()
                if resultado:
                    cliente_id = resultado[0]

                    # Actualizar el estado de la solicitud
                    cursor.execute("UPDATE solicitudes SET estado = %s WHERE id = %s", ('Aceptada', solicitud_id))

                    # Insertar en la tabla cita usando el id_empleado proporcionado
                    cursor.execute("""
                        INSERT INTO cita (cliente_id, solicitud_id, empleado_id, fecha_cita, estado) 
                        VALUES (%s, %s, %s, %s, %s)
                    """, (cliente_id, solicitud_id, self.id_empleado, '2024-08-15 10:00:00', 'Pendiente'))

                    conexion.commit()

                    if cursor.rowcount > 0:
                        messagebox.showinfo("Éxito", f"Solicitud con ID {solicitud_id} aceptada, cliente asociado, y cita creada.")
                        self.actualizar_lista_solicitudes()
                    else:
                        messagebox.showwarning("Advertencia", "No se encontró la solicitud con el ID proporcionado.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontró el cliente asociado a la solicitud.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al aceptar la solicitud: {e}")
            finally:
                cursor.close()
                conexion.close()

    def actualizar_datos(self, nombre, apellidos, edad, telefono, correo, puesto, titulo, salario, fecha_nacimiento, id_agencia):
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                
                # Construir la consulta SQL
                update_query = """
                    UPDATE empleados 
                    SET nombre = COALESCE(NULLIF(%s, ''), nombre),
                        apellidos = COALESCE(NULLIF(%s, ''), apellidos),
                        edad = COALESCE(NULLIF(%s, edad), edad),
                        fecha_nacimiento = COALESCE(NULLIF(%s, ''), fecha_nacimiento),
                        telefono = COALESCE(NULLIF(%s, ''), telefono),
                        email = COALESCE(NULLIF(%s, ''), email),
                        puesto = COALESCE(NULLIF(%s, ''), puesto),
                        titulo = COALESCE(NULLIF(%s, ''), titulo),
                        salario = COALESCE(NULLIF(%s, salario), salario),
                        id_agencia = COALESCE(NULLIF(%s, id_agencia), id_agencia)
                    WHERE id = %s
                """
                
                # Preparar los parámetros
                params = (
                    nombre, apellidos, edad, fecha_nacimiento, telefono, correo, puesto, titulo, salario, id_agencia, self.id_empleado
                )
                # Ejecutar la consulta
                cursor.execute(update_query, params)
                conexion.commit()
                
                if cursor.rowcount > 0:
                    messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontró el empleado para actualizar.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar los datos: {e}")
            finally:
                cursor.close()
                conexion.close()










        

