import tkinter as tk
from tkinter import messagebox
from mysql.connector import Error
import mysql.connector
from conexionBD import conectar_bd
from Servicios.servicios import Agencias
from Servicios.servicios import Servicios
from Servicios.servicios import Citas
from Servicios.servicios import Solicitudes
from Personas.usuarios import Clientes
from datetime import datetime



def mostrar_menu_cliente(cliente):
    ventana_menu_cliente = tk.Toplevel()
    
    # Obtener el tamaño de la pantalla
    screen_width = ventana_menu_cliente.winfo_screenwidth()
    screen_height = ventana_menu_cliente.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_menu_cliente.geometry(f"{window_width}x{window_height}+{x}+{y}")
    #ventana_menu_cliente.geometry("800x900")
    ventana_menu_cliente.configure(bg="lightblue")
    
    tk.Label(ventana_menu_cliente, text="¡Bienvenido a nuestro sistema!", font=("Arial", 20), bg="lightblue").pack(pady=20)
    
    # Botón Agencias
    btn_agencias = tk.Button(ventana_menu_cliente, text="Agencias", command=mostrar_agencias, font=("Arial", 14))
    btn_agencias.pack(pady=10)
    
    # Botón Servicios
    btn_servicios = tk.Button(ventana_menu_cliente, text="Servicios Disponibles", command=lambda: mostrar_servicios(cliente), font=("Arial", 14))
    btn_servicios.pack(pady=10)
    
    # Botón Citas
    cliente_id = 2
    btn_gestion_citas = tk.Button(ventana_menu_cliente, text="Gestión de Citas", command=lambda: abrir_gestion_citas(cliente), font=("Arial", 14))
    btn_gestion_citas.pack(pady=20)
    
    # Botón Mi perfil
    btn_perfil = tk.Button(ventana_menu_cliente, text="Mi Perfil", command=lambda: mostrar_perfil(cliente), font=("Arial", 14))
    btn_perfil.pack(pady=10)

    # Botón Solicitar Servicio
    btn_soli = tk.Button(ventana_menu_cliente, text="Solicitar Servicio", command=lambda: solicitar_servicio(cliente), font=("Arial", 14))
    btn_soli.pack(pady=10)


def mostrar_agencias():
    def mostrar_detalles():
        agencias = Agencias.obtener_agencias()
        
        if agencias:
            detalles_agencias = ""
            for agencia in agencias:
                detalles_agencias += (f"ID: {agencia.id}\nNombre: {agencia.nombre}\nDirección: {agencia.direccion}\nTeléfono: {agencia.telefono}\nDescripción: {agencia.descripcion}\n\n")
            
            # Mostrar los detalles en el widget de texto
            text_widget.delete("1.0", tk.END)  # Limpiar el widget de texto
            text_widget.insert(tk.END, detalles_agencias)
        else:
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, "No se pudo obtener la información de las agencias.")

    # Crear la ventana para mostrar agencias
    ventana_agencias = tk.Toplevel()
    ventana_agencias.title("Agencias Disponibles")
    
    # Obtener el tamaño de la pantalla
    screen_width = ventana_agencias.winfo_screenwidth()
    screen_height = ventana_agencias.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_agencias.geometry(f"{window_width}x{window_height}+{x}+{y}")
    ventana_agencias.configure(bg="lightyellow")
    
    # Crear un widget Text para mostrar los detalles
    text_widget = tk.Text(ventana_agencias, wrap=tk.WORD, height=20, width=70)
    text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    # Crear un botón para cargar los detalles
    btn_cargar_detalles = tk.Button(ventana_agencias, text="Cargar Detalles", command=mostrar_detalles, font=("Arial", 14))
    btn_cargar_detalles.pack(pady=10)
    
    # Llamar a mostrar_detalles para cargar los datos inicialmente (opcional)
    mostrar_detalles()


