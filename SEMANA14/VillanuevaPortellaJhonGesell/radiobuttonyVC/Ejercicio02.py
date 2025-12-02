from tkinter import *

# Creación de la ventana principal
root = Tk()
root.title('RadioButton y variables de control')
root.resizable(False, False)

# Variables de control
color_seleccionado = IntVar()
colores = {
    1: ('Rojo', 'firebrick1'),
    2: ('Azul', 'royalblue2'),
    3: ('Verde', 'mediumseagreen'),
    4: ('Amarillo', 'gold'),
}

# Marcos principales
marco_opciones = LabelFrame(root, text='Opciones', padx=12, pady=12)
marco_opciones.grid(row=0, column=0, padx=10, pady=10, sticky='n')

marco_boton = LabelFrame(root, text='Acción', padx=12, pady=12)
marco_boton.grid(row=1, column=0, padx=10, pady=10, sticky='n')

marco_resultado = LabelFrame(root, text='Resultado', padx=12, pady=12)
marco_resultado.grid(row=2, column=0, rowspan=2, padx=10, pady=10)

# Etiqueta donde se mostrará la selección
resultado = Label(marco_resultado, text='Color seleccionado: Rojo', width=25)
resultado.pack(padx=5, pady=5)

# RadioButtons con las opciones de color
for valor, (texto, _) in colores.items():
    Radiobutton(
        marco_opciones,
        text=texto,
        variable=color_seleccionado,
        value=valor,
    ).pack(anchor='w')


# Función que actualiza el resultado con el color elegido

def actualizar_color():
    _, color = colores[color_seleccionado.get()]
    texto, _ = colores[color_seleccionado.get()]
    resultado.config(text=f'Color seleccionado: {texto}', background=color)


Button(
    marco_boton,
    text='Mostrar selección',
    command=actualizar_color,
    width=20,
    background='deepskyblue',
    foreground='white',
).pack()

# Bucle de ejecución
root.mainloop()
