from tkinter import *

"""Paso 2: añadir márgenes al marco de 300x300 px."""

root = Tk()
root.title("Estilos y Marcos - Paso 2")
root.resizable(False, False)

marco_inicial = LabelFrame(root, text="Marco de 300 x 300", width=300, height=300)
marco_inicial.pack(padx=25, pady=10)
marco_inicial.pack_propagate(False)

root.mainloop()
