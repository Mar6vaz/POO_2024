# Esta estructura de contro evalua una condicion si la condicion se cumple se ejecuta la o las instrucciones contenidas dentro de ella 

# Esta estructura tiene 4 varientes
# 1.- if simple
# 2.- if compuesto
# 3.- if anidado
# 4.- if con el elif

#ejemplo 1 if simple

# color="rojo"

# if color=="rojo":
#     print("Soy el color rojo")

#ejemplo 2 if compuesto

# color="rojo"

# if color=="rojo":
#     print("Soy el color rojo")
# else:
#     print("No soy el color rojo")   


#ejemplo 3 if anidado

# color="rojo"

# if color=="rojo":
#     print("Soy el color rojo")
#     if color!="rojo":
#       print("No soy rojo color rojo")
# else:
#     print("No soy el color rojo")   

#ejemplo 4 if y elif 

color=input("Ingresa el color: ")

if color=="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo")   
elif color=="azul":
    print("Soy el color azul")    
elif color=="negro":
    print("Soy el color negro")   
else:
     print("No soy ninguno de los colores anteriores")
 


