#AQUI ESTAN LOS MENUS DE OPCIONES

from Animales import mascota
from Personas import usuarios 
from Servicios import veterinaria
from funciones import *
from conexionBD import obtener_conexion 


def menu_inicial():
    while True:
        limpiarPantalla()
        print("""
             ....::::::Sistema Gestión Veterinaria::::::....
          1- Veterinaria
          2- Empleados
          3- Clientes
          4- Animales
          5- Citas
          6- Servicios
          7- Salir
        """)
        opcion=input("Eliga una opcion: ").upper()

        if opcion == '1' or opcion == 'VETERINARIA':
            menu_veterinaria()

        elif opcion == '2' or opcion == 'EMPLEADOS':
            menu_empleados()

        elif opcion == '3' or opcion == 'CLIENTES':
            menu_clientes()

        elif opcion == '4' or opcion == 'ANIMALES':
            menu_animales()

        elif opcion == '5' or opcion == 'CITAS':
            menu_citas()

        elif opcion == '6' or opcion == 'SERVICIOS':
            menu_servicios()

        elif opcion == '7' or opcion == 'SALIR':
            print("¡Que tenga un buen día!...Ha salido del sistema")
            break
        else:
            print("\t Opcion no váida....Porfavor intente de nuevo")
            esperarTecla()


def menu_veterinaria():
    while True:
        limpiarPantalla()
        print("""
        .....:::::Gestión Veterinarias:::::...
          1) Ver Veterinarias
          2) Actualizar datos
          3) Regresar
        """)

        opcion = input("Eliga una opción: ").upper()

        if opcion == '1' or opcion=='VER':
            limpiarPantalla()
            print("\t\t¡He aqui todas las Veterinarias activas!")
            print("")
            
            obj_veter = veterinaria.Veterinarias(None, None, None, None)  
            obj_veter.mostrar_detalles()
            esperarTecla()


        elif opcion == '2' or opcion== 'ACTUALIZAR':
            limpiarPantalla()
            print("\t\t¡Actualizaré los datos de la Veterinaria!")
            print("")
            
            identif = input("Ingrese el ID de la veterinaria a actualizar: ")
            obj_veter = veterinaria.Veterinarias(identif, '', '', '')
            obj_veter.actualizar_detalles(identif)
            esperarTecla()


        elif opcion == '3' or opcion=='REGRESAR':
            break

        else:
            print("Opción no válida.... por favor intente de nuevo")
            esperarTecla()


    
def menu_empleados():
    while True:
        limpiarPantalla()
        print("""
        .....:::::Gestión Empleados:::::...
          1) Mostrar disponibles
          2) Agregar nuevo empleado
          3) Actualizar campos
          4) Eliminar empleado
          5) Regresar
        """)
        opcion = input("Eliga una opción: ").upper()

        if opcion == '1' or opcion == 'MOSTRAR':
            limpiarPantalla()
            print("\t\t ¡Te mostraré los empleados activos!")
            print("")
          
            obj_empleado=usuarios.Empleados(None, None, None, None, None, None, None)
            obj_empleado.mostrar_empleados()
            esperarTecla()
            

        elif opcion == '2' or opcion == 'AGREGAR':
            limpiarPantalla()
            print("\t\t ¡Agregar un nuevo empleado!")
            print("")
            nombre = input("Ingrese el nombre del empleado: ")
            direccion = input("Ingrese la dirección del empleado: ")
            telefono = input("Ingrese el teléfono del empleado: ")
            puesto = input("Ingrese el puesto del empleado: ")

            while True: 
                try: 
                    salario = float(input("Ingrese el salario del empleado: "))
                    break  
                except ValueError:
                    print("Error: El salario debe ser un número válido. Por favor, ingrese un valor numérico.")

            id_veterinaria = input("Ingrese el ID de la veterinaria a la que pertenece el empleado: ")

            try:
               
                obj_empleado = veterinaria.Veterinarias(None, None, None, None)
                obj_empleado.agregar_empleado(nombre, direccion, telefono, puesto, salario, id_veterinaria)
            except Exception as e:
                print(f"Ocurrió un error: {e}")
            esperarTecla()
            
                
            


        elif opcion == '3' or opcion == 'ACTUALIZAR':
            limpiarPantalla()
            print("\t\t¡Actualizaré los datos del empleado activo!")
            print("")
            
            id_empleado =input("Ingrese el ID del empleado a actualizar: ")
            obj_empleado = usuarios.Empleados(id_empleado, '', '', '', '', '', '') 
            obj_empleado.actualizar_datos(id_empleado)
            esperarTecla()


        elif opcion == '4' or opcion == 'ELIMINAR':
            limpiarPantalla()
            print("\t\t¡Eliminaras un empleado!")
            print("")
          
            id_empleado =input("Ingrese el ID del empleado a eliminar: ")
            
            obj_veterinaria = veterinaria.Veterinarias(None, None, None, None) 
            obj_veterinaria.eliminar_empleado(id_empleado)
            esperarTecla()

        elif opcion == '5' or opcion == 'REGRESAR':
            break

        else:
            print("Opción no válida.... por favor intente de nuevo")
            esperarTecla()

