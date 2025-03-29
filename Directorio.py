# directorio telefónico, donde debe asegurar que los datos sean guardados de forma eficiente,
# donde no haya perdida de datos y se pueda consultar la información rápidamente.

class DirectorioTelefonico:
    def __init__(self, size=100):
        self.size = size
        self.tabla = [[] for _ in range(self.size)]

    def _hash(self, clave):
        return hash(clave) % self.size

    def agregar_contacto(self, nombre, telefono, direccion, email):
        indice = self._hash(nombre.lower())
        for contacto in self.tabla[indice]:
            if contacto["nombre"] == nombre:
                contacto.update({"telefono": telefono, "direccion": direccion, "email": email})
                return "Contacto actualizado."
        
        self.tabla[indice].append({"nombre": nombre, "telefono": telefono, "direccion": direccion, "email": email})
        return "Contacto agregado."

    def buscar_contacto(self, nombre):
        indice = self._hash(nombre.lower())
        for contacto in self.tabla[indice]:
            if contacto["nombre"] == nombre:
                return contacto
        return "Contacto no encontrado."

    def eliminar_contacto(self, nombre):
        indice = self._hash(nombre.lower())
        for i, contacto in enumerate(self.tabla[indice]):
            if contacto["nombre"] == nombre:
                del self.tabla[indice][i]
                return "Contacto eliminado."
        return "Contacto no encontrado."

    def mostrar_directorio(self):
        contactos = []
        for bucket in self.tabla:
            contactos.extend(bucket)
        return contactos

    def mostrar_contactos_con_casillas(self):
        contactos = []
        for indice, bucket in enumerate(self.tabla):
            for contacto in bucket:
                contactos.append({"casilla": indice, **contacto})
        return contactos

def menu():
    directorio = DirectorioTelefonico()
    while True:
        print("\nMenú del Directorio Telefónico")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            direccion = input("Ingrese la dirección: ")
            email = input("Ingrese el email: ")
            print(directorio.agregar_contacto(nombre, telefono, direccion, email))

        elif opcion == "2":
            nombre = input("Ingrese el nombre a buscar: ")
            print(directorio.buscar_contacto(nombre))

        elif opcion == "3":
            nombre = input("Ingrese el nombre a eliminar: ")
            print(directorio.eliminar_contacto(nombre))

        elif opcion == "4":
            print(directorio.mostrar_directorio())
        

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()