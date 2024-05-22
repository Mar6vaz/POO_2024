#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobados = 0
reprobados = 0


for i in range(1, 16):
    while True:
        try:
            calificacion = float(input(f"Introduce la calificación del alumno {i}: "))
            if 0 <= calificacion <= 100:
                break
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    
    if calificacion >= 60:
        aprobados += 1
    else:
        reprobados += 1

        
print(f"\nNúmero de alumnos aprobados: {aprobados}")
print(f"Número de alumnos reprobados: {reprobados}")

    