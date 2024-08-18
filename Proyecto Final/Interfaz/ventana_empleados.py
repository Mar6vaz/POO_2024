import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import mysql.connector
from conexionBD import conectar_bd 
from Personas.usuarios import Empleados



def abrir_ventana_actualizacion(empleado_id):
    empleado = Empleados(usuario=empleado_id)

    def guardar_cambios():
        # Recoger los valores de los campos de entrada
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        edad = entry_edad.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()
        puesto = entry_puesto.get()
        titulo = entry_titulo.get()
        salario = entry_salario.get()
        fecha_nacimiento = entry_fecha_nacimiento.get()
        id_agencia = entry_id_agencia.get()

        # Actualizar los datos del empleado
        empleado.actualizar_datos(nombre, apellidos, edad, telefono, correo, puesto, titulo, salario, fecha_nacimiento, id_agencia)
        ventana_actualizacion.destroy()


    ventana_actualizacion = tk.Toplevel()
    ventana_actualizacion.title("Actualizar Datos del Empleado")

    # Obtener el tamaño de la pantalla
    screen_width = ventana_actualizacion.winfo_screenwidth()
    screen_height = ventana_actualizacion.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_actualizacion.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tk.Label(ventana_actualizacion, text="Actualizar Datos del Empleado", font=("Arial", 14)).pack(pady=10)

    # Crear y colocar campos de entrada
    tk.Label(ventana_actualizacion, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(ventana_actualizacion)
    entry_nombre.insert(0, empleado.nombre if empleado.nombre else "")
    entry_nombre.pack(pady=5)

    tk.Label(ventana_actualizacion, text="Apellidos:").pack(pady=5)
    entry_apellidos = tk.Entry(ventana_actualizacion)
    entry_apellidos.insert(0, empleado.apellidos if empleado.apellidos else "")
    entry_apellidos.pack(pady=5)

    tk.Label(ventana_actualizacion, text="Edad:").pack(pady=5)
    entry_edad = tk.Entry(ventana_actualizacion)
    entry_edad.insert(0, empleado.edad if empleado.edad else "")
    entry_edad.pack(pady=5)

    tk.Label(ventana_actualizacion, text="Teléfono:").pack(pady=5)
    entry_telefono = tk.Entry(ventana_actualizacion)
    entry_telefono.insert(0, empleado.telefono if empleado.telefono else "")
    entry_telefono.pack(pady=5)

    tk.Label(ventana_actualizacion, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(ventana_actualizacion)
    entry_correo.insert(0, empleado.correo if empleado.correo else "")
    entry_correo.pack(pady=5)


    tk.Label(ventana_actualizacion, text="Puesto:").pack(pady=5)
    entry_puesto = tk.Entry(ventana_actualizacion)
    entry_puesto.insert(0, empleado.puesto if empleado.puesto else "")
    entry_puesto.pack(pady=5)

    tk.Label(ventana_actualizacion, text="Título:").pack(pady=5)
    entry_titulo = tk.Entry(ventana_actualizacion)
    entry_titulo.insert(0, empleado.titulo if empleado.titulo else "")
    entry_titulo.pack(pady=5)

    tk.Label(ventana_actualizacion, text="Salario:").pack(pady=5)
    entry_salario = tk.Entry(ventana_actualizacion)
    entry_salario.insert(0, empleado.salario if empleado.salario else "")
    entry_salario.pack(pady=5)

    tk.Label(ventana_actualizacion, text="Fecha de Nacimiento:").pack(pady=5)
    entry_fecha_nacimiento = tk.Entry(ventana_actualizacion)
    entry_fecha_nacimiento.insert(0, empleado.fecha_nacimiento if empleado.fecha_nacimiento else "")
    entry_fecha_nacimiento.pack(pady=5)

    tk.Label(ventana_actualizacion, text="ID Agencia:").pack(pady=5)
    entry_id_agencia = tk.Entry(ventana_actualizacion)
    entry_id_agencia.insert(0, empleado.id_agencia if empleado.id_agencia else "")
    entry_id_agencia.pack(pady=5)

    tk.Button(ventana_actualizacion, text="Guardar Cambios", command=guardar_cambios).pack(pady=20)



def mostrar_solicitudes(empleado):
    def aceptar_solicitud(solicitud_id):
        # Implementa la lógica para aceptar una solicitud aquí
        pass

    def actualizar_lista_solicitudes():
        # Limpiar el contenido del frame de solicitudes antes de actualizar
        for widget in frame_solicitudes.winfo_children():
            widget.destroy()

        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Seleccionar las solicitudes asociadas al empleado
                cursor.execute("""
                    SELECT s.id, s.servicio_id, s.cliente_id, s.fecha_solicitud, s.estado 
                    FROM solicitudes s 
                    WHERE s.empleado_id = %s
                """, (empleado,))
                solicitudes = cursor.fetchall()

                for solicitud in solicitudes:
                    solicitud_id = solicitud[0]
                    estado = solicitud[4]

                    # Mostrar la información de la solicitud
                    tk.Label(frame_solicitudes, text=f"ID: {solicitud_id}, Estado: {estado}", bg="cornsilk2").pack(pady=5)
                    
                    # Crear un botón "Aceptar" para cada solicitud
                    tk.Button(frame_solicitudes, text="Aceptar", command=lambda id=solicitud_id: aceptar_solicitud(id)).pack(pady=2)

            except Exception as e:
                messagebox.showerror("Error", f"Error al obtener las solicitudes: {e}")
            finally:
                cursor.close()
                conexion.close()

    ventana_solicitudes = tk.Toplevel()
    ventana_solicitudes.title("Solicitudes del Empleado")

    # Obtener el tamaño de la pantalla
    screen_width = ventana_solicitudes.winfo_screenwidth()
    screen_height = ventana_solicitudes.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_solicitudes.geometry(f"{window_width}x{window_height}+{x}+{y}")

    tk.Label(ventana_solicitudes, text="Solicitudes Asociadas:", font=("Arial", 14), bg="cornsilk2").pack(pady=10)

    frame_solicitudes = tk.Frame(ventana_solicitudes, bg="cornsilk2")
    frame_solicitudes.pack(fill=tk.BOTH, expand=True)

    tk.Button(ventana_solicitudes, text="Actualizar Lista", command=actualizar_lista_solicitudes).pack(pady=10)
    actualizar_lista_solicitudes()


def mostrar_datos(empleado_id):
    # Crear una instancia de Empleados con el ID proporcionado
    empleado = Empleados(usuario=empleado_id)
    
    def cargar_datos():
        try:
            # Obtener los datos del empleado desde la base de datos
            datos = empleado.obtener_datos()  
            if datos:
                # Actualizar las etiquetas con los datos del empleado
                nombre_label.config(text=f"Nombre: {datos[0]}")
                apellidos_label.config(text=f"Apellidos: {datos[1]}")
                edad_label.config(text=f"Edad: {datos[2]}")
                telefono_label.config(text=f"Teléfono: {datos[3]}")
                correo_label.config(text=f"Correo: {datos[4]}")
                puesto_label.config(text=f"Puesto: {datos[5]}")
                titulo_label.config(text=f"Título: {datos[6]}")
                salario_label.config(text=f"Salario: {datos[7]}")
                fecha_nacimiento_label.config(text=f"Fecha de Nacimiento: {datos[8]}")
                id_agencia_label.config(text=f"ID Agencia: {datos[9]}")
            else:
                messagebox.showerror("Error", "No se encontraron datos para el empleado.", parent=ventana_datos)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener datos: {e}", parent=ventana_datos)

    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos del Empleado")

    # Configuración de la ventana
    screen_width = ventana_datos.winfo_screenwidth()
    screen_height = ventana_datos.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_datos.geometry(f"{window_width}x{window_height}+{x}+{y}")
    ventana_datos.configure(bg="MistyRose4")

    # Crear y colocar las etiquetas para los datos
    nombre_label = tk.Label(ventana_datos, text="Nombre:", bg="MistyRose4", font=("Arial", 12))
    nombre_label.pack(pady=5)
    apellidos_label = tk.Label(ventana_datos, text="Apellidos:", bg="MistyRose4", font=("Arial", 12))
    apellidos_label.pack(pady=5)
    edad_label = tk.Label(ventana_datos, text="Edad:", bg="MistyRose4", font=("Arial", 12))
    edad_label.pack(pady=5)
    telefono_label = tk.Label(ventana_datos, text="Teléfono:", bg="MistyRose4", font=("Arial", 12))
    telefono_label.pack(pady=5)
    correo_label = tk.Label(ventana_datos, text="Correo:", bg="MistyRose4", font=("Arial", 12))
    correo_label.pack(pady=5)
    puesto_label = tk.Label(ventana_datos, text="Puesto:", bg="MistyRose4", font=("Arial", 12))
    puesto_label.pack(pady=5)
    titulo_label = tk.Label(ventana_datos, text="Título:", bg="MistyRose4", font=("Arial", 12))
    titulo_label.pack(pady=5)
    salario_label = tk.Label(ventana_datos, text="Salario:", bg="MistyRose4", font=("Arial", 12))
    salario_label.pack(pady=5)
    fecha_nacimiento_label = tk.Label(ventana_datos, text="Fecha de Nacimiento:", bg="MistyRose4", font=("Arial", 12))
    fecha_nacimiento_label.pack(pady=5)
    id_agencia_label = tk.Label(ventana_datos, text="ID Agencia:", bg="MistyRose4", font=("Arial", 12))
    id_agencia_label.pack(pady=5)

    # Botón para cargar los datos
    tk.Button(ventana_datos, text="Cargar Datos", command=cargar_datos).pack(pady=20)

    # Cargar los datos iniciales
    cargar_datos()


def mostrar_ventana_empleados(empleado):
    ventana_empleado = tk.Toplevel()
    ventana_empleado.title("Menú del Empleado")

    # Obtener el tamaño de la pantalla
    screen_width = ventana_empleado.winfo_screenwidth()
    screen_height = ventana_empleado.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_empleado.geometry(f"{window_width}x{window_height}+{x}+{y}")
    ventana_empleado.configure(bg="MistyRose4")

    # Crear y colocar los botones
    tk.Button(ventana_empleado, text="Atender Solicitudes", command=lambda: mostrar_solicitudes(empleado), width=25, height=3, font=("Arial", 14)).pack(pady=20)
    tk.Button(ventana_empleado, text="Mis Datos", command=lambda: mostrar_datos(empleado), width=25, height=3, font=("Arial", 14)).pack(pady=20)
    tk.Button(ventana_empleado, text="Actualizar Datos", command=lambda: abrir_ventana_actualizacion(empleado), width=25, height=3, font=("Arial", 14)).pack(pady=20)
