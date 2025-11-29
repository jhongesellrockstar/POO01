# Clase base: Usuario del sistema
class Usuario:
    def __init__(self, usuario_id, nombre_usuario):
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario

# Clase base: Empleado de la empresa
class Empleado:
    def __init__(self, empleado_id, nombre, departamento):
        self.empleado_id = empleado_id
        self.nombre = nombre
        self.departamento = departamento

# Clase derivada: UsuarioEmpleado hereda de Usuario y Empleado
class UsuarioEmpleado(Usuario, Empleado):
    def __init__(self, usuario_id, nombre_usuario, empleado_id, nombre, departamento, rol):
        Usuario.__init__(self, usuario_id, nombre_usuario)
        Empleado.__init__(self, empleado_id, nombre, departamento)
        self.rol = rol  # atributo adicional relacionado al sistema

    def mostrar_info_completa(self):
        return (f"Usuario: {self.nombre_usuario} (ID: {self.usuario_id})\n"
                f"Empleado: {self.nombre} (ID: {self.empleado_id})\n"
                f"Departamento: {self.departamento}\n"
                f"Rol del sistema: {self.rol}")

# Uso
usuario1 = UsuarioEmpleado(
    usuario_id=101,
    nombre_usuario="jlopez",
    empleado_id=5001,
    nombre="José López",
    departamento="TI",
    rol="Administrador"
)

print(usuario1.mostrar_info_completa())
