import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

IMG_PATH = os.path.join(os.path.dirname(__file__), "imagenes", "script02")
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"}


def load_login_image():
    for name in sorted(os.listdir(IMG_PATH)):
        path = os.path.join(IMG_PATH, name)
        if not os.path.isfile(path):
            continue
        if os.path.splitext(name)[1].lower() not in SUPPORTED_EXTENSIONS:
            continue
        with Image.open(path) as img:
            width = 250
            height = int(img.height * (width / img.width))
            resized = img.resize((width, height), Image.LANCZOS)
            return ImageTk.PhotoImage(resized)
    placeholder = Image.new("RGB", (250, 160), color="#cfd8dc")
    return ImageTk.PhotoImage(placeholder)


def open_welcome_window(username):
    top = tk.Toplevel()
    top.title("Panel principal")
    top.minsize(300, 300)
    ttk.Label(top, text=f"Bienvenido, {username or 'usuario'}", font=("Arial", 14)).pack(pady=20)


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

    ttk.Button(main_frame, text="Ingresar", command=on_login).pack(fill=tk.X)
    username_entry.focus()


def main():
    root = tk.Tk()
    build_ui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
