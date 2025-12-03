import tkinter as tk
from PIL import Image, ImageTk


IMAGE_PATHS = [
    "Figuras_a_usar/Figure01.png",
    "Figuras_a_usar/Figure02.jpg",
    "Figuras_a_usar/Figure03.jpg",
    "Figuras_a_usar/Figure04.png",
]

BUTTON_COLORS = [
    "#ffebee",
    "#e8f5e9",
    "#e3f2fd",
    "#fff3e0",
]

MESSAGES = [
    "Hola Emma",
    "Accediendo a tu cuenta personal",
    "Bienvenido a configuración",
    "Entrando al panel principal",
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
    window.title("Radio Buttons con botón personalizado - Item 6")

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
            text=f"Opción {index + 1}",
            variable=selected_option,
            value=index + 1,
            indicatoron=True,
            bg=color,
            activebackground=color,
            selectcolor="#c8e6c9",
        )
        radio.grid(row=row * 2 + 1, column=column, padx=10, pady=(0, 10), sticky="we")

    message_label = tk.Label(container, text="", font=("Arial", 12), bg=container["bg"])
    message_label.grid(row=5, column=0, columnspan=2, pady=(10, 5))

    def show_message():
        selection = selected_option.get()
        if selection == 0:
            message_label.config(text="Debe seleccionar una opción", fg="red")
        else:
            message_label.config(text=MESSAGES[selection - 1], fg="black")

    action_button = tk.Button(
        container,
        text="Confirmar selección",
        command=show_message,
        bg="#1e88e5",
        fg="white",
        activebackground="#1565c0",
        activeforeground="white",
        relief="raised",
        bd=3,
        padx=14,
        pady=8,
        cursor="hand2",
        highlightthickness=0,
    )
    action_button.grid(row=4, column=0, columnspan=2, pady=(10, 5))

    window.mainloop()


if __name__ == "__main__":
    main()
