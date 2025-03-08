# 3. Clases Electrodoméstico, Lavadora, Refrigerador:

# # Crea una clase base Electrodoméstico con atributos como marca, modelo y consumoEnergético, y un método encender().
# # Crea dos clases derivadas: Lavadora (con un atributo adicional capacidad) y 
# # Refrigerador (con un atributo adicional tieneCongelador).
# # Implementa el método encender() de manera específica para cada tipo de electrodoméstico, 
# # considerando sus funciones particulares. Por ejemplo, la Lavadora podría iniciarCicloDeLavado() 
# # y el Refrigerador podría regularTemperatura().

class Electrodomestico:
    def __init__(self, marca, modelo, consumo_energia):
        self.marca = marca
        self.modelo = modelo
        self.consumo_energia = consumo_energia
    
    def encender(self):
        print(f"El {self.marca} {self.modelo} está listo para usarse")


class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energia, capacidad):
        super().__init__(marca, modelo, consumo_energia)
        self.capacidad = capacidad
    
    def iniciar_ciclo_lavado(self):
        print(f"La lavadora {self.marca} {self.modelo} está lavando ropa (capacidad: {self.capacidad} kg)")
    
    def encender(self):
        print(f"La lavadora {self.marca} {self.modelo} está encendida")
        self.iniciar_ciclo_lavado()


class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energia, tiene_congelador):
        super().__init__(marca, modelo, consumo_energia)
        self.tiene_congelador = tiene_congelador
    
    def regular_temperatura(self):
        print(f"El refrigerador {self.marca} {self.modelo} está enfriando bien")
    
    def encender(self):
        print(f"El refrigerador {self.marca} {self.modelo} está encendido")
        self.regular_temperatura()


lavadora = Lavadora("LG", "TurboWash", "A", 10)
refrigerador = Refrigerador("Samsung", "CoolMax", "B", True)

lavadora.encender()
refrigerador.encender()