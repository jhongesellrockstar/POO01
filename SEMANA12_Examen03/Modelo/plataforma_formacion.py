from abc import ABC, abstractmethod

# Clase abstracta base
class Usuario(ABC):
    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo

    @abstractmethod
    def rol(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__nombre} ({self.__correo})"

# Comportamiento académico
class Academico:
    def mostrar_info_academica(self):
        return f"Usuario académico con rol: {self.rol()}"

# Comportamiento evaluador
class Evaluador:
    def calificar(self, estudiante, curso, nota):
        if not isinstance(estudiante, Estudiante):
            raise ValueError("Solo se puede calificar a estudiantes.")
        estudiante.recibir_evaluacion(curso, nota)

# Herencia múltiple
class Profesor(Usuario, Academico, Evaluador):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.cursos = []

    def crear_curso(self, nombre):
        curso = Curso(nombre, self)
        self.cursos.append(curso)
        return curso

    def rol(self):
        return "Profesor"

class Estudiante(Usuario, Academico):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.evaluaciones = []

    def inscribirse(self, curso):
        curso.inscribir_estudiante(self)

    def recibir_evaluacion(self, curso, nota):
        self.evaluaciones.append(Evaluacion(curso.nombre, nota))

    def rol(self):
        return "Estudiante"

    def estadisticas(self):
        aprobados = list(filter(lambda e: e.nota >= 11, self.evaluaciones))
        destacados = list(filter(lambda e: e.nota >= 18, self.evaluaciones))
        promedio = sum(e.nota for e in self.evaluaciones) / len(self.evaluaciones) if self.evaluaciones else 0
        return {
            "promedio": promedio,
            "aprobados": len(aprobados),
            "destacados": list(map(lambda e: e.curso, destacados))
        }

# Clase Curso
class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise ValueError("Solo se pueden inscribir estudiantes.")
        self.estudiantes.append(estudiante)

    def __str__(self):
        return f"Curso: {self.nombre} - Profesor: {self.profesor}"

# Clase Evaluación
class Evaluacion:
    def __init__(self, curso, nota):
        self.curso = curso
        self.nota = nota

    def __str__(self):
        return f"{self.curso}: Nota {self.nota}"

# Pruebas
if __name__ == "__main__":
    try:
        prof = Profesor("Dra. Rosa", "rosa@uni.edu.pe")
        est1 = Estudiante("Carlos", "carlos@correo.com")
        est2 = Estudiante("Lucía", "lucia@correo.com")

        curso1 = prof.crear_curso("POO-I")
        curso2 = prof.crear_curso("Algoritmos")

        est1.inscribirse(curso1)
        est2.inscribirse(curso1)
        est2.inscribirse(curso2)

        prof.calificar(est1, curso1, 17)
        prof.calificar(est2, curso1, 19)
        prof.calificar(est2, curso2, 14)

        print(est1)
        for ev in est1.evaluaciones:
            print(ev)
        print(est1.estadisticas())

        print(est2)
        for ev in est2.evaluaciones:
            print(ev)
        print(est2.estadisticas())

        prof.calificar("no es estudiante", curso1, 15)  # Provoca excepción

    except Exception as e:
        print("Error:", e)
