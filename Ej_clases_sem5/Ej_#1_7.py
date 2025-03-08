# # # Ejercicio 7
# # # Clase Producto: Crea una clase Producto con atributos como nombre,precio y cantidadDisponible. 
# # # Incluye métodos para obtener y establecer los valores de estos atributos, 
# # # así como un método calcularTotal() que calcule el costo total de una cierta cantidad de productos.

class Producto():
    def __init__(self, nombre, precio, cantidadDisponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidadDisponible = cantidadDisponible
    def calcularTotal(self, cantidad):
        return self.precio * cantidad

nombre = input("Ingrese el nombre del producto: ")
precio = float(input("ingrese el precio del producto: "))
cantidadDisponible = 100
cantidadACalcular = int(input("ingrese cuantas unidades del producto desea cotizar: "))

producto = Producto(nombre, precio,cantidadDisponible)

if cantidadACalcular <= 100:
    print(f"El total a pagar por {cantidadACalcular} unidades de {producto.nombre} es: {producto.calcularTotal(cantidadACalcular):.2f}")
    
else:
    print("cantidad insuficiente de productos, elija una cantidad menor")

