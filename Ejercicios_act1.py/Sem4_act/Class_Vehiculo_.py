# Instrucciones
# Ejercicio 1:  Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; 
# la clase también debe contener dos métodos encender y arrancar. 
# Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado

# Ejercicio 2: Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo. 
# Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado

# Ejercicio 3: La clase Vehiculo, debe tener una propiedad llamada tipo (esta contendrá el tipo de vehiculo - Carro o Moto -), 
# esta propiedad debe ser seteada al momento de instanciar la clase Carro o Moto y al momento de imprimir el objeto debe indicar 
# el tipo de vehiculo junto con el texto mostrado anteriormente 

# Ejercicio 4: Hacer control de encendido de los vehiculos, para esto al momento de usar el método encender, se debe validar 
# el nivel de combustible del vehiculo (medida dada en galones) no este por debajo de un 10%, si este tiene un nivel muy bajo, 
# mostrar la advertencia que necesita ir a la gasolinera. 

# Ejercicio 5:  Debes hacer un ejercicio donde por medio de un método, el vehículo de marcha y haga un consumo de combustible a 
# medida que este funcione, cuando llegue a los niveles de combustible definidos en el punto anterior, muestre la advertencia y 
# si esta llega a cero, detenga la marcha 



# 1
class Vehiculo:
    def __init__(self, marca, combustible, tipo):
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo
        self.encendido = False
    
    def __str__(self):
        return self.tipo + " - Marca: " + self.marca + ", Combustible: " + str(self.combustible) + "%"
    
    def encender(self):
        if self.combustible < 10:
            print("Advertencia: Combustible bajo. Necesita ir a la gasolinera.")
        else:
            self.encendido = True
            print("El/La " + self.tipo + " " + self.marca + " está encendido.")

    def arrancar(self):
        if self.encendido:
            if self.combustible > 0:
                print("El/La " + self.tipo + " " + self.marca + " ha comenzado a moverse.")
                self.consumir_combustible()
            else:
                print("El " + self.tipo + " " + self.marca + " no puede moverse, está sin combustible.")
        else:
            print("Primero debe encender el/la " + self.tipo + " " + self.marca + ".")

    def consumir_combustible(self):
        while self.combustible > 0:
            self.combustible -= 5
            print("Combustible restante: " + str(self.combustible) + "%")
            if self.combustible < 10:
                print("Advertencia: Combustible bajo. Necesita ir a la gasolinera.")
            if self.combustible <= 0:
                self.combustible = 0
                print("El/La " + self.tipo + " " + self.marca + " se ha detenido por falta de combustible.")
                break

# 2:
class Moto(Vehiculo):
    def __init__(self, marca, combustible):
        Vehiculo.__init__(self, marca, combustible, "Moto")

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        Vehiculo.__init__(self, marca, combustible, "Carro")

# 3:
print("\n--- Creando instancias de vehículos ---")
moto1 = Moto("Kawasaki", 40)
carro1 = Carro("Mazda", 30)

print("\n--- Estado inicial de los vehículos ---")
print(moto1)
print(carro1)

# 4:
print("\n--- Intentando encender los vehículos ---")
moto1.encender()
carro1.encender()

# 5:
print("\n--- Intentando arrancar y consumir combustible ---")
moto1.arrancar()
carro1.arrancar()
