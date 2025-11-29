"""Ventana de login con imagen y apertura de nueva ventana al hacer clic.

Requisitos del docente (resumen):
- Título de la ventana.
- Cargar una imagen en la ventana.
- Un botón que al hacer clic abra una nueva ventana (mínimo 300x300 px).
- Campos de "Usuario" y "Contraseña" con entrada enmascarada con asteriscos.

Para usarlo:
- Coloca una imagen en la carpeta "imagenes/script02".
- Ejecuta: python script02.py
"""

from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

IMG_PATH = Path(__file__).parent / "imagenes" / "script02"
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"}


def load_login_image():
    for image_path in sorted(IMG_PATH.iterdir()):
        if image_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        with Image.open(image_path) as img:
            resized = img.resize((250, int(img.height * (250 / img.width))), Image.LANCZOS)
            return ImageTk.PhotoImage(resized)
    # Placeholder simple
    placeholder = Image.new("RGB", (250, 160), color="#cfd8dc")
    return ImageTk.PhotoImage(placeholder)


def open_welcome_window(username: str):
    top = tk.Toplevel()
    top.title("Panel principal")
    top.minsize(300, 300)
    ttk.Label(top, text=f"Bienvenido, {username or 'usuario'}", font=("Arial", 14)).pack(
        pady=20
    )


def build_ui(root):
    root.title("Login con imagen")
    root.geometry("500x400")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill=tk.BOTH, expand=True)

    login_image = load_login_image()
    image_label = ttk.Label(main_frame, image=login_image)
    image_label.image = login_image
    image_label.pack(pady=(0, 15))

    ttk.Label(main_frame, text="Usuario").pack(anchor=tk.W)
    username_var = tk.StringVar()
    username_entry = ttk.Entry(main_frame, textvariable=username_var)
    username_entry.pack(fill=tk.X, pady=(0, 10))

    ttk.Label(main_frame, text="Contraseña").pack(anchor=tk.W)
    password_var = tk.StringVar()
    password_entry = ttk.Entry(main_frame, textvariable=password_var, show="*")
    password_entry.pack(fill=tk.X, pady=(0, 20))

    def on_login():
        open_welcome_window(username_var.get())

    login_button = ttk.Button(main_frame, text="Ingresar", command=on_login)
    login_button.pack(fill=tk.X)

    username_entry.focus()


def main():
    root = tk.Tk()
    build_ui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
