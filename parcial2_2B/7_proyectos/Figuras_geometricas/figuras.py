from clases import*

def main():
    rectangulo1 = Rectangulo(3, 4, True, 10, 20)
    print(rectangulo1.getInfo())
    
    circulo1 = Circulo(3, 3, True, 6)
    print(circulo1.getInfo())

if __name__ == "__main__":
    main()