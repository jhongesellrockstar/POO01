from tkinter import *
# Crear la ventana principal
ventana = Tk()
ventana.title("Ejercicio con Tkinter")
ventana.geometry("300x200")

# Etiqueta de instrucción
label_instruccion = Label(ventana, text="Escribe tu nombre:")
label_instruccion.pack(pady=10)

# Campo de texto (Entry)
entrada_nombre = Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

# Etiqueta para mostrar el resultado
label_resultado = Label(ventana, text="", fg="blue")
label_resultado.pack(pady=10)

# Función que se ejecuta al presionar el botón
def saludar():
    nombre = entrada_nombre.get()
    if nombre.strip() == "":
        label_resultado.config(text="Por favor, escribe tu nombre.")
    else:
        label_resultado.config(text=f"¡Hola, {nombre}!")

# Botón que llama a la función
boton_saludar = Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
