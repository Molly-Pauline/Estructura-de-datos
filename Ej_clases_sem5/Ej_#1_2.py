# # # Ejercicio 2
# # # Clase CuentaBancaria: Crea una clase CuentaBancaria con atributos como titular 
# # # (un objeto de la clase Persona), saldo y númeroDeCuenta. Incluye métodos para depositar, 
# # # retirar y consultarSaldo. Asegúrate de manejar casos como retiros que exceden el saldo disponible.

class Persona():

    def __init__ (self, nombre, edad, genero):

        self.nombre = nombre
        self.edad = edad
        self.genero = genero


class Cuenta_Bancaria():
    def __init__ (self, persona, saldo, numeroDeCuenta):
        self.titular = persona
        self.saldo = saldo
        self.numeroDeCuenta = numeroDeCuenta

    def depositar(self, valor_deposito):
        self.saldo = self.saldo + valor_deposito

    def retirar(self, valor_retiro):

        if valor_retiro < self.saldo:
    
            self.saldo = self.saldo - valor_retiro
            print("Retiro exitoso")
        else:
            print("Saldo insuficiente")
    def consultarSaldo(self):
        print(self.saldo)

nombre = input("Ingrese el nombre: ")
edad = int(input("ingrese su edad: "))
genero = input("ingrese su genero: ")


titular = Persona(nombre, edad, genero)


numeroDeCuenta = int(input("ingrese su numero de cuenta: "))
saldo = float(input("ingrese su saldo actual: "))


cuenta = Cuenta_Bancaria(titular, saldo, numeroDeCuenta)

while (True):
    print("¿que transaccion realizará?\n1. Consultar saldo\n2. Depositar\n3. Retiro\n4. Finalizar")
    opcion = int(input())
    if opcion == 1:
        cuenta.consultarSaldo()
    elif opcion == 2:
        cuenta.depositar(float(input("ingrese valor a depositar")))
        print("Deposito exitoso")
    elif opcion == 3:
        cuenta.retirar(float(input("ingrese valor a retirar")))
    elif opcion == 4:
        print("transacción finalizada")
        break