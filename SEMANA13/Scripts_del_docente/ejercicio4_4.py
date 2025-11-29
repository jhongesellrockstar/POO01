import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class AplicacionAvanzada(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- Configuración de ventana ---
        self.title("Tkinter Avanzado - Demo Completa")
        self.geometry("600x500")
        self.configure(bg="#f2f2f2")

        # Intento de cargar icono
        self.cargar_icono()

        # Frame principal con estilo
        self.marco = tk.Frame(self, bg="#ffffff", relief="ridge", bd=3)
        self.marco.pack(padx=20, pady=20, fill="both", expand=True)

        # Widgets
        self.crear_widgets()

    # -------------------------------------------------------------
    def cargar_icono(self):
        """Carga un icono .ico con manejo de errores."""
        try:
            self.iconbitmap("world.ico")
        except Exception:
            print("No se pudo cargar icono.ico (Continuando...)")

    # -------------------------------------------------------------
    def crear_widgets(self):
        """Crea todos los widgets principales."""
        
        # Label título
        titulo = tk.Label(self.marco, text="Formulario Avanzado",
                          font=("Arial", 18, "bold"), bg="#ffffff")
        titulo.pack(pady=10)

        # Entry con validación
        self.entry_texto = tk.Entry(self.marco, font=("Arial", 14))
        self.entry_texto.pack(pady=5)

        # Botón procesar
        btn_procesar = tk.Button(self.marco, text="Procesar entrada",
                                 font=("Arial", 12),
                                 command=self.procesar_texto)
        btn_procesar.pack(pady=10)

        # Text multilinea
        self.caja_texto = tk.Text(self.marco, width=50, height=6, font=("Arial", 12))
        self.caja_texto.pack(pady=10)

        # Cargar imagen
        self.label_imagen = tk.Label(self.marco, bg="#ffffff")
        self.label_imagen.pack(pady=10)

        btn_imagen = tk.Button(self.marco, text="Cargar imagen",
                               font=("Arial", 12),
                               command=self.cargar_imagen)
        btn_imagen.pack(pady=5)

    # -------------------------------------------------------------
    def procesar_texto(self):
        """Procesa texto del Entry con validación y manejo de excepciones."""
        try:
            texto = self.entry_texto.get()

            if not texto.strip():
                raise ValueError("El campo de texto está vacío.")

            self.caja_texto.insert(tk.END, f"✔ Entrada válida: {texto}\n")
            messagebox.showinfo("Correcto", "Texto procesado correctamente.")

        except ValueError as e:
            messagebox.showwarning("Advertencia", str(e))

        except Exception as e:
            messagebox.showerror("Error inesperado", f"Ocurrió un error: {e}")

    # -------------------------------------------------------------
    def cargar_imagen(self):
        """Permite seleccionar imagen y la carga con manejo de errores."""
        try:
            ruta = filedialog.askopenfilename(
                title="Seleccionar imagen",
                filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif")]
            )

            if not ruta:
                return  # usuario canceló

            img = Image.open('naturaleza.jpg')
            img = img.resize((250, 250))
            img_tk = ImageTk.PhotoImage(img)

            self.label_imagen.config(image=img_tk)
            self.label_imagen.image = img_tk  # evitar que python libere la imagen

            self.caja_texto.insert(tk.END, f"✔ Imagen cargada: {ruta}\n")

        except Exception as e:
            messagebox.showerror("Error al cargar imagen", f"No se pudo cargar la imagen:\n{e}")

# -------------------------------------------------------------
if __name__ == "__main__":
    app = AplicacionAvanzada()
    app.mainloop()
