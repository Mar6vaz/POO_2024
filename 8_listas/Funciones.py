peliculas = []
def agregar_pelicula():
    pelicula = input("Ingrese el nombre de la película que desea agregar: ")
    peliculas.append(pelicula)
    print(f"Película '{pelicula}' agregada con éxito.")

def remover_pelicula():
    pelicula = input("Ingrese el nombre de la película que desea remover: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"Película '{pelicula}' removida con éxito.")
    else:
        print(f"Película '{pelicula}' no se encuentra en la lista.")

def consultar_peliculas():
    if peliculas:
        print("Listado de películas:")
        for pelicula in peliculas:
            print(f"- {pelicula}")
    else:
        print("No hay películas en la lista.")

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")