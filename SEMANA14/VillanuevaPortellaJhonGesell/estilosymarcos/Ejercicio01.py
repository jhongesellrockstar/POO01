from tkinter import *

# Creación de la ventana principal
root = Tk()
root.title('Tablero de ajedrez')
root.resizable(False, False)

# Marco contenedor del tablero
marco_tablero = LabelFrame(
    root,
    text='Tablero de 8 x 8',
    padx=12,
    pady=12,
)
marco_tablero.pack(padx=15, pady=15)

# Colores alternados para las casillas
color_oscuro = 'sienna'
color_claro = 'cornsilk'

# Construcción del tablero
for fila in range(8):
    for columna in range(8):
        color = color_oscuro if (fila + columna) % 2 == 0 else color_claro
        Button(
            marco_tablero,
            background=color,
            activebackground=color,
            border=1,
            width=4,
            height=2,
            state=DISABLED,
        ).grid(row=fila, column=columna, padx=2, pady=2)

# Bucle de ejecución
root.mainloop()
