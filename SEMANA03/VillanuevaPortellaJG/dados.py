import random

def tirar_dado():
    return random.randint(1, 6)

def juego_tres_dados():
    d1, d2, d3 = tirar_dado(), tirar_dado(), tirar_dado()
    print(f"Resultados: {d1}, {d2}, {d3}")
    if d1 == d2 == d3:
        print("¡Ganó!")
    else:
        print("Perdió.")

juego_tres_dados()
