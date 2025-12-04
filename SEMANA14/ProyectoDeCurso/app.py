import shutil
from datetime import datetime, timedelta
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from database import Database
from models import Cita, Especialidad, Hospital, Paciente, hash_password

BASE_DIR = Path(__file__).resolve().parent
MEDIA_DIR = BASE_DIR / "media" / "profiles"
REPORTS_DIR = BASE_DIR / "reports"
MEDIA_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

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
        Hospital(7, "Hospital Nacional Alberto Sabogal", 0.62, 0.42, "Seguro", [esp_general, esp_cardiologia, esp_gineco]),
        Hospital(8, "Hospital Nacional Arzobispo Loayza", 0.40, 0.15, "SIS", [esp_general, esp_gineco, esp_pediatria]),
        Hospital(9, "Hospital Guillermo Almenara", 0.15, 0.45, "Seguro", [esp_general, esp_cardiologia, esp_trauma]),
        Hospital(10, "Clínica Internacional San Borja", 0.78, 0.48, "Privado", [esp_general, esp_cardiologia, esp_gineco]),
        Hospital(11, "Clínica Ricardo Palma", 0.68, 0.20, "Privado", [esp_general, esp_pediatria, esp_trauma]),
        Hospital(12, "Hospital de Emergencias Villa El Salvador", 0.33, 0.80, "SIS", [esp_general, esp_trauma]),
        Hospital(13, "Hospital María Auxiliadora", 0.48, 0.88, "SIS", [esp_general, esp_gineco, esp_pediatria]),
        Hospital(14, "Hospital Cayetano Heredia", 0.22, 0.60, "Seguro", [esp_general, esp_cardiologia, esp_trauma]),
        Hospital(15, "Clínica Delgado", 0.70, 0.32, "Privado", [esp_general, esp_cardiologia, esp_gineco]),
        Hospital(16, "Clínica Anglo Americana", 0.60, 0.12, "Privado", [esp_general, esp_pediatria, esp_cardiologia]),
    ]
    return hospitals

HOSPITALES = build_sample_hospitals()


def save_profile_image(source_path: str | Path) -> str | None:
    try:
        src = Path(source_path)
        if not src.exists():
            return None
        destination = MEDIA_DIR / f"{src.stem}_{int(datetime.now().timestamp())}{src.suffix}"
        shutil.copy(src, destination)
        return str(destination)
    except Exception:
        print("error")
    return None


def _escape_pdf_text(text: str) -> str:
    return text.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")


def _write_basic_pdf(title: str, lines: list[str], output_path: Path) -> Path | None:
    try:
        content_lines = []
        y_pos = 760
        content_lines.append(f"BT /F1 16 Tf 72 {y_pos} Td ({_escape_pdf_text(title)}) Tj ET")
        y_pos -= 24
        for line in lines:
            content_lines.append(f"BT /F1 11 Tf 72 {y_pos} Td ({_escape_pdf_text(line)}) Tj ET")
            y_pos -= 16
        stream = "\n".join(content_lines)
        stream_bytes = stream.encode("utf-8")

        objects = [
            "1 0 obj<< /Type /Catalog /Pages 2 0 R >>endobj\n",
            "2 0 obj<< /Type /Pages /Kids [3 0 R] /Count 1 >>endobj\n",
            "3 0 obj<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>endobj\n",
            f"4 0 obj<< /Length {len(stream_bytes)} >>stream\n{stream}\nendstream endobj\n",
            "5 0 obj<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>endobj\n",
        ]

        pdf_parts = ["%PDF-1.4\n"]
        offsets = []
        cursor = len(pdf_parts[0])
        for obj in objects:
            offsets.append(cursor)
            pdf_parts.append(obj)
            cursor += len(obj.encode("utf-8"))

        xref_start = cursor
        xref_lines = ["xref", "0 6", "0000000000 65535 f "]
        for off in offsets:
            xref_lines.append(f"{off:010d} 00000 n ")
        trailer = "trailer<< /Size 6 /Root 1 0 R >>"
        startxref = f"startxref\n{xref_start}"
        pdf_parts.append("\n".join(xref_lines) + "\n" + trailer + "\n" + startxref + "\n%%EOF")

        output_path.write_text("".join(pdf_parts), encoding="utf-8")
        return output_path
    except Exception:
        print("error")
        return None


