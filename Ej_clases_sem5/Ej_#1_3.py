# # # Ejercicio 3
# # # Clase Rectángulo: Crea una clase Rectángulo con atributos base y altura. 
# # # Incluye métodos para calcular el área y el perímetro del rectángulo.

class Rectangulo ():

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura
    
    def area(self):
        area = self.base * self.altura
        print(f"el valor del area del rectangulo es de {area} cm")
        
    def perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        print(f"el valor del perimetro del rectangulo es {perimetro} cm")
        
base = float(input("Ingrese el valor de la base del rectangulo (en centimetros): "))
altura = float(input("Ingrese el valor de la altura del rectangulo (en centimetros): "))

operacion = Rectangulo (base, altura)

while (True):
    print("¿que operación desea realizar?\n1. Calcular area\n2. Calcular perimetro\n3. Finalizar")
    opcion = int(input())
    if opcion == 1:
        operacion.area()
    elif opcion == 2:
        operacion.perimetro()
    elif opcion == 3:
        print("Calculo finalizado")
        break