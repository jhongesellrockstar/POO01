# script02.py
class Empleado:
    def __init__(self, nombre, apellido, emp_id, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.emp_id = emp_id
        self.salario = salario

class Programador(Empleado):
    def __init__(self, nombre, apellido, emp_id, salario, lenguajes=None):
        super().__init__(nombre, apellido, emp_id, salario)
        self.lenguajes_programacion = set(lenguajes or [])

class Diseñador(Empleado):
    def __init__(self, nombre, apellido, emp_id, salario, herramientas=None):
        super().__init__(nombre, apellido, emp_id, salario)
        self.herramientas_diseno = set(herramientas or [])

class EmpleadoMultifuncional(Programador, Diseñador):
    def __init__(self, nombre, apellido, emp_id, salario,
                 lenguajes=None, herramientas=None):
        Programador.__init__(self, nombre, apellido, emp_id, salario, lenguajes)
        Diseñador.__init__(self, nombre, apellido, emp_id, salario, herramientas)
        self.tareas = []

    def agregar_habilidad(self, tipo, valor):
        if tipo == "lenguaje":
            self.lenguajes_programacion.add(valor)
        elif tipo == "herramienta":
            self.herramientas_diseno.add(valor)

    def agregar_tarea(self, desc):
        self.tareas.append(desc)

    def listar(self):
        return {
            "empleado": f"{self.nombre} {self.apellido} ({self.emp_id})",
            "lenguajes": sorted(self.lenguajes_programacion),
            "herramientas": sorted(self.herramientas_diseno),
            "tareas": list(self.tareas)
        }

e = EmpleadoMultifuncional("Fiorella", "Villanueva", 101, 6500,
                           lenguajes={"Python"}, herramientas={"Figma"})
e.agregar_habilidad("lenguaje", "JavaScript")
e.agregar_habilidad("herramienta", "Illustrator")
e.agregar_tarea("API de facturación")
e.agregar_tarea("Prototipo de interfaz")
print(e.listar())
