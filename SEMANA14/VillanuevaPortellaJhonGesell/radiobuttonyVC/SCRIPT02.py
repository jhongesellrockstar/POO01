import tkinter as tk
from PIL import Image, ImageTk


IMAGE_PATHS = [
    "Figuras_a_usar/Figure01.png",
    "Figuras_a_usar/Figure02.jpg",
    "Figuras_a_usar/Figure03.jpg",
    "Figuras_a_usar/Figure04.png",
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
        "Opción Norte",
        "Opción Sur",
        "Opción Este",
        "Opción Oeste",
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