def generate_pdf_report(paciente: Paciente, citas: list[Cita], output_path: Path) -> Path | None:
    try:
        lines = [f"Paciente: {paciente.nombre} ({paciente.dni})", f"Correo: {paciente.correo}", ""]
        if not citas:
            lines.append("Sin citas registradas.")
        else:
            for c in citas:
                lines.append(
                    f"- {c.fecha} {c.hora} | {c.especialidad} en {c.hospital_nombre} — Estado: {c.estado}"
                )
        return _write_basic_pdf("Historial de citas - SaludTurno", lines, output_path)
    except Exception:
        print("error")
        return None

# ----------------------------
# Aplicación con Tkinter (frames que cambian)
# ----------------------------
class SaludTurnoApp:
    def __init__(self, root, db: Database | None = None):
        self.root = root
        root.title("SaludTurno - Gestión de Citas (Simulado)")
        root.geometry("1000x650")
        root.resizable(False, False)

        self.db = db or Database()
        self.db.init_schema()
        self.current_user: Paciente | None = None
        self.selected_hospital: Hospital | None = None
        self.profile_image_obj = None
        self.signup_profile_path: str | None = None

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
        self.signup_profile_path = None

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

        ttk.Label(self.frame_signup, text="Foto de perfil (opcional):").grid(column=0, row=5, sticky="e")
        btn_photo = ttk.Button(self.frame_signup, text="Seleccionar", command=self.select_signup_photo)
        btn_photo.grid(column=1, row=5, pady=4, sticky="w")
        self.signup_photo_label = ttk.Label(self.frame_signup, text="Sin imagen cargada")
        self.signup_photo_label.grid(column=1, row=5, padx=(90,0), sticky="w")

        btn_create = ttk.Button(self.frame_signup, text="Crear cuenta", command=self.create_account_action)
        btn_create.grid(column=0, row=6, columnspan=2, pady=(10,0))

        # Botón para volver al login si cambió de opinión
        btn_back = ttk.Button(self.frame_signup, text="Volver al inicio", command=lambda: self.show_login_frame())
        btn_back.grid(column=0, row=7, columnspan=2, pady=(6,0))

    def hide_all_frames(self):
        for f in [self.frame_login, self.frame_signup, self.frame_main, self.frame_booking]:
            if f:
                try:
                    f.destroy()
                except:
                    pass

    def select_signup_photo(self):
        try:
            file_path = filedialog.askopenfilename(
                title="Selecciona una foto",
                filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif"), ("Todos", "*.*")],
            )
            if not file_path:
                return
            stored = save_profile_image(file_path)
            if stored:
                self.signup_profile_path = stored
                if hasattr(self, "signup_photo_label"):
                    self.signup_photo_label.config(text=Path(file_path).name)
            else:
                messagebox.showerror("Error", "No se pudo guardar la imagen de perfil.")
        except Exception:
            print("error")

    # ----------------------------
    # Acciones de Login / Signup
    # ----------------------------
    def login_action(self):
        key = self.login_entry_user.get().strip()
        pw = self.login_entry_pass.get()
        if not key or not pw:
            messagebox.showwarning("Falta información", "Ingresa DNI/correo y contraseña.")
            return

        try:
            user = self.db.get_user_by_identifier(key)
        except Exception:
            print("error")
            user = None

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
        if self.db.get_user_by_dni(dni):
            messagebox.showerror("Error", "Ya existe un usuario con ese DNI.")
            return
        if self.db.get_user_by_correo(correo):
            messagebox.showerror("Error", "Correo ya en uso.")
            return
        ph = hash_password(pw)
        p = Paciente(dni, correo, nombre, ph, self.signup_profile_path)
        try:
            self.db.create_user(p)
            messagebox.showinfo("Cuenta creada", "Cuenta creada exitosamente.")
        except Exception:
            print("error")
            messagebox.showerror("Error", "No se pudo crear la cuenta.")
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
        ttk.Label(control, text="Perfil actual:").pack(anchor="w")
        self.profile_text = tk.StringVar(value=self._profile_label())
        ttk.Label(control, textvariable=self.profile_text, wraplength=200).pack(anchor="w")
        ttk.Button(control, text="Actualizar foto", command=self.change_profile_photo).pack(anchor="w", pady=4)

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

    def _profile_label(self):
        if self.current_user and self.current_user.profile_image:
            return f"Foto: {Path(self.current_user.profile_image).name}"
        return "Foto: sin cargar"

    def change_profile_photo(self):
        try:
            file_path = filedialog.askopenfilename(
                title="Actualizar foto de perfil",
                filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif"), ("Todos", "*.*")],
            )
            if not file_path or not self.current_user:
                return
            stored = save_profile_image(file_path)
            if not stored:
                messagebox.showerror("Error", "No se pudo guardar la imagen.")
                return
            self.current_user.actualizar_foto(stored)
            self.db.update_profile_image(self.current_user.dni, stored)
            if hasattr(self, "profile_text"):
                self.profile_text.set(self._profile_label())
            messagebox.showinfo("Actualizado", "Foto de perfil actualizada.")
        except Exception:
            print("error")
            messagebox.showerror("Error", "No se pudo actualizar la foto de perfil.")

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
        texto = (
            f"Hospital: {hospital.nombre}\n"
            f"Afiliación: {hospital.afiliacion}\n"
            f"Especialidad: {esp}\n"
            f"Fecha: {fecha}\n"
            f"Hora: {hora}\n"
            f"Usuario: {self.current_user.nombre}\n"
        )
        self.resumen_text.config(state="normal")
        self.resumen_text.delete("1.0", tk.END)
        self.resumen_text.insert("1.0", texto)
        self.resumen_text.config(state="disabled")

    def confirm_booking(self, hospital):
        especialidad = self.especialidad_var.get()
        if not especialidad:
            messagebox.showwarning("Selecciona especialidad", "Debes escoger una especialidad para reservar.")
            return

        fecha = self.date_combo.get()
        hora = self.hora_combo.get()
        cita = Cita(
            self.current_user.dni,
            hospital.id,
            hospital.nombre,
            especialidad,
            fecha,
            hora,
        )
        try:
            self.db.add_appointment(cita)
            self.current_user.agregar_cita(cita)
            messagebox.showinfo(
                "Cita reservada",
                f"Cita en {hospital.nombre} para {especialidad} el {fecha} a las {hora} registrada con éxito.",
            )
            self.back_to_map()
        except Exception:
            print("error")
            messagebox.showerror("Error", "No se pudo registrar la cita.")

    def show_historial(self):
        self.current_user.historial = self.db.list_appointments(self.current_user.dni)
        if not self.current_user.historial:
            messagebox.showinfo("Historial vacío", "Aún no tienes citas registradas.")
            return

        ventana = tk.Toplevel(self.root)
        ventana.title("Historial de citas")
        ventana.geometry("700x300")

        cols = ("hospital", "especialidad", "fecha", "hora", "estado")
        tree = ttk.Treeview(ventana, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col.capitalize())
            tree.column(col, width=120)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        for c in self.current_user.historial:
            tree.insert(
                "",
                tk.END,
                values=(c.hospital_nombre, c.especialidad, c.fecha, c.hora, c.estado),
            )

        ttk.Button(
            ventana,
            text="Exportar historial a PDF",
            command=lambda: self.export_historial_pdf(),
        ).pack(pady=6)

    def export_historial_pdf(self):
        try:
            if not self.current_user:
                messagebox.showerror("Error", "No hay usuario en sesión.")
                return
            citas = self.current_user.historial if self.current_user.historial else []
            if not citas:
                messagebox.showinfo("Sin datos", "No hay citas para exportar.")
                return
            filename = REPORTS_DIR / f"historial_{self.current_user.dni}_{int(datetime.now().timestamp())}.pdf"
            result = generate_pdf_report(self.current_user, citas, filename)
            if result:
                messagebox.showinfo("Reporte listo", f"PDF guardado en:\n{result}")
            else:
                messagebox.showerror("Error", "No se pudo generar el PDF.")
        except Exception:
            print("error")
            messagebox.showerror("Error", "Ocurrió un problema al exportar el PDF.")

    def run(self):
        self.root.mainloop()


def main():
    root = tk.Tk()
    db = Database()
    db.init_schema()
    app = SaludTurnoApp(root, db=db)
    app.run()


if __name__ == "__main__":
    main()
