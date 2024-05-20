#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

for tabla in range(1, 11):
    
    print(f"Tabla del {tabla}:")
    
    
    for multiplicador in range(1, 11):
        
        resultado = tabla * multiplicador
        
        
        print(f"{tabla} x {multiplicador} = {resultado}")
    
    
    print()
