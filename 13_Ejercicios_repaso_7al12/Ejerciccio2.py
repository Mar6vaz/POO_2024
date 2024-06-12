# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

lista=[]
# WHILE
# seg=True
# while len(lista)<=120:
#     añada=input("Ingrese un elemento para agregar a la lista: ")
#     lista.append(añada)
#     print(lista)
#     resp=input("¿Quieres seguir agregando valores? (si/no): ").strip().lower() #Elimina espacios adicionales, convierte a minusculas
    
#     if  resp=="no":
#         print("Ejecucion del SW terminado")
#         break
        
        

    
#FOR 
cantidad=len(lista)
for cantidad in range(121):
   añada=input("Ingrese un elemento para agregar a la lista: ")
   lista.append(añada)
   print(lista)
   resp=input("¿Quieres seguir agregando valores? (si/no): ").strip().lower() #Elimina espacios adicionales, convierte a minusculas
    
   if  resp=="no":
     print("Ejecucion del SW terminado")
     break