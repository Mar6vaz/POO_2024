#Los tipos de datos mas comunes en python son:
#simples o primitivos
#int(entero)
#float(real)
#bool(logico)

#estructurados
#str(cadena)
#list(lista)
#tuple
#dict(como un objeto)

#Ejemplos variables primitivos
entero=23
float=3.1416
logico=False

#estructurados
palabra="Hola"
palabra2="@"
list=[10,20,30,40]
list2=[True,100,3.3,"Que tal",'9']
tuple=("Hola","Que","Tal")
dict={
    "nombre":"Daniel el traavieso",
    "apellidos":"Hernandez Gomez",
    "edad":20,
    "estatura":1.7
}

#Mostrar el tipo de datos de cada identificador
print(type(entero))
print(type(float))
print(type(logico))
print(type(palabra))
print(type(palabra2))
print(type(list))
print(type(tuple))
print(type(dict))