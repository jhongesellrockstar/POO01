from tkinter import *

"""Paso 3: crear dos marcos vacíos de 200x400 px con colores diferentes."""

root = Tk()
root.title("Estilos y Marcos - Paso 3")
root.resizable(False, False)

# Paso 1 y 2: marco inicial con márgenes
marco_inicial = LabelFrame(root, text="Marco de 300 x 300", width=300, height=300)
marco_inicial.pack(padx=25, pady=10)
marco_inicial.pack_propagate(False)

# Paso 3: borrar el marco anterior y crear dos marcos de 200x400
marco_inicial.destroy()

contenedor = Frame(root)
contenedor.pack(padx=15, pady=15)

marco_izquierdo = Frame(contenedor, width=200, height=400, background="lightblue")
marco_izquierdo.pack(side=LEFT)
marco_izquierdo.pack_propagate(False)

marco_derecho = Frame(contenedor, width=200, height=400, background="lightgreen")
marco_derecho.pack(side=RIGHT)
marco_derecho.pack_propagate(False)

root.mainloop()
