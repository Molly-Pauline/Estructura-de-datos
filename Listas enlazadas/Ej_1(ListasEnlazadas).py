# # Ejercicio 1: Sistema para el Control de Animales en un Zoológico
# # Obj: Diseñar e implementar un sistema básico para controlar el registro de animales en un zoológico utilizando listas enlazadas.
    # # Requisitos:
        # # Clase Animal:
            # # Crear una clase Animal que contenga los siguientes atributos básicos: /
            # # Nombre /
            # # Edad /
            # # Tipo de Animal (por ejemplo: Águila, Pantera, Vaca, etc.) /
        # # Implementar métodos básicos como constructores, getters y setters. /
        # # Lista Enlazada:
            # # Crear una lista enlazada que permita agregar animales al listado.
            # # Asegurar que no se permita añadir animales repetidos (animales con el mismo nombre y tipo).
            # # Mostrar Animales:
            # # Implementar dos métodos diferentes para mostrar todos los animales registrados:
                # # Un método iterativo (usando un bucle).
                # # Un método recursivo.



class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_especie(self):
        return self.__especie

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_tipo(self, especie):
        self.__especie = especie

    def __str__(self):
        return f"{self.__nombre} - {self.__edad} años - {self.__especie}"


class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None



class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        if self.buscar_animal(animal.get_nombre(), animal.get_edad(), animal.get_especie()):
            print(f"\n El animal {animal.get_nombre()} ya está registrado con la misma edad y especie.")
            return  
        
        nuevo_nodo = Nodo(animal)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

        print("\n¡¡¡Animal agregado correctamente!!!.")

    def buscar_animal(self, nombre, edad, especie):
        actual = self.cabeza
        while actual:
            if (actual.animal.get_nombre() == nombre and 
                actual.animal.get_edad() == edad and 
                actual.animal.get_especie() == especie):
                return True
            actual = actual.siguiente
        return False

    def mostrar_animales_iterativo(self):
        if self.cabeza is None:
            print("\nNo hay animales registrados.")
            return
        actual = self.cabeza
        while actual:
            print(actual.animal)
            actual = actual.siguiente

    def mostrar_animales_recursivo(self, nodo=None):
        if nodo is None:  
            nodo = self.cabeza  
        
        if nodo is None:  
            print("\nNo hay animales registrados.")
            return
        
        print(nodo.animal)
        
        if nodo.siguiente is not None:  
            self.mostrar_animales_recursivo(nodo.siguiente)



def menu():
    zoologico = ListaEnlazada()
    
    while True:
        print("\n Menú del Zoológico")
        print("1. Agregar un animal")
        print("2. Mostrar animales (Iterativo)")
        print("3. Mostrar animales (Recursivo)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("\n Ingrese el nombre del animal: ").strip()
            edad = input("\n Ingrese la edad del animal: ").strip()
            especie = input("\n Ingrese la especie del animal (perro, gato, etc.): ").strip()
            
            if nombre and edad.isdigit() and especie:
                zoologico.agregar_animal(Animal(nombre, int(edad), especie))
            else:
                print("\n Datos inválidos. Intente nuevamente.")

        elif opcion == "2":
            print("\n Animales en el zoológico (Iterativo):")
            zoologico.mostrar_animales_iterativo()

        elif opcion == "3":
            print("\n Animales en el zoológico (Recursivo):")
            zoologico.mostrar_animales_recursivo()

        elif opcion == "4":
            print("\nSaliendo del sistema.")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

menu()