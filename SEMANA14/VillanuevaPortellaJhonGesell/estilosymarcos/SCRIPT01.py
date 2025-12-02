from tkinter import *

"""Paso 1: crear un marco visible de 300x300 px con un título usando Frame."""

root = Tk()
root.title("Estilos y Marcos - Paso 1")
root.resizable(False, False)

marco_inicial = Frame(root, width=300, height=300, relief="groove", borderwidth=2)
marco_inicial.pack()
marco_inicial.pack_propagate(False)

Label(marco_inicial, text="Marco de 300 x 300").pack(pady=5)

root.mainloop()
