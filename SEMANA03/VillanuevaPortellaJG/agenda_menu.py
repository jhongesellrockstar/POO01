class Contacto:
    def __init__(self, nombre, telefono, mail):
        self.nombre = nombre; self.telefono = telefono; self.mail = mail

class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        while True:
            print("\n--- Agenda ---")
            print("1) Cargar contacto")
            print("2) Listado completo")
            print("3) Consultar por nombre")
            print("4) Modificar teléfono y mail")
            print("5) Finalizar")
            op = input("Opción: ").strip()
            if op == "1": self.cargar()
            elif op == "2": self.listado()
            elif op == "3": self.consultar()
            elif op == "4": self.modificar()
            elif op == "5":
                print("Fin."); break
            else: print("Opción inválida.")

    def cargar(self):
        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        mail = input("Mail: ").strip()
        self.contactos.append(Contacto(nombre, telefono, mail))
        print("Contacto agregado.")

    def listado(self):
        if not self.contactos:
            print("Agenda vacía."); return
        print("\nAgenda:")
        for c in self.contactos:
            print(f"- {c.nombre} | Tel: {c.telefono} | Mail: {c.mail}")

    def _buscar(self, nombre):
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower(): return c
        return None

    def consultar(self):
        nombre = input("Nombre a buscar: ").strip()
        c = self._buscar(nombre)
        if c: print(f"Encontrado: {c.nombre} | Tel: {c.telefono} | Mail: {c.mail}")
        else: print("No existe.")

    def modificar(self):
        nombre = input("Nombre a modificar: ").strip()
        c = self._buscar(nombre)
        if not c:
            print("No existe."); return
        c.telefono = input("Nuevo teléfono: ").strip()
        c.mail = input("Nuevo mail: ").strip()
        print("Actualizado.")

Agenda().menu()
