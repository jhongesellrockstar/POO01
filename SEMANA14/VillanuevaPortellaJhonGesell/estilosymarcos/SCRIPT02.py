from tkinter import *

"""Paso 2: añadir márgenes al marco de 300x300 px sin usar LabelFrame."""

root = Tk()
root.title("Estilos y Marcos - Paso 2")
root.resizable(False, False)

marco_inicial = Frame(root, width=300, height=300, relief="groove", borderwidth=2)
marco_inicial.pack(padx=25, pady=10)
marco_inicial.pack_propagate(False)

Label(marco_inicial, text="Marco de 300 x 300").pack(pady=5)

root.mainloop()
