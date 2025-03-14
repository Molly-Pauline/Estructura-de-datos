# # Ejercicio 2: Sistema de Gestión de Tareas
# # Objetivo: Diseñar e implementar un sistema básico para gestionar tareas mediante listas enlazadas.
    # # Requisitos:
        # # Cada tarea debe tener:
            # # Descripción (texto breve)
            # # Prioridad (valor numérico, por ejemplo: 1 alta, 3 baja)
            # # Fecha de vencimiento
        # # El sistema debe permitir:
            # # Agregar una tarea:
            # # El usuario puede ingresar los detalles de la nueva tarea.
            # # Eliminar una tarea:
            # # Eliminar una tarea especificando la descripción o la posición en la lista.
            # # Mostrar todas las tareas:
                # # Las tareas deben mostrarse ordenadas:
                # # Primero por prioridad (de alta a baja).
                # # En caso de empate, por fecha de vencimiento (más próxima primero).
            # # Buscar una tarea:
                # # Permitir buscar una tarea por descripción y mostrar sus detalles si existe.
            # # Marcar una tarea como completada:
                # # Al completar, la tarea debe eliminarse de la lista.

    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def es_vacio(self):
        return self.cabeza is None

    def agregar_nodo(self, dato):
        nodo = Node(dato)
        if self.es_vacio():
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo

    def eliminar(self, dato):
        nodo_actual = self.cabeza
        if nodo_actual.data == dato:
            self.cabeza = nodo_actual.next
            return
        while nodo_actual.next is not None:
            if nodo_actual.next.data == dato:
                nodo_actual.next = nodo_actual.next.next
                return
            nodo_actual = nodo_actual.next

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.next

    def ordenar(self):
        if not self.cabeza or not self.cabeza.next:
            return

        current = self.cabeza
        while current:
            min_node = current
            searcher = current.next

            while searcher:
                if searcher.data.prioridad < min_node.data.prioridad:
                    min_node = searcher

                elif searcher.data.prioridad == min_node.data.prioridad:

                    if int(searcher.data.fechaDeVencimiento[6:9]) < int(min_node .data.fechaDeVencimiento[6:9]):

                        min_node = searcher
                    
                    elif int(searcher.data.fechaDeVencimiento[3:4]) < int(min_node .data.fechaDeVencimiento[3:4]):

                        min_node = searcher

                    elif int(searcher.data.fechaDeVencimiento[0:1]) < int(min_node .data.fechaDeVencimiento[0:1]):

                        min_node = searcher

                searcher = searcher.next

            current.data, min_node.data = min_node.data, current.data
            current = current.next
      

class Tarea():

    tareas = ListaEnlazada()

    def __init__(self, descripcion, prioridad, fechaDeVencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fechaDeVencimiento = fechaDeVencimiento
        Tarea.tareas.agregar_nodo(self)
        
    def __str__ (self):
        return f"Descripción: {self.descripcion}; Prioridad: {self.prioridad}; Fecha De Vencimiento: {self.fechaDeVencimiento}"


while (True):

    print("\nSISTEMA DE GESTIÓN DE TAREAS")
    print("\n¿Qué acción desea realizar?")
    print("1. Agregar tarea.")
    print("2. Eliminar una tarea.")
    print("3. Mostrar tareas.")
    print("4. Buscar y finalizar tareas.")
    print("5. Salir.")
    print("")
    opcion = int(input("Ingrese la opcion que desee: "))

    if opcion == 1:

        descripcion = input("\nIngrese la descripcion de la tarea: ")
        prioridad = input("\nIngrese la prioridad de la tarea (1 Alta - 2 Media - 3 Baja): ")

        while prioridad != None:
            if int(prioridad) > 0 and int(prioridad) < 4:
                True
            else:
                print("\nOpción invalida, intente nuevamente.")
                prioridad = input("\nIngrese la prioridad de la tarea (1 Alta - 2 Media - 3 Baja): ")
            break
        
        
        fechaVencimiento = input("ingrese la fecha de vecimiento de la tarea (DD/MM/AAA): ")


        tarea = Tarea(descripcion, prioridad, fechaVencimiento)

        print("\n¡¡¡Tarea creada con exito!!!")


    elif opcion == 2:
        
        print("\n¿Cómo desea eliminar de la lista?")
        print("1. por descripcion.")
        print("2. por indice.")
        opcion2 = int(input())

     
        if opcion2 == 1 and not(Tarea.tareas.es_vacio()):

            des = input("\nIngrese la descripcion de la tarea: ")

            temp = Tarea.tareas.cabeza
            elemento = None

            while temp != None:

                if temp.data.descripcion == des:

                    elemento = temp.data
                
                temp = temp.next

            if elemento != None:

               Tarea.tareas.eliminar(elemento)
               print("\n¡Tarea eliminada con éxito!")
            else:

                print(f"\nNo se encontró la tarea con descripcion: {des}, intente nuevamente.")

        
        elif opcion2 == 2 and not(Tarea.tareas.es_vacio()):
            
            indice = int(input("\nIngrese la posicion de la tarea: "))
            temp = Tarea.tareas.cabeza
            elemento = None 
            i = 1   
            while temp != None and i <= i:
                
                if i == indice:
                    elemento = temp.data

                temp = temp.next
                i = i+1

            if elemento != None:

               Tarea.tareas.eliminar(elemento)
               print("\n¡Tarea eliminada con éxito!")
            else:

                print(f"\nNo se encontró ninguna tarea registrada con el indice: {indice}, intente nuevamente.")


    elif opcion == 3:

        Tarea.tareas.ordenar()
        Tarea.tareas.imprimir()

    elif opcion == 4:

        des = input("\nIngrese la descripción de la tarea: ")

        temp = Tarea.tareas.cabeza
        elemento = None

        while temp != None:

            if temp.data.descripcion == des:

                elemento = temp.data
            
            temp = temp.next

        if elemento != None:

            print(elemento)
            opcion = int(input("\nDesea marcar la tarea como hecha? \n1. Si. \n2. No.\n"))

            if opcion == 1:

                Tarea.tareas.eliminar(elemento)
                print("\nTarea finalizada con éxito, ¡Felicidades!")
            
            elif opcion == 2:
                print("\nEntendido, no se finalizó la tarea.")
                

        else:

            print(f"\nNo se encontro la tarea con descripcion: {des}, intente nuevamente.")
    
    elif opcion == 5:
        print("\nSaliendo del sistema, ¡Hasta pronto!")
        break

    else:
        print("\nOpcion incorrecta, intente nuevamente.")
