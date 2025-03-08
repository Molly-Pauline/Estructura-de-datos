# # 4. Clases Usuario, Administrador, Cliente:

# # Crea una clase base Usuario con atributos como nombreDeUsuario y contraseña, y un método iniciarSesión().
# # Crea dos clases derivadas: Administrador (con un método adicional gestionarUsuarios()) 
# # y Cliente (con un método adicional realizarCompra()).Implementa el método iniciarSesión() para verificar las 
# # credenciales del usuario. Asegúrate de que los métodos adicionales de las clases derivadas reflejen los permisos y 
# # acciones específicas de cada tipo de usuario.

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
    
    def iniciar_sesion(self, usuario, clave):
        if usuario == self.nombre_usuario and clave == self.contrasena:
            print(f"Bienvenido, {self.nombre_usuario}!")
        else:
            print("Usuario o contraseña incorrectos.")


class Administrador(Usuario):
    def __init__(self, nombre_usuario, contrasena):
        super().__init__(nombre_usuario, contrasena)
    
    def gestionar_usuarios(self):
        print(f"{self.nombre_usuario} está gestionando usuarios")


class Cliente(Usuario):
    def __init__(self, nombre_usuario, contrasena):
        super().__init__(nombre_usuario, contrasena)
    
    def realizar_compra(self):
        print(f"{self.nombre_usuario} está comprando cosas")


admin = Administrador("admin123", "seguro123")
cliente = Cliente("Molly", "clave123")

admin.iniciar_sesion("admin123", "seguro123")
admin.gestionar_usuarios()

cliente.iniciar_sesion("Molly", "clave123")
cliente.realizar_compra()