def mostrar_servicios(cliente):
    def mostrar_detalles():
        detalles_servicios = Servicios.obtener_detalles_servicios()
        # Mostrar los detalles en el widget de texto
        text_widget.delete("1.0", tk.END)  # Limpiar el widget de texto
        for detalle in detalles_servicios:
            text_widget.insert(tk.END, detalle + "\n")
    
    # Crear la ventana para mostrar servicios
    ventana_servicios = tk.Toplevel()
    ventana_servicios.title("Servicios Disponibles")
    
    # Obtener el tamaño de la pantalla
    screen_width = ventana_servicios.winfo_screenwidth()
    screen_height = ventana_servicios.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_servicios.geometry(f"{window_width}x{window_height}+{x}+{y}")
    ventana_servicios.configure(bg="lightgreen")
    
    # Crear un widget Text para mostrar los detalles
    text_widget = tk.Text(ventana_servicios, wrap=tk.WORD, height=20, width=70)
    text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    # Crear un botón para cargar los detalles
    btn_cargar_detalles = tk.Button(ventana_servicios, text="Cargar Detalles", command=mostrar_detalles, font=("Arial", 14))
    btn_cargar_detalles.pack(pady=10)
    
    # Llamar a mostrar_detalles para cargar los datos inicialmente (opcional)
    mostrar_detalles()


def mostrar_citas(cliente):
    def mostrar_detalles():
        citas = Citas.obtener_citas(cliente)
        if citas:
            detalles = "\n\n".join([f"ID: {cita.id}\nSolicitud ID: {cita.id_solicitud}\nEmpleado ID: {cita.id_empleado}\nFecha: {cita.fecha}\nEstado: {cita.estado}" for cita in citas])
        else:
            detalles = "No hay citas programadas para usted."

        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, detalles)

    def ventana_confirmar_cita():
        def confirmar_cita():
            id_cita = entry_id_cita.get()
            conexion = conectar_bd()
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT COUNT(*) FROM citas WHERE id = %s", (id_cita,))
                resultado = cursor.fetchone()
                if resultado[0] == 0:
                    messagebox.showwarning("Error", "Lo sentimos... esta cita no se ha programado.", parent=ventana_citas)
                else:
                    respuesta = messagebox.askyesno("Confirmación", "¿Seguro que confirmará esta cita?")
                    if respuesta:
                        Citas.actualizar_estado_cita(id_cita, 'Confirmada')
                        messagebox.showinfo("Confirmación", f"Cita con ID {id_cita} confirmada.")
                        mostrar_detalles()
                    else:
                        messagebox.showinfo("Cancelado", "La confirmación ha sido cancelada.", parent=ventana_citas)
            except Exception as e:
                messagebox.showerror("Error", f"Error al confirmar la cita: {e}", parent=ventana_citas)
        
        ventana_confirmacion = tk.Toplevel()
        ventana_confirmacion.title("Confirmar Cita")
        # Obtener el tamaño de la pantalla
        screen_width = ventana_confirmacion.winfo_screenwidth()
        screen_height = ventana_confirmacion.winfo_screenheight()

        # Tamaño de la ventana
        window_width = 950
        window_height = 700

        # Calcular la posición centrada
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Establecer tamaño y posición
        ventana_confirmacion.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        tk.Label(ventana_confirmacion, text="ID Cita:", font=("Arial", 12)).pack(pady=10)
        entry_id_cita = tk.Entry(ventana_confirmacion)
        entry_id_cita.pack(pady=5)
        
        tk.Button(ventana_confirmacion, text="Confirmar Cita", command=confirmar_cita, font=("Arial", 14)).pack(pady=20)

    def ventana_cancelar_cita():
        def cancelar_cita():
            id_cita = entry_id_cita.get()
            conexion = conectar_bd()
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT COUNT(*) FROM citas WHERE id = %s", (id_cita,))
                resultado = cursor.fetchone()
                if resultado[0] == 0:
                    messagebox.showwarning("Error", "Lo sentimos... esta cita no se ha programado.", parent=ventana_citas)
                else:
                    respuesta = messagebox.askyesno("Cancelación", "¿Seguro que cancelará esta cita?")
                    if respuesta:
                        Citas.actualizar_estado_cita(id_cita, 'Cancelada')
                        messagebox.showinfo("Confirmación", f"Cita con ID {id_cita} cancelada.")
                        mostrar_detalles()
                    else:
                        messagebox.showinfo("Cancelado", "La cancelación ha sido cancelada.", parent=ventana_citas)
            except Exception as e:
                messagebox.showerror("Error", f"Error al cancelar la cita: {e}", parent=ventana_citas)
        
        ventana_cancelacion = tk.Toplevel()
        ventana_cancelacion.title("Cancelar Cita")
        # Obtener el tamaño de la pantalla
        screen_width = ventana_cancelacion.winfo_screenwidth()
        screen_height = ventana_cancelacion.winfo_screenheight()

        # Tamaño de la ventana
        window_width = 950
        window_height = 700

        # Calcular la posición centrada
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Establecer tamaño y posición
        ventana_cancelacion.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        tk.Label(ventana_cancelacion, text="ID Cita:", font=("Arial", 12)).pack(pady=10)
        entry_id_cita = tk.Entry(ventana_cancelacion)
        entry_id_cita.pack(pady=5)
        
        tk.Button(ventana_cancelacion, text="Cancelar Cita", command=cancelar_cita, font=("Arial", 14)).pack(pady=20)

    ventana_citas = tk.Toplevel()
    ventana_citas.title("Gestión de Citas")
    # Obtener el tamaño de la pantalla
    screen_width = ventana_citas.winfo_screenwidth()
    screen_height = ventana_citas.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_citas.geometry(f"{window_width}x{window_height}+{x}+{y}")

    text_widget = tk.Text(ventana_citas, wrap=tk.WORD, height=15, width=70)
    text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    btn_mostrar_citas = tk.Button(ventana_citas, text="Mostrar Citas Programadas", command=mostrar_detalles, font=("Arial", 14))
    btn_mostrar_citas.pack(pady=10)

    btn_confirmar_cita = tk.Button(ventana_citas, text="Confirmar Cita", command=ventana_confirmar_cita, font=("Arial", 14))
    btn_confirmar_cita.pack(pady=10)

    btn_cancelar_cita = tk.Button(ventana_citas, text="Cancelar Cita", command=ventana_cancelar_cita, font=("Arial", 14))
    btn_cancelar_cita.pack(pady=10)

