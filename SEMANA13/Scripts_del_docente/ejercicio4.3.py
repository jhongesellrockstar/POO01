import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necesita instalar pillow: pip install pillow

def procesar_texto():
    """
    Función que toma el texto del Entry y muestra un mensaje.
    Incluye manejo de excepciones.
    """
    try:
        texto = entrada.get()
        if texto.strip() == "":
            raise ValueError("El campo está vacío. Escribe algo.")
        messagebox.showinfo("Resultado", f"Has escrito: {texto}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Ocurrió un problema: {e}")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo Tkinter con Widgets")
ventana.geometry("400x450")

# Establecer icono (usar archivo .ico)
try:
    ventana.iconbitmap("world.ico")  # Debe existir el archivo
except Exception:
    print("No se pudo cargar el icono. Continuando sin icono...")

# Label
label = tk.Label(ventana, text="Escribe algo:", font=("Arial", 12))
label.pack(pady=10)

# Entry
entrada = tk.Entry(ventana, font=("Arial", 12), width=30)
entrada.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Procesar", font=("Arial", 12),
                  command=procesar_texto)
boton.pack(pady=10)

# Imagen
try:
    img = Image.open("naturaleza.jpg")
    img = img.resize((250, 250))
    img_tk = ImageTk.PhotoImage(img)

    label_img = tk.Label(ventana, image=img_tk)
    label_img.image = img_tk  # mantener referencia
    label_img.pack(pady=10)
except Exception:
    tk.Label(ventana, text="No se pudo cargar la imagen.").pack()

# Ejecutar ventana
ventana.mainloop()
