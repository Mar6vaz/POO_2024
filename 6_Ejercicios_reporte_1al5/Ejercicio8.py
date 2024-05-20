#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

numero = float(input("Ingresen el numero: "))

porcentaje = float(input("Ingrese el porcentaje (%): "))

resultado = (porcentaje / 100) * numero

print(f"{porcentaje}% de {numero} es {resultado}")

