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

# lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Verificar si la lista está vacía
    def es_vacio(self):
        return self.cabeza is None

    # Agregar Nodo
    def agregar_nodo(self, dato):
        nodo = Node(dato)
        if self.es_vacio():
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo

    # Eliminar Nodo
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

    # Imprimir Lista
    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.next

    def ordenar(self):
        if not self.cabeza or not self.cabeza.next:
            return  # Lista vacía o con un solo nodo (ordenada)

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

            # Intercambiar valores
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
        return f"Descripciom: {self.descripcion}; Prioridad: {self.prioridad}; Fecha De Vencimiento: {self.fechaDeVencimiento}"


while (True):

    print("Sistema de gestion de tareas")

    print("1. Agregar tarea")
    print("2. Eliminar una tarea")
    print("3. Mostrar tareas")
    print("4. Buscar y finalizar tareas")
    print("")
    opcion = int(input("Ingrese la opcion que desee: "))

    if opcion == 1:

        descripcion = input("Ingrese la descripcion de la tarea: ")
        prioridad = input("Ingrese la prioridad de la tarea (1 Alto - 3 Bajo)")
        fechaVencimiento = input("Ingrese fecha de vencimiento (DD/MM/AAAA): ")

        tarea = Tarea(descripcion, prioridad, fechaVencimiento)

        print("Tarea creada con exito")


    elif opcion == 2:
        
        print("Como desea eliminar de la lista")
        print("1. por descripcion ")
        print("2. por indice")
        opcion2 = int(input())

     
        if opcion2 == 1 and not(Tarea.tareas.es_vacio()):

            des = input("Ingrese la descripcion de la tarea")

            temp = Tarea.tareas.cabeza
            elemento = None

            while temp != None:

                if temp.data.descripcion == des:

                    elemento = temp.data
                
                temp = temp.next

            if elemento != None:

               Tarea.tareas.eliminar(elemento)
               print("Se elimino el elemento elegido")
            else:

                print(f"No se encontro la tarea con descripcion: {des}")

        
        elif opcion2 == 2 and not(Tarea.tareas.es_vacio()):
            
            indice = int(input("Ingrese la posicion del elemento"))
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
               print("Se elimino el elemento elegido")
            else:

                print(f"No se encontro la tarea con indice: {indice}")


    elif opcion == 3:

        Tarea.tareas.ordenar()
        Tarea.tareas.imprimir()

    elif opcion == 4:

        des = input("Ingrese la descripcion de la tarea")

        temp = Tarea.tareas.cabeza
        elemento = None

        while temp != None:

            if temp.data.descripcion == des:

                elemento = temp.data
            
            temp = temp.next

        if elemento != None:

            print(elemento)
            opcion = int(input("Desea marcar la tarea como hecha? \n1. Si \n2. No"))

            if opcion == 1:

                Tarea.tareas.eliminar(elemento)
                

        else:

            print(f"No se encontro la tarea con descripcion: {des}")