def menu_clientes():
     while True:
        limpiarPantalla()
        print("""
        .....:::::Gestión Clientes:::::...
          1) Mostrar cliente
          2) Agregar cliente
          3) Actualizar cliente
          4) Eliminar cliente
          5) Regresar
        """)
        opcion=input("Eliga una opcion: ").upper()

        if opcion == '1' or opcion == 'MOSTRAR':
            limpiarPantalla()
            print("\t\t ¡Te mostraré los clientes activos!")
            print("")
            #Crear una instancia de la clase 
            obj_cliente=usuarios.Clientes(None, None, None, None, None)
            obj_cliente.mostrar_cliente()
            esperarTecla()
            

        elif opcion == '2' or opcion == 'AGREGAR':
            limpiarPantalla()
            print("\t\t¡Bienvenido nuevo cliente!")
            print("\tServicios de calidad a un solo paso")
            print("")

            
            nombre = input("Nombre del cliente: ")
            direccion = input("Dirección del cliente: ")
            telefono = input("Teléfono del cliente: ")
            tipo = input("Tipo de cliente (particular, empresa, etc.): ")

          
            obj_cliente = veterinaria.Veterinarias(None, None, None, None)
            cliente_id=obj_cliente.agregar_cliente(nombre, direccion, telefono, tipo)
    

            if cliente_id:
                
                while True:
                    agregar_mascota = input("¿Desea agregar una mascota para este cliente? (s/n): ").lower()
                    if agregar_mascota == 's':
                       
                        nombre_mascota = input("Nombre de la mascota: ")
                        especie_mascota = input("Especie de la mascota: ")
                        raza_mascota = input("Raza de la mascota: ")
                        edad_mascota = input("Edad de la mascota: ")

                        obj_animal = usuarios.Clientes(None, None, None, None, None)
                        obj_animal.agregar_animal(nombre_mascota, especie_mascota, raza_mascota, edad_mascota, cliente_id)
                        esperarTecla()

                    elif agregar_mascota == 'n':
                        break
                    else:
                        print("Opción no válida. Por favor, elija 's' o 'n'.")
            else:
                print("No se pudo agregar el cliente. No se procederá a agregar mascotas.")
            esperarTecla()

        elif opcion == '3' or opcion == 'ACTUALIZAR':
            limpiarPantalla()
            print("\t\t¡Actualizaré los datos del cliente!")
            print("")
            # Solicitar ID del cliente a actualizar
            cliente_id =input("Ingrese el ID del cliente a actualizar: ")
            obj_cliente = usuarios.Clientes(cliente_id, '', '', '', '') #creacion de la instancia de la clase
            # Actualizar detalles de empleado activo
            obj_cliente.actualizar_datos(cliente_id)
            esperarTecla()
        

        elif opcion == '4' or opcion == 'ELIMINAR':
            limpiarPantalla()
            print("\t\t¡Eliminaras un cliente!")
            print("")
            
            cliente_id =input("Ingrese el ID del cliente a eliminar: ")
           
            obj_veterinaria = veterinaria.Veterinarias(None, None, None, None) 
            obj_veterinaria.eliminar_cliente(cliente_id) 
            esperarTecla()

        elif opcion == '5' or opcion == 'REGRESAR':
            print("")
            break
        else:
            print("Opcion no válida.... porfavor intente de nuevo")
            esperarTecla()

     
