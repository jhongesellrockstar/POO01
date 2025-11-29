class InstrumentoMusical:
    def sonar(self):
        print("sonido genérico de instrumento")

class Guitarra(InstrumentoMusical):
    def sonar(self):
        print("Strum, strum (guitarra)")

class Piano(InstrumentoMusical):
    def sonar(self):
        print("Plin, plan (piano)")

def hacer_sonar_todos(lista_instrumentos):
    for inst in lista_instrumentos:
        inst.sonar()

# Pruebas
g = Guitarra()
p = Piano()
hacer_sonar_todos([g, p, Guitarra(), Piano()])