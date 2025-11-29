# Clase base: Usuario
class Usuario:
    def __init__(self, usuario_id, nombre_usuario, accesos):
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario
        self.accesos = accesos  # Lista de accesos al sistema

    def contar_accesos(self):
        return len(self.accesos)

# Clase base: Empleado
class Empleado:
    def __init__(self, empleado_id, nombre, departamento):
        self.empleado_id = empleado_id
        self.nombre = nombre
        self.departamento = departamento

    def es_ti(self):
        return self.departamento.lower() == "ti"

# Clase derivada con herencia múltiple
class UsuarioEmpleado(Usuario, Empleado):
    def __init__(self, usuario_id, nombre_usuario, accesos, empleado_id, nombre, departamento, rol):
        Usuario.__init__(self, usuario_id, nombre_usuario, accesos)
        Empleado.__init__(self, empleado_id, nombre, departamento)
        self.rol = rol

    def mostrar_resumen(self):
        print(f"\nResumen del UsuarioEmpleado: {self.nombre} ({self.nombre_usuario})")
        print(f"Departamento: {self.departamento} | Rol: {self.rol}")
        print(f"Número de accesos: {self.contar_accesos()}")

        # Condicional con lambda: verificar si tiene acceso crítico
        tiene_acceso_critico = lambda accesos: "AdminPanel" in accesos
        if tiene_acceso_critico(self.accesos):
            print("⚠️ Tiene acceso al panel de administración.") 
        else:
            print("✅ No tiene acceso crítico.")

        # Bucle con condicional
        print("🗂 Lista de accesos:")
        for acceso in self.accesos:
            if acceso.startswith("Mod"):
                print(f" - [Módulo] {acceso}")
            else:
                print(f" - {acceso}")

        # Mostrar si es parte del área de TI
        if self.es_ti():
            print("👨‍💻 Pertenece al área de Tecnología de la Información.")
        else:
            print("📂 Pertenece a otro departamento.")

# Datos simulados
accesos_usuario = ["Dashboard", "ModInventario", "ModUsuarios", "AdminPanel"]

usuario1 = UsuarioEmpleado(
    usuario_id=101,
    nombre_usuario="jlopez",
    accesos=accesos_usuario,
    empleado_id=5001,
    nombre="José López",
    departamento="TI",
    rol="Administrador"
)

usuario1.mostrar_resumen()

