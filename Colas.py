from typing import Optional

class Node:
    def __init__(self, value: object) -> None:
        self.value: object = value
        self.next: Optional["Node"] = None

class Queue:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def enqueue(self, value: object) -> None:
        new_node: Node = Node(value)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self) -> object:
        if self.isEmpty():
            raise Exception("Queue is empty")
        assert self.head is not None
        removed_value: object = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return removed_value

    def peek(self) -> Optional[object]:
        if self.isEmpty():
            return None
        assert self.head is not None
        return self.head.value

    def getSize(self) -> int:
        return self.size

    def __str__(self) -> str:
        if self.isEmpty():
            return "No hay turnos pendientes."
        result: list[str] = []
        current: Optional[Node] = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)

if __name__ == "__main__":

    quest = Queue()
    helper = Queue()
    cashier = Queue()
    others = Queue()
    priority = Queue()
    
    while True:
        


            opcion = int(input("Elija una opcion:\n1. Pedir ficho\n2. Siguiente turno\n3. Turnos restantes\n4. Salir\n")) #Int

            if opcion == 1:

                print("Ingrese los siguientes datos\n")

                nombre = input("Ingrese su nombre: ")
                documento = input("Ingrese su documento: ")
                tipo = input("Seleccione el tipo de atencion a recibir: 1. duda.\n 2. Asesor.\n 3. caja.\n 4. otros.\n")
                edad = int(input("Ingrese su edad: "))
                prioridad = input("¿Solicita atención prioritaria? (Si no desea especificarla presione enter)\n 1. Si.\n 2. No. ")

                if prioridad == "" and edad >= 60:

                    prioridad = "usuario de prioridad"

            
                usuario = (nombre, documento, tipo, edad, prioridad)

                if (usuario[4]) == "usuario de prioridad":

                    priority.enqueue(usuario)

                elif (usuario[2]) == "duda":
                    
                    quest.enqueue(usuario)
                
                elif (usuario[2] == "asesor"):

                    helper.enqueue(usuario)

                elif (usuario [2] == "caja"):

                    cashier.enqueue(usuario)

                else:

                    others.enqueue(usuario)

            elif opcion == 2:
                tipo = input("Ingrese la cola a consultar (duda, asesor, caja, otros, prioridad): ").strip().lower()
                cola = {"duda": quest, "asesor": helper, "caja": cashier, "otros": others, "prioridad": priority}.get(tipo)
                if cola is None:
                    print("Tipo de atención no válido.")
                elif cola.isEmpty():
                    print(f"No hay turnos en la cola de {tipo}.")
                else:
                    siguiente = cola.dequeue()
                    print(f"Siguiente turno en {tipo}: {siguiente}")

            elif opcion == 3:
                tipo = input("Ingrese la cola a verificar (duda, asesor, caja, otros, prioridad): ").strip().lower()
                cola = {"duda": quest, "asesor": helper, "caja": cashier, "otros": others, "prioridad": priority}.get(tipo)
                if cola is None:
                    print("Tipo de atención no válido.")
                else:
                    print(f"Turnos pendientes en {tipo}: {cola}") 
                
            elif opcion == 4:
                
                break