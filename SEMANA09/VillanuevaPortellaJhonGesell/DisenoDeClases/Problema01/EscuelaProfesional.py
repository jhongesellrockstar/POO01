from Docente import Docente

class EscuelaProfesional:
    contador_escuelas = 0

    def __init__(self, id_registro, curso):
        EscuelaProfesional.contador_escuelas += 1
        self.id_registro = id_registro
        self.curso = curso
        self.docentes = []  # lista de objetos Docente

    def agregar_docente(self, docente: Docente):
        self.docentes.append(docente)

    def __str__(self):
        docentes_nombres = ', '.join([d.nombre for d in self.docentes]) or "Sin docentes"
        return (f"EscuelaProfesional(registro={self.id_registro}, curso={self.curso}, "
                f"docentes=[{docentes_nombres}])")
