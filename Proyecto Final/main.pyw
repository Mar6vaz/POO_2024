
import tkinter as tk
from tkinter import messagebox
from conexionBD import conectar_bd
import hashlib
from datetime import datetime
from Personas.usuarios import Clientes, Empleados
from Interfaz.registro import abrir_ventana_registro
from Interfaz.ventana_cliente import mostrar_menu_cliente
from Interfaz.ventana_empleados import mostrar_ventana_empleados


def mostrar_inicio_sesion():
    def intentar_inicio_sesion():
        email = entry_email.get()
        password = entry_password.get()
        tipo_usuario = var_tipo_usuario.get()

        print(f"Email ingresado: {email}")
        print(f"Contraseña ingresada: {password}")

        if tipo_usuario == 'cliente':
            # Crear cliente con solo correo y password para iniciar sesión
            cliente = Clientes(usuario=email, correo=email, password=password)
            tipo, id_usuario = cliente.iniciar_sesion()
            
            print(f"Tipo de usuario: {tipo}")
            print(f"ID de usuario: {id_usuario}")
            
            if tipo == 'cliente':
                messagebox.showinfo("Inicio de Sesión Exitoso", "Has iniciado sesión como Cliente")
                ventana_inicio_sesion.destroy()
                mostrar_menu_cliente(id_usuario)
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        
        elif tipo_usuario == 'empleado':
            # Crear una instancia de Empleados solo para iniciar sesión
            empleado = Empleados(usuario='', nombre='', apellidos='', edad=0, telefono='', correo=email, password=password, puesto='', titulo='', salario=0, fecha_nacimiento='', id_agencia=0)
            tipo, id_usuario = empleado.iniciar_sesion()
            
            print(f"Tipo de usuario: {tipo}")
            print(f"ID de usuario: {id_usuario}")
            
            if tipo == 'empleado':
                messagebox.showinfo("Inicio de Sesión Exitoso", "Has iniciado sesión como Empleado")
                ventana_inicio_sesion.destroy()
                mostrar_ventana_empleados(id_usuario)
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        
        else:
            messagebox.showerror("Error", "Selecciona un tipo de usuario.")
    # Crear la ventana de inicio de sesión
    ventana_inicio_sesion = tk.Toplevel()
    ventana_inicio_sesion.title("Inicio de Sesión")

    # Obtener las dimensiones de la ventana principal
    ancho_ventana_principal = ventana.winfo_width()
    alto_ventana_principal = ventana.winfo_height()
    x_ventana_principal = ventana.winfo_x()
    y_ventana_principal = ventana.winfo_y()

    # Dimensiones de la ventana de inicio de sesión
    ancho_inicio_sesion = 400
    alto_inicio_sesion = 400

    # Calcular la posición para centrar la ventana de inicio de sesión
    x = x_ventana_principal + (ancho_ventana_principal - ancho_inicio_sesion) // 2
    y = y_ventana_principal + (alto_ventana_principal - alto_inicio_sesion) // 2

    ventana_inicio_sesion.geometry(f"{ancho_inicio_sesion}x{alto_inicio_sesion}+{x}+{y}")
    ventana_inicio_sesion.configure(bg="cornsilk2")

    # Etiquetas y campos de entrada
    tk.Label(ventana_inicio_sesion, text="Correo Electrónico:", bg="cornsilk2").pack(pady=10)
    entry_email = tk.Entry(ventana_inicio_sesion)
    entry_email.pack(pady=5)

    tk.Label(ventana_inicio_sesion, text="Contraseña:", bg="cornsilk2").pack(pady=10)
    entry_password = tk.Entry(ventana_inicio_sesion, show="*")
    entry_password.pack(pady=5)

    tk.Label(ventana_inicio_sesion, text="Tipo de Usuario:", bg="cornsilk2").pack(pady=10)
    var_tipo_usuario = tk.StringVar(value='cliente')
    tk.Radiobutton(ventana_inicio_sesion, text="Cliente", variable=var_tipo_usuario, value='cliente', bg="cornsilk2").pack(pady=5)
    tk.Radiobutton(ventana_inicio_sesion, text="Empleado", variable=var_tipo_usuario, value='empleado', bg="cornsilk2").pack(pady=5)

    # Botón para intentar el inicio de sesión
    tk.Button(ventana_inicio_sesion, text="Iniciar Sesión", command=intentar_inicio_sesion).pack(pady=20)

def registrar():
    abrir_ventana_registro(ventana)

def main():
    global ventana  # Definir ventana como global para acceder en otras funciones
    ventana = tk.Tk()
    ventana.title("Proyecto Final")

    # Obtener el tamaño de la pantalla
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()

    # Tamaño de la ventana
    window_width = 950
    window_height = 700

    # Calcular la posición centrada
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Establecer tamaño y posición
    ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")
    ventana.configure(bg="cornsilk2")

    # Crear el título
    titulo = tk.Label(ventana, text="Sistema Gestor de Beneficiarios y Servicios Comunitarios", 
                      font=("Arial", 24, "bold"), bg="cornsilk2", padx=10, pady=20)
    titulo.pack()

    # Crear los botones
    btn_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=mostrar_inicio_sesion, font=("Arial", 16))
    btn_iniciar_sesion.pack(pady=10)

    btn_registrar = tk.Button(ventana, text="Registrar", command=registrar, font=("Arial", 16))
    btn_registrar.pack(pady=10)

    # Ejecutar el loop principal
    ventana.mainloop()

if __name__ == "__main__":
    main()



# # Configuración de la ventana
# ventana.title("Proyecto Final")

# # Obtener el tamaño de la pantalla
# screen_width = ventana.winfo_screenwidth()
# screen_height = ventana.winfo_screenheight()

# # Tamaño de la ventana
# window_width = 950
# window_height = 700

# # Calcular la posición centrada
# x = (screen_width - window_width) // 2
# y = (screen_height - window_height) // 2

# # Establecer tamaño y posición
# ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")
# #ventana.geometry("900x700+100+50")
# ventana.configure(bg="cornsilk2")

# # Crear el título
# titulo = tk.Label(ventana, text="Sistema Gestor de Beneficiarios y Servicios Comunitarios", 
#                   font=("Arial", 24, "bold"), bg="cornsilk2", padx=10, pady=20)
# titulo.pack()

# # Crear los botones
# btn_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=mostrar_inicio_sesion, font=("Arial", 16))
# btn_iniciar_sesion.pack(pady=10)

# btn_registrar = tk.Button(ventana, text="Registrar", command=registrar, font=("Arial", 16))
# btn_registrar.pack(pady=10)

# # Ejecutar el loop principal
# ventana.mainloop()
