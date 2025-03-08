# # 1.  Clases Empleado, Gerente, Desarrollador:

# # Crea una clase base Empleado con atributos como nombre, salario y departamento, y un método trabajar().
# # Crea dos clases derivadas: Gerente (con un atributo adicional equipo que es una lista de empleados) 
# # y Desarrollador (con un atributo adicional lenguajeDeProgramación).
# # Implementa el método trabajar() de manera específica para cada tipo de empleado, reflejando sus responsabilidades 
# # particulares. Por ejemplo, el Gerente podría supervisarAEquipo() y el Desarrollador podría escribirCódigo().

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando en el departamento de {self.departamento}")


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo
    
    def supervisarAEquipo(self):
        print(f"{self.nombre} está supervisando a su equipo: {', '.join(self.equipo)}")
    
    def trabajar(self):
        print(f"{self.nombre} está gestionando el equipo en el departamento de {self.departamento}")
        self.supervisarAEquipo()


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion
    
    def escribirCodigo(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}")
    
    def trabajar(self):
        print(f"{self.nombre} está desarrollando software en el departamento de {self.departamento}")
        self.escribirCodigo()

gerente = Gerente("Molly", 500000000, "Administración", ["Andres", "Luis"])
desarrollador = Desarrollador("andres", 4000000, "TI", "Python")

gerente.trabajar()
desarrollador.trabajar()