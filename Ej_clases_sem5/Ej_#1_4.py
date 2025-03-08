# # # Ejercicio 4
# # # Clase Círculo: Crea una clase Círculo con un atributo radio. 
# # # Incluye métodos para calcular el área y la circunferencia del círculo.

import math
class Circulo ():
    def __init__(self, radio):
        self.radio = radio

    def area (self):
        area = math.pi * self.radio ** 2
        print(f"el valor del area del circulo es de {area:.2f} cm")
    
    def circunferencia (self):
        circunferencia = 2 * math.pi * self.radio
        print(f"el valor de la circunferencia del circulo es de {circunferencia:.2f} cm")

radio = float(input("Ingrese el valor del radio del círculo (en centímetros): "))

operacion = Circulo (radio)

while (True):
    print("¿que operación desea realizar?\n1. Calcular area\n2. Calcular circunferencia\n3. Finalizar")
    opcion = int(input())
    if opcion == 1:
        operacion.area()
    elif opcion == 2:
        operacion.circunferencia()
    elif opcion == 3:
        print("Calculo finalizado")
        break