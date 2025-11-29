from tkinter import *

# Crear la ventana principal
ventana = Tk()
ventana.title("Calculadora de Promedio")
ventana.geometry("350x350")

# Título
titulo = Label(ventana, text="Calculadora de Promedio de Notas", font=("Arial", 12, "bold"))
titulo.pack(pady=10)

# Etiquetas y campos de entrada
label_nota1 = Label(ventana, text="Nota 1:")
label_nota1.pack()
entry_nota1 = Entry(ventana)
entry_nota1.pack(pady=5)

label_nota2 =Label(ventana, text="Nota 2:")
label_nota2.pack()
entry_nota2 = Entry(ventana)
entry_nota2.pack(pady=5)

label_nota3 = Label(ventana, text="Nota 3:")
label_nota3.pack()
entry_nota3 = Entry(ventana)
entry_nota3.pack(pady=5)

# Etiqueta de resultado
label_resultado = Label(ventana, text="", fg="blue", font=("Arial", 10, "bold"))
label_resultado.pack(pady=10)

# Función para calcular el promedio
def calcular_promedio():
    try:
        # Obtener valores y convertirlos a float
        n1 = float(entry_nota1.get())
        n2 = float(entry_nota2.get())
        n3 = float(entry_nota3.get())
        
        # Validar que estén entre 0 y 10
        if not (0 <= n1 <= 20 and 0 <= n2 <= 20 and 0 <= n3 <= 20):
            label_resultado.config(text="⚠️ Las notas deben estar entre 0 y 20.", fg="red")
            return
        
        # Calcular promedio
        promedio = (n1 + n2 + n3) / 3
        
        # Mostrar resultado
        if promedio >= 11:
            label_resultado.config(text=f"Promedio: {promedio:.2f} ✅ Aprobado", fg="green")
        else:
            label_resultado.config(text=f"Promedio: {promedio:.2f} ❌ Reprobado", fg="red")
    
    except ValueError:
        # Si el usuario no escribe números
        label_resultado.config(text="⚠️ Ingresa solo números válidos.", fg="red")

# Botón para calcular
boton_calcular = Button(ventana, text="Calcular Promedio", command=calcular_promedio)
boton_calcular.pack(pady=10)

# Botón para limpiar
def limpiar_campos():
    entry_nota1.delete(0, END)
    entry_nota2.delete(0, END)
    entry_nota3.delete(0, END)
    label_resultado.config(text="")

boton_limpiar = Button(ventana, text="Limpiar", command=limpiar_campos)
boton_limpiar.pack(pady=5)

# Ejecutar ventana
ventana.mainloop()
