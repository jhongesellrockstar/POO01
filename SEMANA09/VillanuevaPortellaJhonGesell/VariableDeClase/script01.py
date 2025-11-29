class Jugador:
    contador_pasadaTiempo = 30
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        
    def imprimir(self):
        print(f"Jugador: {self.nombre}, Puntaje: {self.puntaje}")
        print(f"Tiempo restante: {Jugador.contador_pasadaTiempo} minutos")
    
    def pasar_tiempo(self):
        if Jugador.contador_pasadaTiempo > 0:
            Jugador.contador_pasadaTiempo -= 1
            return True
        return False
        
jugador1 = Jugador("Jhon", "20")
jugador2 = Jugador("Gesell","17")

print("Estado inicial:")
jugador1.imprimir()
jugador2.imprimir()

print("\nReduciendo el tiempo:")
while jugador1.pasar_tiempo():
    print(f"Tiempo restante: {Jugador.contador_pasadaTiempo} minutos")

print("\nTiempo agotado!")