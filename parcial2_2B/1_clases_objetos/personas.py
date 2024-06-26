#Clase 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

#Herencia La clase Estudiante hereda de la clase Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def informar_carrera(self):
        print(f"Soy {self.nombre} y estudio la carrera de {self.carrera}.")

#Instaciar objetos de la clase principal

persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

persona1.saludar()
persona2.saludar()

#Instaciar objetos de la clase secundaria 
estudiante = Estudiante("Ana", 20, "Ingeniería Informática")
estudiante.saludar()
estudiante.informar_carrera() 