def menu_animales():
    while True:
        limpiarPantalla()
        print("""
        .....:::::Gestión Animales:::::...
          1) Mostrar Mascotas 
          2) Agregar Mascota
          3) Actualizar Datos
          4) Eliminar Mascota
          5) Regresar
        """)
        opcion=input("Eliga una opcion: ").upper()

        if opcion == '1' or opcion == 'MOSTRAR':
            limpiarPantalla()
            print("\t\t ¡Te mostraré detalles de mascotas por dueño!")
            print("")
            cliente_id = input("Ingrese el ID del cliente para mostrar: ")
           
            obj_animal = mascota.Animales(None, None, None, None, None, cliente_id)
            obj_animal.mostrar_historial(cliente_id)
            esperarTecla()

        elif opcion == '2' or opcion == 'AGREGAR':
            limpiarPantalla()
            print("\t\t ¡Agregarás a una mascota por cliente activo!")
            print("")
            cliente_id = input("Ingrese el ID del cliente: ")
             
            nombre_mascota = input("Nombre de la mascota: ")
            especie_mascota = input("Especie de la mascota: ")
            raza_mascota = input("Raza de la mascota: ")
            edad_mascota = input("Edad de la mascota: ")
            
           
            obj_animal = usuarios.Clientes(None, None, None, None, None)
            obj_animal.agregar_animal(nombre_mascota, especie_mascota, raza_mascota, edad_mascota, cliente_id)
            esperarTecla()
            

        elif opcion == '3' or opcion == 'ACTUALIZAR':
            limpiarPantalla()
            print("\t\t¡Actualizarás los datos de una mascota!")
            print("")
            id_mascota = input("Ingrese el ID de la mascota existente: ")

            
            obj_animal = mascota.Animales(None,None,None,None,None,None)  
            obj_animal.actualizar_historial(id_mascota)
            esperarTecla()

                    

        elif opcion == '4' or opcion == 'ELIMINAR':
            limpiarPantalla()
            print("\t\t ¡Eliminarás una mascota!")
            id_animal = input("Ingrese el ID de la mascota que desea eliminar: ")
            
            obj_cliente = usuarios.Clientes(None, None, None, None, None)  
            obj_cliente.eliminar_animal(id_animal)
            esperarTecla()

            

        elif opcion == '5' or opcion == 'REGRESAR':
            print("")
            break
        else:
            print("Opcion no válida.... porfavor intente de nuevo")
            esperarTecla()
        
