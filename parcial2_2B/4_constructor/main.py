
from coches import *


#Crear un objetos o instanciar la clase
print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)

#Mostrar los valores inicales del objeto o instancia de la clase
coche1.getInfo()



#Crear otro objeto e imprimir los valores
print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",180,150,6)
coche2.setColor("Blue Demon")
#Imprimir los valores del otro objeto
coche2.getInfo()

