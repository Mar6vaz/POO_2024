import tkinter as tk
from tkinter import messagebox
from Personas.usuarios import Clientes, Empleados

def abrir_ventana_registro(ventana_principal):
    def registrar_cliente():
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        edad = entry_edad.get()
        telefono = entry_telefono.get()
        correo = entry_email.get()
        direccion = entry_direccion.get()
        password = entry_password.get()
        
        cliente = Clientes(None, nombre=nombre, apellidos=apellidos, edad=edad, telefono=telefono, correo=correo, password=password, direccion=direccion)
        mensaje, error = cliente.registrar()
        if mensaje:
            messagebox.showinfo("Registro Exitoso", mensaje)
            ventana_registro.destroy()  # Cierra la ventana de registro
        else:
            messagebox.showerror("Error", error)

    # Crear la ventana de registro
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registro")

    # Obtener las dimensiones de la ventana principal
    ancho_ventana_principal = ventana_principal.winfo_width()
    alto_ventana_principal = ventana_principal.winfo_height()
    x_ventana_principal = ventana_principal.winfo_x()
    y_ventana_principal = ventana_principal.winfo_y()

    # Dimensiones de la ventana de registro
    ancho_registro = 500
    alto_registro = 600

    # Calcular la posición para centrar la ventana de registro
    x = x_ventana_principal + (ancho_ventana_principal - ancho_registro) // 2
    y = y_ventana_principal + (alto_ventana_principal - alto_registro) // 2

    ventana_registro.geometry(f"{ancho_registro}x{alto_registro}+{x}+{y}")
    ventana_registro.configure(bg="cornsilk2")

    # Etiquetas y campos de entrada
    tk.Label(ventana_registro, text="Nombre:", bg="cornsilk2").pack(pady=5)
    entry_nombre = tk.Entry(ventana_registro)
    entry_nombre.pack(pady=5)

    tk.Label(ventana_registro, text="Apellidos:", bg="cornsilk2").pack(pady=5)
    entry_apellidos = tk.Entry(ventana_registro)
    entry_apellidos.pack(pady=5)

    tk.Label(ventana_registro, text="Edad:", bg="cornsilk2").pack(pady=5)
    entry_edad = tk.Entry(ventana_registro)
    entry_edad.pack(pady=5)

    tk.Label(ventana_registro, text="Teléfono:", bg="cornsilk2").pack(pady=5)
    entry_telefono = tk.Entry(ventana_registro)
    entry_telefono.pack(pady=5)

    tk.Label(ventana_registro, text="Dirección:", bg="cornsilk2").pack(pady=5)
    entry_direccion = tk.Entry(ventana_registro)
    entry_direccion.pack(pady=5)

    tk.Label(ventana_registro, text="Correo Electrónico:", bg="cornsilk2").pack(pady=5)
    entry_email = tk.Entry(ventana_registro)
    entry_email.pack(pady=5)

    tk.Label(ventana_registro, text="Contraseña:", bg="cornsilk2").pack(pady=5)
    entry_password = tk.Entry(ventana_registro, show="*")
    entry_password.pack(pady=5)

    # Botón para registrar
    tk.Button(ventana_registro, text="Registrar", command=registrar_cliente).pack(pady=20)

    # Ejecutar la ventana de registro
    ventana_registro.mainloop()