def menu_servicios():
    while True:
        limpiarPantalla()
        print("""
        .....:::::Gestión Servicios:::::...
          1) Mostrar disponibles 
          2) Actualizar costos
          3) Agregar Servicios
          4) Eliminar servicios
          5) Regresar
        """)
        opcion=input("Eliga una opcion: ").upper()

        if opcion == '1' or opcion == 'MOSTRAR':
            limpiarPantalla()
            print("\t\t¡He aqui todas las Veterinarias activas!")
            
            obj_servicios = veterinaria.Servicios(None, None, None, None, None)  
            obj_servicios.mostrar_servicios()
            esperarTecla()

        elif opcion == '2' or opcion == 'ACTUALIZAR':
            limpiarPantalla()
            print("\t\t ¡Actualizarás el costo del servicio que desees!")
            print("")
            id_servicio=input("Ingrese el ID del servicio: ")
            
            obj_servicios=veterinaria.Servicios(id_servicio, None, None, None, None)
            obj_servicios.actualizar_costo(id_servicio)
            esperarTecla()


        elif opcion == '3' or opcion == 'AGREGAR':
            limpiarPantalla()
            print("\t\t ¡Agregar un nuevo servicio!")
            print("")
            nombre = input("Ingrese el nombre del servicio: ")
            descripcion = input("Ingrese la descripción del servicio: ")
            costo = input("Ingrese el costo del servicio: ")
            id_veterinaria = input("Ingrese el ID de la veterinaria: ")
             
            obj_servicios=veterinaria.Veterinarias(None, None, None, None)
            obj_servicios.agregar_servicio(nombre, descripcion, costo, id_veterinaria)
            esperarTecla()

        elif opcion == '4' or opcion == 'ELIMINAR':
            limpiarPantalla()
            print("\t\t ¡Eliminarás un servicio!")
            id_servicio = input("Ingrese el ID del servicio que desea eliminar: ")
            # Crear una instancia de la clase veterinarias
            obj_veterinaria = veterinaria.Veterinarias(None, None, None, None)  # O instancia adecuada
            obj_veterinaria.eliminar_servicio(id_servicio)
            esperarTecla()

        elif opcion == '5' or opcion == 'REGRESAR':
            print("")
            break
        else:
            print("Opcion no válida.... porfavor intente de nuevo")
            esperarTecla()

def menu_citas():
    while True:
        limpiarPantalla()
        print("""
                  ....:::::Gestion Citas::::::....
        ¿Que desea hacer?
            1) Programar Cita
            2) Confirmar Cita 
            3) Cancelar Cita
            4) Mostrar Citas
            5) Regresar
        """)
        opcion=input("Eliga una opcion: ").upper()

        if opcion == '1' or opcion == 'PROGRAMAR':
            limpiarPantalla()
            print("\tProgramar una cita")
            print("")
            # Pedir datos
            id_cliente = input("Ingrese el ID del cliente: ")
            id_animal = input("Ingrese el ID del animal: ")
            id_empleado = input("Ingrese el ID del empleado: ")
            id_servicio = input("Ingrese el ID del servicio: ")
            # Crear una instancia de la clase Citas y agregar la cita
            obj_cita = veterinaria.Citas(None, None, None, None, None, None)
            obj_cita.programar_cita(id_cliente, id_animal, id_empleado, id_servicio)
            esperarTecla()
      

        elif opcion == '2' or opcion == 'CONFIRMAR':
            limpiarPantalla()
            print("\t\t!Confirmemos una cita ya programada!")
            print("")
            id_cita = input("Ingrese el ID de la cita que desea confirmar: ")
            obj_cita = veterinaria.Citas(None, None, None, None, None, None)  
            obj_cita.confirmar(id_cita)
            esperarTecla()

        elif opcion == '3' or opcion == 'CANCELAR':
            limpiarPantalla()
            print("\t\t!Cancelarás una cita ya programada!")
            print("")
            id_cita = input("Ingrese el ID de la cita a cancelar: ")
            obj_cita = veterinaria.Citas(None, None, None, None, None, None)
            obj_cita.cancelar_cita(id_cita)
            esperarTecla()

        elif opcion == '4' or opcion== 'MOSTRAR':
            limpiarPantalla()
            print("\t\t Mostraré Citas por Cliente")
            print("")
            id_cliente = input("Ingrese el ID del cliente para mostrar sus citas: ").strip() 
            
            obj_cita = veterinaria.Citas(None, None, None, None, None, None)
            obj_cita.mostrar_citas(id_cliente)
            esperarTecla()

        elif opcion == '5' or opcion == 'REGRESAR':
            break

        else:
            print("Opcion no válida.... porfavor intente de nuevo")
            esperarTecla()



if __name__ == "__main__":
    menu_inicial()


