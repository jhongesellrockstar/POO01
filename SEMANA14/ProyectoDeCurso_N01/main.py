"""Punto de entrada principal para SaludTurno."""
import tkinter as tk

from database import Database
from borrador import SaludTurnoApp


def main():
    db = Database()
    db.init_schema()
    root = tk.Tk()
    app = SaludTurnoApp(root, db=db)
    app.run()


if __name__ == "__main__":
    main()
