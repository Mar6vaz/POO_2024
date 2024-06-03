import datetime

class saludo():
    #Metodo magico para inicializar un objeto
    def __init__(self, nombre):
        self.nombre = nombre
        self.hora = datetime.datetime.now().hour
        self.minutos = datetime.datetime.now().minute
    #Metodo magico para mostrar los datos de un objeto en String 

    def __str__(self):
        return f"Hola {self.nombre} son las {self.hora}:{self.minutos}h"
    #Metodo para sumar dos objetos 
    def __add__(self, otro):
        return f"Hola {self.nombre} son las {self.hora}:{self.minutos}h y has recibido {otro.visitas} visitas"
    #Metdo para destruir un objeto 
    def __del__(self):
        print("Objeto destruido")
    
class visitas():
    def __init__(self, visitas):
        self.visitas=visitas
    
saludar = saludo("Leonardo")

visitas=visitas("100")
saludo_visitas=saludar + visitas
print(saludo_visitas)

