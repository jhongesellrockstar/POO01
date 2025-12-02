from tkinter import *

"""Paso 4: construir una cuadrícula estilo ajedrez siguiendo los pasos previos."""

root = Tk()
root.title("Estilos y Marcos - Paso 4")
root.resizable(False, False)

# Paso 1 y 2: marco inicial con márgenes
marco_inicial = LabelFrame(root, text="Marco de 300 x 300", width=300, height=300)
marco_inicial.pack(padx=25, pady=10)
marco_inicial.pack_propagate(False)

# Paso 3: eliminar el marco inicial y mostrar dos marcos de 200x400
marco_inicial.destroy()

contenedor = Frame(root)
contenedor.pack(padx=15, pady=15)

marco_izquierdo = Frame(contenedor, width=200, height=400, background="lightblue")
marco_izquierdo.pack(side=LEFT)
marco_izquierdo.pack_propagate(False)

marco_derecho = Frame(contenedor, width=200, height=400, background="lightgreen")
marco_derecho.pack(side=RIGHT)
marco_derecho.pack_propagate(False)

# Paso 4: limpiar y mostrar la cuadrícula estilo ajedrez 3x3
contenedor.destroy()

marco_tablero = LabelFrame(root, text="Tablero estilo ajedrez 3 x 3", padx=10, pady=10)
marco_tablero.pack(padx=15, pady=15)

color_oscuro = "tomato"
color_claro = "lightyellow"

for fila in range(3):
    for columna in range(3):
        color = color_oscuro if (fila + columna) % 2 == 0 else color_claro
        Frame(
            marco_tablero,
            width=60,
            height=60,
            background=color,
            border=1,
            relief="solid",
        ).grid(row=fila, column=columna, padx=2, pady=2)

root.mainloop()
