import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

IMG_DIR = os.path.join(os.path.dirname(__file__), "imagenes", "script01")
TARGET_WIDTH = 400
MAX_IMAGES = 4
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"}


def load_images():
    images = []
    for name in sorted(os.listdir(IMG_DIR)):
        path = os.path.join(IMG_DIR, name)
        if not os.path.isfile(path):
            continue
        if os.path.splitext(name)[1].lower() not in SUPPORTED_EXTENSIONS:
            continue
        with Image.open(path) as img:
            ratio = TARGET_WIDTH / float(img.width)
            resized_height = int(img.height * ratio)
            resized = img.resize((TARGET_WIDTH, resized_height), Image.LANCZOS)
            images.append(ImageTk.PhotoImage(resized))
        if len(images) >= MAX_IMAGES:
            break
    return images


def placeholder_images():
    colors = ["#e57373", "#64b5f6", "#81c784", "#ffb74d"]
    placeholders = []
    for color in colors:
        img = Image.new("RGB", (TARGET_WIDTH, int(TARGET_WIDTH * 0.65)), color=color)
        placeholders.append(ImageTk.PhotoImage(img))
    return placeholders


def build_ui(root):
    root.title("Galería de imágenes (400px de ancho)")
    main_frame = ttk.Frame(root, padding=10)
    main_frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    images = load_images()
    if not images:
        images = placeholder_images()

    for index, image in enumerate(images):
        row, col = divmod(index, 2)
        frame = ttk.Frame(scrollable_frame, padding=5)
        frame.grid(row=row, column=col, sticky="nsew")
        label = ttk.Label(frame, image=image)
        label.image = image
        label.pack()

    for col in range(2):
        scrollable_frame.columnconfigure(col, weight=1)


def main():
    root = tk.Tk()
    build_ui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
