class AlumnosApp:
    def __init__(self):
        self.nombres = []
        self.notas = []

    def menu(self):
        while True:
            print("\n--- Menú Alumnos ---")
            print("1) Cargar alumnos")
            print("2) Listar alumnos")
            print("3) Mostrar alumnos con nota >= 11")
            print("4) Finalizar")
            op = input("Opción: ").strip()
            if op == "1":
                self.cargar()
            elif op == "2":
                self.listar()
            elif op == "3":
                self.mayores_11()
            elif op == "4":
                print("Fin del programa.")
                break
            else:
                print("Opción inválida.")

    def cargar(self):
        self.nombres.clear(); self.notas.clear()
        print("Ingrese 5 alumnos (nombre y nota).")
        for i in range(5):
            nombre = input(f"Nombre {i+1}: ").strip()
            nota = self._leer_nota(f"Nota {i+1} (0-20): ")
            self.nombres.append(nombre); self.notas.append(nota)
        print("Carga completa.")

    def _leer_nota(self, msg):
        while True:
            try:
                n = float(input(msg))
                if 0 <= n <= 20: return n
                print("La nota debe estar entre 0 y 20.")
            except ValueError:
                print("Entrada no válida.")

    def listar(self):
        if not self.nombres:
            print("No hay alumnos cargados."); return
        print("\nListado:")
        for nom, nota in zip(self.nombres, self.notas):
            print(f"- {nom}: {nota}")

    def mayores_11(self):
        if not self.nombres:
            print("Primero cargue alumnos."); return
        print("\nAlumnos con nota >= 11:")
        hay = False
        for nom, nota in zip(self.nombres, self.notas):
            if nota >= 11:
                print(f"- {nom}: {nota}"); hay = True
        if not hay: print("Ninguno.")

app = AlumnosApp()
app.menu()
