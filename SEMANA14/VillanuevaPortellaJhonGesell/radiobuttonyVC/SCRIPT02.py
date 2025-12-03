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
    window.title("Radio Buttons con imágenes - Item 2")

    options = [
        "Moto 01",
        "Moto 02",
        "Moto 03",
        "Moto 04",
    ]

    selected_option = tk.IntVar(value=0)
    photos = load_images()

    for index, (text, photo) in enumerate(zip(options, photos)):
        row = index // 2
        column = index % 2

        image_label = tk.Label(window, image=photo)
        image_label.image = photo
        image_label.grid(row=row * 2, column=column, padx=10, pady=(10, 0))

        radio = tk.Radiobutton(
            window,
            text=text,
            variable=selected_option,
            value=index + 1,
            indicatoron=True,
        )
        radio.grid(row=row * 2 + 1, column=column, padx=10, pady=(0, 10), sticky="w")

    window.mainloop()


if __name__ == "__main__":
    main()
