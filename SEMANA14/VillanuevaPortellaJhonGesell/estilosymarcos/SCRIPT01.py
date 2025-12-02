from tkinter import *

"""Paso 1: crear un marco visible de 300x300 px con un título."""

root = Tk()
root.title("Estilos y Marcos - Paso 1")
root.resizable(False, False)

marco_inicial = LabelFrame(root, text="Marco de 300 x 300", width=300, height=300)
marco_inicial.pack()
marco_inicial.pack_propagate(False)

root.mainloop()
