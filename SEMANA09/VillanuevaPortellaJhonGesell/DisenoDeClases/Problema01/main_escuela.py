from EscuelaProfesional import EscuelaProfesional
from Docente import Docente
from Alumno import Alumno

# --- Bloque principal ---
if __name__ == "__main__":
    # Crear escuela profesional
    ep = EscuelaProfesional(101, "Programación Orientada a Objetos")

    # Crear docentes
    d1 = Docente("Carlos", 20, 50)
    d2 = Docente("Lucía", 16, 60)

    # Crear alumnos
    a1 = Alumno("Ana", 15, 20)
    a2 = Alumno("Luis", 14, 18)
    a3 = Alumno("María", 16, 22)

    # Asignar alumnos a docentes
    d1.agregar_alumno(a1)
    d1.agregar_alumno(a2)
    d2.agregar_alumno(a3)

    # Agregar docentes a la escuela
    ep.agregar_docente(d1)
    ep.agregar_docente(d2)

    # Mostrar resultados
    print(ep)
    print(d1)
    print(d2)
    print(a1)
    print(a2)
    print(a3)
