# # # Ejercicio 1
# # # Clase Persona: Crea una clase Persona con atributos como nombre, edad y género. 
# # # Incluye métodos para obtener y establecer los valores de estos atributos, 
# # # así como un método presentarse() que imprima una breve descripción de la persona.
class Persona():

    def __init__ (self, nombre, edad, genero):

        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    
    def presentarse (self):
        print(f"hola, mi nombre es {self.nombre}, mi edad es {self.edad} y mi genero es {self.genero}")

nombre = input("Ingrese el nombre: ")
edad = int(input("ingrese su edad: "))
genero = input("ingrese su genero: ")
persona1 = Persona(nombre, edad, genero)
persona1.presentarse()


