# # # Ejercicio 5
# # # Clase Libro: Crea una clase Libro con atributos como título, autor, género y 
# # # añoDePublicación. Incluye métodos para obtener y establecer los valores de 
# # # estos atributos, así como un método mostrarDetalles() que imprima la información del libro.

class Libro ():
    def __init__(self,titulo, autor, genero, añoDePublicacion):

        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.añoDePublicacion = añoDePublicacion
    
    def presentar_libro (self):
        print(f"El nombre del libro es {self.titulo}, fué escrito por {self.autor}, pertenece al genero de {self.genero} y se publicó en el año {self.añoDePublicacion}")

titulo = input("Ingrese el titulo del libro: ")
autor = input("ingrese el nombre autor del libro: ")
genero = input("ingrese el genero literario al que el libro pertenece: ")
añoDePublicacion = int(input("ingrese el año de publicacion del libro: "))

obra1 = Libro(titulo, autor, genero, añoDePublicacion)
obra1.presentar_libro()
