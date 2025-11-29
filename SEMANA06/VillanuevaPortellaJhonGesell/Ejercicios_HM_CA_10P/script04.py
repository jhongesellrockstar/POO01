# script04.py
class Personaje:
    def __init__(self, nombre, nivel=1, salud=100):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud

class Mago(Personaje):
    def __init__(self, nombre, nivel=1, salud=100, mana=100, tipo_magia="fuego"):
        super().__init__(nombre, nivel, salud)
        self.mana = mana
        self.tipo_magia = tipo_magia

    def escribir_hechizo(self):
        return f"{self.nombre} prepara hechizo de {self.tipo_magia}."

class Guerrero(Personaje):
    def __init__(self, nombre, nivel=1, salud=120, fuerza=15, armadura=5):
        super().__init__(nombre, nivel, salud)
        self.fuerza = fuerza
        self.armadura = armadura

    def atacar(self):
        return f"{self.nombre} ataca con fuerza {self.fuerza}."

class MagoGuerrero(Mago, Guerrero):
    def __init__(self, nombre):
        Mago.__init__(self, nombre, nivel=1, salud=110, mana=120, tipo_magia="rayo")
        Guerrero.__init__(self, nombre, nivel=1, salud=110, fuerza=12, armadura=7)

    def atacar_con_magia(self):
        return f"{self.atacar()} {self.escribir_hechizo()} Daño combinado!"

    def subir_nivel(self):
        self.nivel += 1
        self.fuerza += 2
        self.mana += 10
        self.salud += 5

h = MagoGuerrero("Ulises")
print(h.atacar_con_magia())
h.subir_nivel()
print(f"Nivel: {h.nivel}, Salud: {h.salud}, Fuerza: {h.fuerza}, Mana: {h.mana}")
