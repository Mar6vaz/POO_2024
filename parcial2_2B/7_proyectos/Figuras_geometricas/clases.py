class Figura:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible
    
    def estaVisible(self):
        return self.visible
    
    def ocultar(self):
        self.visible = False
    
    def mostrar(self):
        self.visible = True
    
    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
    
    def calcularArea(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
    def getInfo(self):
        return f"Posición: ({self.x}, {self.y}), Visible: {self.visible}"

class Rectangulo(Figura):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.alto = alto
        self.ancho = ancho
    
    def calcularArea(self):
        return self.alto * self.ancho
    
    def getInfo(self):
        return f"Rectángulo -> {super().getInfo()}, Alto: {self.alto}, Ancho: {self.ancho}, Área: {self.calcularArea()}"

class Circulo(Figura):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.radio = radio
    
    def calcularArea(self):
        import math
        return math.pi * self.radio ** 2
    
    def getInfo(self):
        return f"Círculo -> {super().getInfo()}, Radio: {self.radio}, Área: {self.calcularArea()}"
