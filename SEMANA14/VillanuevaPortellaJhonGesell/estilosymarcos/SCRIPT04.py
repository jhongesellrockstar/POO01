from tkinter import *

"""Paso 4: construir una cuadrícula estilo ajedrez siguiendo los pasos previos."""

root = Tk()
root.title("Estilos y Marcos - Paso 4")
root.resizable(False, False)

# Paso 1 y 2: marco inicial con márgenes
marco_inicial = Frame(root, width=300, height=300, relief="groove", borderwidth=2)
marco_inicial.pack(padx=25, pady=10)
marco_inicial.pack_propagate(False)
Label(marco_inicial, text="Marco de 300 x 300").pack(pady=5)

# Paso 3: eliminar el marco inicial y mostrar dos marcos de 200x400
marco_inicial.destroy()

contenedor = Frame(root)
contenedor.pack(padx=15, pady=15)

marco_izquierdo = Frame(contenedor, width=200, height=400, background="lightblue", relief="ridge", borderwidth=2)
marco_izquierdo.pack(side=LEFT)
marco_izquierdo.pack_propagate(False)

marco_derecho = Frame(contenedor, width=200, height=400, background="lightgreen", relief="ridge", borderwidth=2)
marco_derecho.pack(side=RIGHT)
marco_derecho.pack_propagate(False)

# Paso 4: limpiar y mostrar la cuadrícula estilo ajedrez 3x3 sin bucles
contenedor.destroy()

Label(root, text="Tablero estilo ajedrez 3 x 3").pack(pady=(10, 0))

marco_tablero = Frame(root, padx=10, pady=10, relief="groove", borderwidth=2)
marco_tablero.pack(padx=15, pady=15)

color_oscuro = "tomato"
color_claro = "lightyellow"

celda_00 = Frame(marco_tablero, width=60, height=60, background=color_oscuro, border=1, relief="solid")
celda_00.grid(row=0, column=0, padx=2, pady=2)
celda_00.pack_propagate(False)

celda_01 = Frame(marco_tablero, width=60, height=60, background=color_claro, border=1, relief="solid")
celda_01.grid(row=0, column=1, padx=2, pady=2)
celda_01.pack_propagate(False)

celda_02 = Frame(marco_tablero, width=60, height=60, background=color_oscuro, border=1, relief="solid")
celda_02.grid(row=0, column=2, padx=2, pady=2)
celda_02.pack_propagate(False)

celda_10 = Frame(marco_tablero, width=60, height=60, background=color_claro, border=1, relief="solid")
celda_10.grid(row=1, column=0, padx=2, pady=2)
celda_10.pack_propagate(False)

celda_11 = Frame(marco_tablero, width=60, height=60, background=color_oscuro, border=1, relief="solid")
celda_11.grid(row=1, column=1, padx=2, pady=2)
celda_11.pack_propagate(False)

celda_12 = Frame(marco_tablero, width=60, height=60, background=color_claro, border=1, relief="solid")
celda_12.grid(row=1, column=2, padx=2, pady=2)
celda_12.pack_propagate(False)

celda_20 = Frame(marco_tablero, width=60, height=60, background=color_oscuro, border=1, relief="solid")
celda_20.grid(row=2, column=0, padx=2, pady=2)
celda_20.pack_propagate(False)

celda_21 = Frame(marco_tablero, width=60, height=60, background=color_claro, border=1, relief="solid")
celda_21.grid(row=2, column=1, padx=2, pady=2)
celda_21.pack_propagate(False)

celda_22 = Frame(marco_tablero, width=60, height=60, background=color_oscuro, border=1, relief="solid")
celda_22.grid(row=2, column=2, padx=2, pady=2)
celda_22.pack_propagate(False)

root.mainloop()
