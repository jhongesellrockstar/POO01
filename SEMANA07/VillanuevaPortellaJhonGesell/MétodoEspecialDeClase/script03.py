# Problema04
class Jugador:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
    def __str__(self):
        if self.puntaje < 1000:
            nivel = 'Principiante'
        else:
            nivel = 'Experto'
        return f'Jugador[Nombre: {self.nombre}, Puntaje: {self.puntaje}, Nivel: {nivel}]'
jugador1 = Jugador('Ana', 950)
jugador2 = Jugador('Luis', 1200)
print(jugador1)
print(jugador2)