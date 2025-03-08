# # # Clase Estudiante: Crea una clase Estudiante con atributos como nombre, edad, curso y 
# # # calificaciones (una lista o arreglo). Incluye métodos para agregar calificaciones, 
# # # calcular el promedio y determinar si el estudiante aprobó o reprobó el curso.



class Estudiante():
    def __init__(self, nombre, edad, curso, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = calificaciones
    def Promedio(self):
        promedio = 0
        for i in self.calificaciones:
            promedio = promedio + i 

        promedio = (promedio / len(self.calificaciones))
        if promedio < 3:
            print(f"su promedio es igual a {promedio:.2f}, usted reprobó la asignatura")
        elif promedio >= 3:
            print(f"su promedio es igual a {promedio:.2f}, usted aprobó la asignatura")
    def agregarCalificaciones(self, calificacion):
        self.calificaciones.append(calificacion)

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
curso = input("ingrese el nombre del curso ")

numero = int(input("Ingrese la cantidad de notas"))
notas = []

estudiante1 = Estudiante(nombre, edad, curso, notas)


for i in range (numero):
    
    estudiante1.agregarCalificaciones(float(input(f"ingrese la calificacion {i+1}")))

estudiante1.Promedio()