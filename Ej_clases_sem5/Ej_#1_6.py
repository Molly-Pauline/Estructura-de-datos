# # # Ejercicio 6
# # # Clase Canción: Crea una clase Canción con atributos como título, artista, álbum y duración. 
# # # Incluye métodos para obtener y establecer los valores de estos atributos, así como un método 
# # # reproducir() que simule la reproducción de la canción (puedes simplemente imprimir un mensaje).

class Cancion():
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion
    
    def presentar_cancion (self):
        print(f"El titulo de la canción es {self.titulo}, el artista que la interpreta es {self.artista}, pertenece al album {self.album} y su duracion es {self.duracion} minutos")

titulo = input("Ingrese el titulo de la cancion: ")
artista = input("ingrese el nombre artista: ")
album = input("ingrese el album al que pertenece la canción: ")
duracion = int(input("ingrese la duracion de la canción: "))

reproducir = Cancion(titulo, artista, album, duracion)
reproducir.presentar_cancion()

while (True):
    print("¿desea escuchar la canción?\n1. Si\n2. No")
    opcion = int(input())
    if opcion == 1:
        reproducir.presentar_cancion()
        print("se está reproduciendo la canción")
    elif opcion == 2:
        print("Entendido, finalizando acción")
        break