def abrir_gestion_citas(cliente):
    mostrar_citas(cliente)



#SECCION DE 'MIPERFIL'
def mostrar_perfil(cliente):
    # Crear la ventana de perfil
    ventana_perfil = tk.Toplevel()
    ventana_perfil.title("Mi Perfil")

    # Configuración de la ventana de perfil
    screen_width = ventana_perfil.winfo_screenwidth()
    screen_height = ventana_perfil.winfo_screenheight()
    window_width = 950
    window_height = 700
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    ventana_perfil.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Crear botones en la ventana de perfil
    btn_mis_datos = tk.Button(ventana_perfil, text="Mis Datos", command=lambda: mostrar_mis_datos(cliente), font=("Arial", 14))
    btn_mis_datos.pack(pady=10)

    btn_actualizar_datos = tk.Button(ventana_perfil, text="Actualizar Datos", command=lambda: actualizar_mis_datos(cliente), font=("Arial", 14))
    btn_actualizar_datos.pack(pady=10)

    btn_mis_solicitudes = tk.Button(ventana_perfil, text="Mis Solicitudes", command=lambda: mostrar_mis_solicitudes(cliente), font=("Arial", 14))
    btn_mis_solicitudes.pack(pady=10)

def mostrar_mis_datos(cliente):
    # Crear la ventana de 'Mis Datos'
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Mis Datos")

    # Configuración de la ventana de datos
    screen_width = ventana_datos.winfo_screenwidth()
    screen_height = ventana_datos.winfo_screenheight()
    window_width = 950
    window_height = 700
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    ventana_datos.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Obtener datos del cliente
    cliente = Clientes(cliente, None, None, None, None, None, None, None)
    datos = cliente.obtener_datos()
    
    print(f"Datos devueltos por obtener_datos: {datos}")  # Debugging
    
    if datos:
        text_widget = tk.Text(ventana_datos, wrap=tk.WORD, height=15, width=70)
        text_widget.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, f"Nombre: {datos[0]}\nApellidos: {datos[1]}\nEdad: {datos[2]}\nTeléfono: {datos[3]}\nDirección: {datos[4]}\nCorreo: {datos[5]}")
    else:
        tk.Label(ventana_datos, text="No se encontraron datos para el cliente.", font=("Arial", 14)).pack(pady=20)


