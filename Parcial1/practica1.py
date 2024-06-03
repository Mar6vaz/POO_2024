total_trabajadores = 0
total_sueldos = 0

while True: 
    nombre = input("Ingrese el nombre del trabajador: ")
    horas_trabajadas = float(input("Ingrese las horas trabajadas a la semana: "))
    dias_trabajados = int(input("Ingrese los días trabajados a la semana: "))
    sueldo_por_hora = float(input("Ingrese el sueldo por hora: "))

    sueldo_semanal = horas_trabajadas * sueldo_por_hora * dias_trabajados
    sueldo_mensual = sueldo_semanal * 4

    print(f"Sueldo semanal de {nombre}: {sueldo_semanal}")
    print(f"Sueldo mensual de {nombre}: {sueldo_mensual}")
    if sueldo_mensual <= 10000:
        print("Obrero tipo A")
    elif 10000 < sueldo_mensual < 15000:
        print("Obrero tipo B")
    else:
        print("Sin categoría")

    total_trabajadores += 1
    total_sueldos += sueldo_mensual
    
    
    otra_captura = input("¿Desea otra captura? (si/no): ")
    if otra_captura !="si":
        break 


print(f"Total de trabajadores capturados: {total_trabajadores}")
print(f"Total de sueldos de todos los trabajadores: {total_sueldos}")

     

