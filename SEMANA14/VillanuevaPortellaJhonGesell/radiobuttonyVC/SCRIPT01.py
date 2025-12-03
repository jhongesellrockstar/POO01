import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Radio Buttons - Item 1")

    options = [
        "Moto 01",
        "Moto 02",
        "Moto 03",
        "Moto 04",
    ]

    selected_option = tk.IntVar(value=0)

    for index, text in enumerate(options):
        row = index // 2
        column = index % 2
        radio = tk.Radiobutton(
            window,
            text=text,
            variable=selected_option,
            value=index + 1,
            indicatoron=True,
        )
        radio.grid(row=row, column=column, padx=10, pady=10, sticky="w")

    window.mainloop()


if __name__ == "__main__":
    main()
