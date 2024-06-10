"""

 
 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""

alumnos={
    "nombre":"Daniel",
    "apellidos":"Fernandez Hernandez",
    "especialidad":"TI",
    "area":"Desarrollo de SW Multiplataforma",
    "semestres":11,
    "duracion":3.8
}

print(alumnos)

print(alumnos["nombre"])

#Agregar elementos

alumnos["telefono"]=6181234567
print(alumnos)


#Actualizar elementos
alumnos.update({"telefono":6182334567})
print(alumnos)

#Eliminar elementos
alumnos.pop("semestres")
print(alumnos)

#Recorrer el dicccionario

for i in alumnos:
    print(f"{i} : {alumnos[i]}")