# # 2. Clases FiguraGeométrica, Triángulo, Cuadrado:

# # Crea una clase base FiguraGeométrica con un método calcularArea().
# # Crea dos clases derivadas: Triángulo (con atributos base y altura) y Cuadrado (con un atributo lado).
# # Implementa el método calcularArea() en cada clase derivada para calcular el área de la figura correspondiente.

class FiguraGeométrica:
    def calcularArea(self):
        pass 


class Triángulo(FiguraGeométrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return (self.base * self.altura) / 2


class Cuadrado(FiguraGeométrica):
    def __init__(self, lado):
        self.lado = lado
    
    def calcularArea(self):
        return self.lado ** 2


triangulo = Triángulo(10, 5)
cuadrado = Cuadrado(4)

print(f"area del triángulo: {triangulo.calcularArea()} cm²")
print(f"area del cuadrado: {cuadrado.calcularArea()} cm²")