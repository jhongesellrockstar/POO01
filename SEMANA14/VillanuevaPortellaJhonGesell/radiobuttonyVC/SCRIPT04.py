import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk


BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "Figuras_a_usar"
IMAGE_PATHS = [
    IMAGE_DIR / "Figure01.png",
    IMAGE_DIR / "Figure02.jpg",
    IMAGE_DIR / "Figure03.jpg",
    IMAGE_DIR / "Figure04.png",
]

BUTTON_COLORS = [
    "#ffebee",
    "#e8f5e9",
    "#e3f2fd",
    "#fff3e0",
]


def load_images(width: int = 200):
    images = []
    for path in IMAGE_PATHS:
        image = Image.open(path)
        ratio = width / image.width
        resized = image.resize((width, int(image.height * ratio)), Image.LANCZOS)
        images.append(ImageTk.PhotoImage(resized))
    return images


def main():
    window = tk.Tk()
    window.title("Radio Buttons con marco - Item 4")

    container = tk.Frame(window, bd=2, relief="groove", padx=12, pady=12, bg="#fafafa")
    container.grid(row=0, column=0, padx=20, pady=20)

    selected_option = tk.IntVar(value=0)
    photos = load_images()

    for index, (photo, color) in enumerate(zip(photos, BUTTON_COLORS)):
        row = index // 2
        column = index % 2

        image_label = tk.Label(container, image=photo, bg=container["bg"])
        image_label.image = photo
        image_label.grid(row=row * 2, column=column, padx=10, pady=(10, 0))

        radio = tk.Radiobutton(
            container,
            text=f"Moto {index + 1:02d}",
            variable=selected_option,
            value=index + 1,
            indicatoron=True,
            bg=color,
            activebackground=color,
            selectcolor="#c8e6c9",
        )
        radio.grid(row=row * 2 + 1, column=column, padx=10, pady=(0, 10), sticky="we")

    window.mainloop()


if __name__ == "__main__":
    main()