def actualizar_mis_datos(cliente):

    cliente = Clientes(cliente, None, None, None, None, None, None, None)

    # Crear la ventana de 'Actualizar Datos'
    ventana_actualizar = tk.Toplevel()
    ventana_actualizar.title("Actualizar Datos")
    ventana_actualizar.configure(bg="lightgreen")
    
    # Obtener el tamaño de la pantalla
    screen_width = ventana_actualizar.winfo_screenwidth()
    screen_height = ventana_actualizar.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_actualizar.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Configuración de la ventana de actualizar datos
    tk.Label(ventana_actualizar, text="Nombre:", font=("Arial", 12)).pack(pady=5)
    entry_nombre = tk.Entry(ventana_actualizar)
    entry_nombre.pack(pady=5)

    tk.Label(ventana_actualizar, text="Apellidos:", font=("Arial", 12)).pack(pady=5)
    entry_apellidos = tk.Entry(ventana_actualizar)
    entry_apellidos.pack(pady=5)

    tk.Label(ventana_actualizar, text="Edad:", font=("Arial", 12)).pack(pady=5)
    entry_edad = tk.Entry(ventana_actualizar)
    entry_edad.pack(pady=5)

    tk.Label(ventana_actualizar, text="Teléfono:", font=("Arial", 12)).pack(pady=5)
    entry_telefono = tk.Entry(ventana_actualizar)
    entry_telefono.pack(pady=5)

    tk.Label(ventana_actualizar, text="Dirección:", font=("Arial", 12)).pack(pady=5)
    entry_direccion = tk.Entry(ventana_actualizar)
    entry_direccion.pack(pady=5)

    tk.Label(ventana_actualizar, text="Email:", font=("Arial", 12)).pack(pady=5)
    entry_email = tk.Entry(ventana_actualizar)
    entry_email.pack(pady=5)

    # Rellenar los campos con los datos actuales del cliente
    entry_nombre.insert(0, cliente.nombre if cliente.nombre else "")
    entry_apellidos.insert(0, cliente.apellidos if cliente.apellidos else "")
    entry_edad.insert(0, cliente.edad if cliente.edad else "")
    entry_telefono.insert(0, cliente.telefono if cliente.telefono else "")
    entry_direccion.insert(0, cliente.direccion if cliente.direccion else "")
    entry_email.insert(0, cliente.correo if cliente.correo else "")

    def guardar_cambios():
        nuevo_nombre = entry_nombre.get()
        nuevo_apellido = entry_apellidos.get()
        nueva_edad = entry_edad.get()
        nuevo_telefono = entry_telefono.get()
        nueva_direccion = entry_direccion.get()
        nuevo_email = entry_email.get()


        

        try:
            if isinstance(cliente, Clientes):
                cliente.actualizar_datos(nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_telefono, nueva_direccion, nuevo_email)
                messagebox.showinfo("Actualizar Datos", "Datos actualizados con éxito.", parent=ventana_actualizar)
            else:
                messagebox.showerror("Error", "Cliente no es una instancia válida de Clientes.", parent=ventana_actualizar)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar los datos: {e}", parent=ventana_actualizar)

        ventana_actualizar.destroy()

    tk.Button(ventana_actualizar, text="Guardar Cambios", command=guardar_cambios).pack(pady=20)








