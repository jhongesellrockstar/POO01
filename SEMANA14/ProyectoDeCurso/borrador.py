import tkinter as tk
from tkinter import ttk, messagebox
import json
import hashlib
from datetime import datetime, timedelta

# ----------------------------
# POO: Clases del dominio
# ----------------------------
class Paciente:
    def _init_(self, dni, correo, nombre, password_hash):
        self.dni = dni
        self.correo = correo
        self.nombre = nombre
        self.password_hash = password_hash
        self.historial = []

    def agregar_cita(self, cita):
        self.historial.append(cita)

    def to_dict(self):
        return {
            "dni": self.dni,
            "correo": self.correo,
            "nombre": self.nombre,
            "password_hash": self.password_hash,
            "historial": [c.to_dict() for c in self.historial]
        }

    @staticmethod
    def from_dict(d):
        p = Paciente(d['dni'], d['correo'], d['nombre'], d['password_hash'])
        p.historial = [Cita.from_dict(cd) for cd in d.get('historial', [])]
        return p

class Medico:
    def _init_(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

class Especialidad:
    def _init_(self, nombre):
        self.nombre = nombre

class Hospital:
    def _init(self, id, nombre, x, y, afiliacion, especialidades):
        self.id = id_
        self.nombre = nombre
        self.x = x
        self.y = y
        self.afiliacion = afiliacion
        self.especialidades = especialidades

class Cita:
    def _init_(self, paciente_dni, hospital_id, hospital_nombre, especialidad, fecha, hora, estado="Reservada"):
        self.paciente_dni = paciente_dni
        self.hospital_id = hospital_id
        self.hospital_nombre = hospital_nombre
        self.especialidad = especialidad
        self.fecha = fecha
        self.hora = hora
        self.estado = estado

    def to_dict(self):
        return {
            "paciente_dni": self.paciente_dni,
            "hospital_id": self.hospital_id,
            "hospital_nombre": self.hospital_nombre,
            "especialidad": self.especialidad,
            "fecha": self.fecha,
            "hora": self.hora,
            "estado": self.estado
        }

    @staticmethod
    def from_dict(d):
        return Cita(d['paciente_dni'], d['hospital_id'], d['hospital_nombre'],
                    d['especialidad'], d['fecha'], d['hora'], d.get('estado', 'Reservada'))

# ----------------------------
# Persistencia simple de usuarios
# ----------------------------
USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {k: Paciente.from_dict(v) for k, v in data.items()}
    except FileNotFoundError:
        return {}
    except Exception as e:
        print("Error cargando users:", e)
        return {}

def save_users(users):
    data = {k: v.to_dict() for k, v in users.items()}
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def hash_password(pw):
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

# ----------------------------
# Datos de hospitales del Callao (simulados)
# ----------------------------
def build_sample_hospitals():
    esp_general = Especialidad("Medicina General")
    esp_pediatria = Especialidad("Pediatría")
    esp_gineco = Especialidad("Ginecología")
    esp_cardiologia = Especialidad("Cardiología")
    esp_trauma = Especialidad("Traumatología")
    hospitals = [
        Hospital(1, "Hospital Regional del Callao", 0.55, 0.35, "SIS", [esp_general, esp_cardiologia, esp_pediatria]),
        Hospital(2, "Hospital Daniel Alcides Carrión", 0.30, 0.50, "Seguro", [esp_general, esp_trauma]),
        Hospital(3, "Clínica San Juan (Privado)", 0.75, 0.60, "Privado", [esp_general, esp_gineco]),
        Hospital(4, "Posta Salud A (Callao Centro)", 0.45, 0.70, "SIS", [esp_general, esp_pediatria]),
        Hospital(5, "Posta Salud B (La Perla)", 0.20, 0.25, "Seguro", [esp_general, esp_gineco]),
        Hospital(6, "Centro de Salud Ventanilla", 0.85, 0.25, "SIS", [esp_general, esp_trauma]),
    ]
    return hospitals

HOSPITALES = build_sample_hospitals()

# ----------------------------
# Aplicación con Tkinter (frames que cambian)
# ----------------------------
class SaludTurnoApp:
    def _init_(self, root):
        self.root = root
        root.title("SaludTurno - Gestión de Citas (Simulado)")
        root.geometry("1000x650")
        root.resizable(False, False)

        self.users = load_users()
        self.current_user = None
        self.selected_hospital = None

        # frames (inicialmente None)
        self.frame_login = None
        self.frame_signup = None
        self.frame_main = None
        self.frame_booking = None

        self.show_login_frame()

    # ----------------------------
    # Frame: LOGIN (solo login)
    # ----------------------------
    def show_login_frame(self, prefill_dni=None, prefill_pw=None):
        self.hide_all_frames()
        self.frame_login = ttk.Frame(self.root, padding=20)
        self.frame_login.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(self.frame_login, text="Bienvenido a SaludTurno", font=("Helvetica", 18)).grid(column=0, row=0, columnspan=2, pady=(0,10))

        ttk.Label(self.frame_login, text="DNI o Correo:").grid(column=0, row=1, sticky="e")
        self.login_entry_user = ttk.Entry(self.frame_login, width=30)
        self.login_entry_user.grid(column=1, row=1, pady=5)
        if prefill_dni:
            self.login_entry_user.insert(0, prefill_dni)

        ttk.Label(self.frame_login, text="Contraseña:").grid(column=0, row=2, sticky="e")
        self.login_entry_pass = ttk.Entry(self.frame_login, width=30, show="*")
        self.login_entry_pass.grid(column=1, row=2, pady=5)
        if prefill_pw:
            self.login_entry_pass.insert(0, prefill_pw)

        btn_login = ttk.Button(self.frame_login, text="Iniciar sesión", command=self.login_action)
        btn_login.grid(column=0, row=3, columnspan=2, pady=8)

        ttk.Separator(self.frame_login, orient="horizontal").grid(column=0, row=4, columnspan=2, sticky="ew", pady=8)

        # Link para ir a crear cuenta
        lbl_nocuenta = ttk.Label(self.frame_login, text="¿No tienes cuenta? ", anchor="center")
        lbl_nocuenta.grid(column=0, row=5, sticky="e")
        btn_link_signup = ttk.Button(self.frame_login, text="Crear una", command=self.show_signup_frame)
        btn_link_signup.grid(column=1, row=5, sticky="w")

    # ----------------------------
    # Frame: SIGNUP (crear cuenta)
    # ----------------------------
    def show_signup_frame(self):
        self.hide_all_frames()
        self.frame_signup = ttk.Frame(self.root, padding=20)
        self.frame_signup.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(self.frame_signup, text="Crear cuenta - SaludTurno", font=("Helvetica", 16)).grid(column=0, row=0, columnspan=2, pady=(0,10))

        ttk.Label(self.frame_signup, text="Nombre completo:").grid(column=0, row=1, sticky="e")
        self.signup_entry_nombre = ttk.Entry(self.frame_signup, width=35)
        self.signup_entry_nombre.grid(column=1, row=1, pady=4)

        ttk.Label(self.frame_signup, text="DNI:").grid(column=0, row=2, sticky="e")
        self.signup_entry_dni = ttk.Entry(self.frame_signup, width=35)
        self.signup_entry_dni.grid(column=1, row=2, pady=4)

        ttk.Label(self.frame_signup, text="Correo:").grid(column=0, row=3, sticky="e")
        self.signup_entry_correo = ttk.Entry(self.frame_signup, width=35)
        self.signup_entry_correo.grid(column=1, row=3, pady=4)

        ttk.Label(self.frame_signup, text="Contraseña:").grid(column=0, row=4, sticky="e")
        self.signup_entry_pass = ttk.Entry(self.frame_signup, width=35, show="*")
        self.signup_entry_pass.grid(column=1, row=4, pady=4)

        btn_create = ttk.Button(self.frame_signup, text="Crear cuenta", command=self.create_account_action)
        btn_create.grid(column=0, row=5, columnspan=2, pady=(10,0))

        # Botón para volver al login si cambió de opinión
        btn_back = ttk.Button(self.frame_signup, text="Volver al inicio", command=lambda: self.show_login_frame())
        btn_back.grid(column=0, row=6, columnspan=2, pady=(6,0))

    def hide_all_frames(self):
        for f in [self.frame_login, self.frame_signup, self.frame_main, self.frame_booking]:
            if f:
                try:
                    f.destroy()
                except:
                    pass

    # ----------------------------
    # Acciones de Login / Signup
    # ----------------------------
    def login_action(self):
        key = self.login_entry_user.get().strip()
        pw = self.login_entry_pass.get()
        if not key or not pw:
            messagebox.showwarning("Falta información", "Ingresa DNI/correo y contraseña.")
            return

        user = None
        if key in self.users:
            user = self.users[key]
        else:
            for u in self.users.values():
                if u.correo == key:
                    user = u
                    break

        if not user:
            messagebox.showerror("No existe", "Usuario no encontrado. Crea una cuenta.")
            return

        if user.password_hash != hash_password(pw):
            messagebox.showerror("Error", "Contraseña incorrecta.")
            return

        self.current_user = user
        messagebox.showinfo("Bienvenido", f"Hola {user.nombre}, sesión iniciada.")
        self.show_main_screen()

    def create_account_action(self):
        nombre = self.signup_entry_nombre.get().strip()
        dni = self.signup_entry_dni.get().strip()
        correo = self.signup_entry_correo.get().strip()
        pw = self.signup_entry_pass.get()
        if not all([nombre, dni, correo, pw]):
            messagebox.showwarning("Falta información", "Completa todos los campos para crear la cuenta.")
            return
        if dni in self.users:
            messagebox.showerror("Error", "Ya existe un usuario con ese DNI.")
            return
        for u in self.users.values():
            if u.correo == correo:
                messagebox.showerror("Error", "Correo ya en uso.")
                return
        ph = hash_password(pw)
        p = Paciente(dni, correo, nombre, ph)
        self.users[dni] = p
        save_users(self.users)
        messagebox.showinfo("Cuenta creada", "Cuenta creada exitosamente.")
        # Volver al login y rellenar campos con lo creado
        self.show_login_frame(prefill_dni=dni, prefill_pw=pw)

    # ----------------------------
    # PANTALLA PRINCIPAL: MAPA SIMULADO + BARRA LATERAL
    # (idéntico a la versión anterior)
    # ----------------------------
    def show_main_screen(self):
        self.hide_all_frames()
        self.frame_main = ttk.Frame(self.root)
        self.frame_main.pack(fill="both", expand=True)

        top = ttk.Frame(self.frame_main, padding=8)
        top.pack(side="top", fill="x")
        ttk.Label(top, text=f"Usuario: {self.current_user.nombre} ({self.current_user.dni})", font=("Helvetica", 12)).pack(side="left")
        ttk.Button(top, text="Ver historial", command=self.show_historial).pack(side="right", padx=5)
        ttk.Button(top, text="Cerrar sesión", command=self.logout).pack(side="right")

        map_frame = ttk.Frame(self.frame_main, padding=8, borderwidth=1, relief="sunken")
        map_frame.pack(side="left", fill="both", expand=True, padx=(10,5), pady=10)

        ttk.Label(map_frame, text="Mapa del Callao (simulado)").pack(anchor="nw")
        self.canvas = tk.Canvas(map_frame, width=680, height=520, bg="#e8f3ff")
        self.canvas.pack(pady=8)
        self.canvas.create_rectangle(20,20,660,500, fill="#f7f7f7", outline="#bfbfbf")
        self.canvas.create_text(340,40, text="Callao - Mapa Simulado", font=("Helvetica", 10, "italic"))

        control = ttk.Frame(self.frame_main, padding=8)
        control.pack(side="right", fill="y", padx=(5,10), pady=10)

        ttk.Label(control, text="Filtrar por afiliación:").pack(anchor="w")
        self.afiliacion_var = tk.StringVar(value="Todos")
        for v in ["Todos", "Seguro", "SIS", "Privado", "Ambos"]:
            ttk.Radiobutton(control, text=v, variable=self.afiliacion_var, value=v, command=self.render_hospital_list).pack(anchor="w")

        ttk.Separator(control, orient="horizontal").pack(fill="x", pady=6)
        ttk.Label(control, text="Hospitales:").pack(anchor="w")

        self.hospital_listbox = tk.Listbox(control, width=35, height=12)
        self.hospital_listbox.pack(pady=4)
        self.hospital_listbox.bind("<<ListboxSelect>>", self.on_hospital_select)

        ttk.Button(control, text="Seleccionar hospital", command=self.select_hospital_button).pack(pady=6)
        ttk.Button(control, text="Reservar cita (siguiente)", command=self.goto_booking_if_selected).pack(pady=6)

        self.canvas_markers = {}
        self.render_map_markers()
        self.render_hospital_list()

    def logout(self):
        self.current_user = None
        self.show_login_frame()

    def render_map_markers(self):
        self.canvas.delete("marker")
        self.canvas_markers.clear()
        for h in HOSPITALES:
            cx = 20 + int(h.x * (660-40))
            cy = 60 + int(h.y * (500-80))
            r = 9
            color = "#2b7bff" if h.afiliacion in ("SIS","Seguro","Ambos") else "#ff7b7b"
            marker = self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color, tags=("marker",))
            text_id = self.canvas.create_text(cx, cy-15, text=h.nombre, font=("Helvetica",8), tags=("marker",))
            self.canvas_markers[h.id] = (marker, text_id)
            self.canvas.tag_bind(marker, "<Button-1>", lambda ev, hid=h.id: self.select_hospital_by_id(hid))
            self.canvas.tag_bind(text_id, "<Button-1>", lambda ev, hid=h.id: self.select_hospital_by_id(hid))

    def render_hospital_list(self):
        af = self.afiliacion_var.get()
        self.hospital_listbox.delete(0, tk.END)
        for h in HOSPITALES:
            if af == "Todos" or af == h.afiliacion or (af == "Ambos" and h.afiliacion == "Ambos"):
                display = f"{h.nombre} — {h.afiliacion}"
                self.hospital_listbox.insert(tk.END, display)

    def on_hospital_select(self, evt):
        sel = evt.widget.curselection()
        if not sel:
            return
        idx = sel[0]
        af = self.afiliacion_var.get()
        filtered = [h for h in HOSPITALES if af == "Todos" or af == h.afiliacion or (af=="Ambos" and h.afiliacion=="Ambos")]
        if idx < len(filtered):
            h = filtered[idx]
            self.highlight_hospital(h)

    def select_hospital_by_id(self, hid):
        for i,h in enumerate(HOSPITALES):
            if h.id == hid:
                self.highlight_hospital(h)
                af = self.afiliacion_var.get()
                filtered = [hh for hh in HOSPITALES if af == "Todos" or af == hh.afiliacion or (af=="Ambos" and hh.afiliacion=="Ambos")]
                try:
                    idx = filtered.index(h)
                except ValueError:
                    idx = None
                if idx is not None:
                    self.hospital_listbox.selection_clear(0, tk.END)
                    self.hospital_listbox.selection_set(idx)
                break

    def highlight_hospital(self, hospital):
        self.canvas.delete("highlight")
        cx = 20 + int(hospital.x * (660-40))
        cy = 60 + int(hospital.y * (500-80))
        self.canvas.create_rectangle(cx-40, cy-30, cx+40, cy+30, outline="#ffaa00", width=2, tags=("highlight",))
        self.selected_hospital = hospital

    def select_hospital_button(self):
        sel = self.hospital_listbox.curselection()
        if not sel:
            messagebox.showwarning("Selecciona", "Elige un hospital de la lista o marca en el mapa.")
            return
        idx = sel[0]
        af = self.afiliacion_var.get()
        filtered = [h for h in HOSPITALES if af == "Todos" or af == h.afiliacion or (af=="Ambos" and h.afiliacion=="Ambos")]
        if idx < len(filtered):
            self.selected_hospital = filtered[idx]
            self.highlight_hospital(self.selected_hospital)

    def goto_booking_if_selected(self):
        if not self.selected_hospital:
            messagebox.showwarning("Selecciona", "Selecciona un hospital primero.")
            return
        self.show_booking_screen(self.selected_hospital)

    # ----------------------------
    # PANTALLA DE RESERVA (idéntica a antes)
    # ----------------------------
    def show_booking_screen(self, hospital):
        self.hide_all_frames()
        self.frame_booking = ttk.Frame(self.root, padding=12)
        self.frame_booking.pack(fill="both", expand=True)

        top = ttk.Frame(self.frame_booking)
        top.pack(fill="x")
        ttk.Label(top, text=f"Reservar cita - {hospital.nombre}", font=("Helvetica", 14)).pack(side="left")
        ttk.Button(top, text="Atrás (Mapa)", command=self.back_to_map).pack(side="right")
        ttk.Button(top, text="Cerrar sesión", command=self.logout).pack(side="right", padx=6)

        body = ttk.Frame(self.frame_booking, padding=10)
        body.pack(fill="both", expand=True)

        left = ttk.Frame(body)
        left.pack(side="left", fill="y", padx=(0,20))
        ttk.Label(left, text=f"Afiliación: {hospital.afiliacion}").pack(anchor="w", pady=2)
        ttk.Label(left, text="Especialidades disponibles:").pack(anchor="w", pady=(8,2))

        self.especialidad_var = tk.StringVar()
        for esp in hospital.especialidades:
            ttk.Radiobutton(left, text=esp.nombre, variable=self.especialidad_var, value=esp.nombre).pack(anchor="w")

        center = ttk.Frame(body)
        center.pack(side="left", fill="y")
        ttk.Label(center, text="Elige fecha:").pack(anchor="w")
        self.date_combo = ttk.Combobox(center, values=self.next_seven_days(), state="readonly")
        self.date_combo.pack(pady=6)
        self.date_combo.current(0)

        ttk.Label(center, text="Elige hora:").pack(anchor="w")
        self.hora_combo = ttk.Combobox(center, values=self.possible_hours(), state="readonly")
        self.hora_combo.pack(pady=6)
        self.hora_combo.current(0)

        ttk.Button(center, text="Reservar cita", command=lambda: self.confirm_booking(hospital)).pack(pady=12)

        right = ttk.Frame(body)
        right.pack(side="left", fill="y", padx=(20,0))
        ttk.Label(right, text="Resumen:").pack(anchor="w")
        self.resumen_text = tk.Text(right, width=35, height=12, state="disabled")
        self.resumen_text.pack()

        self.especialidad_var.trace_add("write", lambda *a: self.update_resumen(hospital))
        self.date_combo.bind("<<ComboboxSelected>>", lambda e: self.update_resumen(hospital))
        self.hora_combo.bind("<<ComboboxSelected>>", lambda e: self.update_resumen(hospital))
        self.update_resumen(hospital)

    def back_to_map(self):
        if self.frame_booking:
            self.frame_booking.destroy()
            self.frame_booking = None
        self.show_main_screen()

    def next_seven_days(self):
        days = []
        today = datetime.today()
        for i in range(7):
            dt = today + timedelta(days=i)
            days.append(dt.strftime("%Y-%m-%d"))
        return days

    def possible_hours(self):
        return ["08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","14:00","14:30","15:00","15:30"]

    def update_resumen(self, hospital):
        esp = self.especialidad_var.get() or "(no seleccionado)"
        fecha = self.date_combo.get()
        hora = self.hora_combo.get()
        texto = f"Hospital: {hospital.nombre}\nAfiliación: {hospital.afiliacion}\nEspecialidad: {esp}\nFecha: {fecha}\nHora: {hora}\nUsuario: {self.current_user.nombre}\n"
        self.resumen_text.config(state="normal")
        self.resumen_text.delete("1.0", tk.END)
        self.resumen