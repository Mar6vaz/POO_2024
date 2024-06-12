from Funciones import*

opcion = True
while opcion:
    print("\n\t..::CALCULADORA BASICA::..\n 1.-Suma \n 2.-Resta\n 3.-Multiplicacion\n 4.-Division\n 5.-Potencia\n 6.-Raiz Cuadrada\n 7.-SALIR")
    opcion = input("\tElige una opción: ").upper()

    if opcion in ["1", "2", "3", "4", "5"]:
        n1 = float(input("Numero #1: "))
        n2 = float(input("Numero #2: "))
        if opcion == "1" or opcion == "+":
            print(f"{n1} + {n2} = {n1 + n2}")
        elif opcion == "2" or opcion == "-":
            print(f"{n1} - {n2} = {n1 - n2}")
        elif opcion == "3" or opcion == "*":
            print(f"{n1} * {n2} = {n1 * n2}")
        elif opcion == "4" or opcion == "/":
            if n2 != 0:
                print(f"{n1} / {n2} = {n1 / n2}")
            else:
                print("No se puede dividir por cero")
        elif opcion == "5":
            print(f"{n1} ^ {n2} = {n1 ** n2}")
    elif opcion == "6":
        n = float(input("Ingrese un número para calcular su raíz cuadrada: "))
        if n >= 0:
            print(f"Raiz cuadrada de {n} = {n ** 0.5}")
        else:
            print("No se puede calcular la raíz cuadrada de un número negativo")
    elif opcion == "7":
        print("Terminaste la ejecución del programa")
        opcion = False
    else:
        print("Opción no válida")