def mostrar_mis_solicitudes(cliente):
    ventana_solicitudes = tk.Toplevel()
    ventana_solicitudes.title("Mis Solicitudes")

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
    ventana_solicitudes.configure(bg="Slategray3")

    # Conectar a la base de datos
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "SELECT id, servicio_id, fecha_solicitud, estado FROM solicitudes WHERE cliente_id = %s"
            cursor.execute(query, (cliente,))
            solicitudes = cursor.fetchall()

            # Mostrar detalles en una etiqueta
            if solicitudes:
                detalles = "\n\n".join([
                    f"ID: {solicitud[0]}\nServicio: {solicitud[1]}\nFecha Solicitud: {solicitud[2]}\nEstado: {solicitud[3]}"
                    for solicitud in solicitudes
                ])
                tk.Label(ventana_solicitudes, text=detalles, font=("Arial", 12), bg="Slategray3").pack(pady=20)
            else:
                tk.Label(ventana_solicitudes, text="No se encontraron solicitudes.", font=("Arial", 12), bg="Slategray3").pack(pady=20)

            cursor.close()
            conexion.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al recuperar las solicitudes: {err}", parent=ventana_solicitudes)
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.", parent=ventana_solicitudes)




def solicitar_servicio(cliente):
    ventana_solicitar = tk.Toplevel()
    ventana_solicitar.title("Solicitud de Servicios")

    # Obtener el tamaño de la pantalla
    screen_width = ventana_solicitar.winfo_screenwidth()
    screen_height = ventana_solicitar.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana_solicitar.geometry(f"{window_width}x{window_height}+{x}+{y}")
    ventana_solicitar.configure(bg="Slategray3")

    # Crear y colocar los widgets
    tk.Label(ventana_solicitar, text="ID Servicio:", font=("Arial", 12)).pack(pady=5)
    entry_idservice = tk.Entry(ventana_solicitar)
    entry_idservice.pack(pady=5)

    tk.Label(ventana_solicitar, text="Documentos:", font=("Arial", 12)).pack(pady=5)
    entry_documentos = tk.Entry(ventana_solicitar)
    entry_documentos.pack(pady=5)

    tk.Label(ventana_solicitar, text="Comentarios:", font=("Arial", 12)).pack(pady=5)
    text_comentarios = tk.Text(ventana_solicitar, height=10, width=70)
    text_comentarios.pack(pady=5)

    def insertar_solicitud():
        id_servicio = entry_idservice.get()
        documentos = entry_documentos.get()
        comentarios = text_comentarios.get("1.0", tk.END).strip()

        if not id_servicio or not documentos or not comentarios:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.", parent=ventana_solicitar)
            return

        # Obtener la información del servicio
        conexion = conectar_bd()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT empleado_id, agencia_id FROM servicios WHERE id = %s", (id_servicio,))
                resultado = cursor.fetchone()
                if resultado:
                    id_empleado = resultado[0]
                    id_agencia = resultado[1]
                    fecha_solicitud = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    solicitud = Solicitudes(
                        servicio_id=id_servicio,
                        empleado_id=id_empleado,
                        cliente_id=cliente,
                        agencia_id=id_agencia,
                        fecha_solicitud=fecha_solicitud,
                        estado='Pendiente',
                        documentos=documentos,
                        comentarios=comentarios
                    )

                    if solicitud.insertar_solicitud():
                        messagebox.showinfo("Éxito", "Solicitud enviada con éxito.", parent=ventana_solicitar)
                        ventana_solicitar.destroy()
                    else:
                        messagebox.showerror("Error", "No se pudo enviar la solicitud.", parent=ventana_solicitar)

                else:
                    messagebox.showwarning("Advertencia", "El servicio especificado no existe.", parent=ventana_solicitar)

                cursor.close()
                conexion.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al enviar la solicitud: {err}", parent=ventana_solicitar)
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos.", parent=ventana_solicitar)

    btn_enviar = tk.Button(ventana_solicitar, text="Enviar Solicitud", command=insertar_solicitud, font=("Arial", 14))
    btn_enviar.pack(pady=20)