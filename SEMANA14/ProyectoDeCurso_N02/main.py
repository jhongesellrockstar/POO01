import tkinter as tk
from tkinter import ttk, messagebox
import json
import hashlib
from datetime import datetime, timedelta
import calendar
import importlib.util

# Comprobar dependencias opcionales sin atrapar excepciones en los imports
REPORTLAB_AVAILABLE = importlib.util.find_spec("reportlab") is not None
if REPORTLAB_AVAILABLE:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import inch
PDF_AVAILABLE = REPORTLAB_AVAILABLE

CV2_AVAILABLE = importlib.util.find_spec("cv2") is not None
if CV2_AVAILABLE:
    import cv2
else:
    cv2 = None

# ----------------------------
# POO: Clases del dominio
# ----------------------------
class Paciente:
    def __init__(self, dni, correo, nombre, password_hash, seguro=None):
        self.dni = dni
        self.correo = correo
        self.nombre = nombre
        self.password_hash = password_hash
        self.historial = []
        self.seguro = seguro  # Seguro del paciente

    def agregar_cita(self, cita):
        self.historial.append(cita)

    def to_dict(self):
        return {
            "dni": self.dni,
            "correo": self.correo,
            "nombre": self.nombre,
            "password_hash": self.password_hash,
            "historial": [c.to_dict() for c in self.historial],
            "seguro": self.seguro.to_dict() if self.seguro else None
        }

    @classmethod
    def from_dict(cls, d):
        seguro = Seguro.from_dict(d['seguro']) if d.get('seguro') else None
        p = cls(d['dni'], d['correo'], d['nombre'], d['password_hash'], seguro)
        p.historial = [Cita.from_dict(cd) for cd in d.get('historial', [])]
        return p

class Medico:
    def __init__(self, nombre, especialidad, horario_atencion=None, calificacion=0, reseñas=None):
        self.nombre = nombre
        self.especialidad = especialidad
        # Horario por defecto: lunes a viernes de 8:00 a 17:00
        self.horario_atencion = horario_atencion or {
            "monday": ["08:00", "17:00"],
            "tuesday": ["08:00", "17:00"],
            "wednesday": ["08:00", "17:00"],
            "thursday": ["08:00", "17:00"],
            "friday": ["08:00", "17:00"],
            "saturday": ["09:00", "13:00"],
            "sunday": ["cerrado", "cerrado"]
        }
        self.calificacion = calificacion  # Calificación promedio (0-5)
        self.reseñas = reseñas or []  # Lista de reseñas

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "especialidad": self.especialidad,
            "horario_atencion": self.horario_atencion,
            "calificacion": self.calificacion,
            "reseñas": self.reseñas
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['nombre'],
            data['especialidad'],
            data.get('horario_atencion'),
            data.get('calificacion', 0),
            data.get('reseñas', [])
        )

class Seguro:
    def __init__(self, nombre, cobertura, costo_cita=0):
        self.nombre = nombre
        self.cobertura = cobertura  # Descripción de lo que cubre
        self.costo_cita = costo_cita  # Costo de la cita con este seguro

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "cobertura": self.cobertura,
            "costo_cita": self.costo_cita
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['nombre'],
            data.get('cobertura', ''),
            data.get('costo_cita', 0)
        )

class Especialidad:
    def __init__(self, nombre, duracion_cita=30, costo_base=0):  # duración en minutos
        self.nombre = nombre
        self.duracion_cita = duracion_cita  # duración típica de la cita en minutos
        self.costo_base = costo_base  # Costo base de la especialidad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "duracion_cita": self.duracion_cita,
            "costo_base": self.costo_base
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['nombre'],
            data.get('duracion_cita', 30),
            data.get('costo_base', 0)
        )

class Hospital:
    def __init__(self, id, nombre, x, y, afiliacion, especialidades, horario=None, medicos=None, calificacion=0, reseñas=None):
        self.id = id
        self.nombre = nombre
        self.x = x
        self.y = y
        self.afiliacion = afiliacion
        self.especialidades = especialidades
        # Horario por defecto: lunes a viernes de 8:00 a 18:00, sábado 9:00 a 13:00
        self.horario = horario or {
            "monday": ["08:00", "18:00"],
            "tuesday": ["08:00", "18:00"],
            "wednesday": ["08:00", "18:00"],
            "thursday": ["08:00", "18:00"],
            "friday": ["08:00", "18:00"],
            "saturday": ["09:00", "13:00"],
            "sunday": ["cerrado", "cerrado"]
        }
        self.medicos = medicos or []  # Lista de médicos
        self.calificacion = calificacion  # Calificación promedio (0-5)
        self.reseñas = reseñas or []  # Lista de reseñas

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "x": self.x,
            "y": self.y,
            "afiliacion": self.afiliacion,
            "especialidades": [esp.to_dict() for esp in self.especialidades],
            "horario": self.horario,
            "medicos": [med.to_dict() for med in self.medicos],
            "calificacion": self.calificacion,
            "reseñas": self.reseñas
        }

    @classmethod
    def from_dict(cls, data):
        especialidades = [Especialidad.from_dict(esp_data) for esp_data in data.get('especialidades', [])]
        medicos = [Medico.from_dict(med_data) for med_data in data.get('medicos', [])]
        return cls(
            data['id'],
            data['nombre'],
            data['x'],
            data['y'],
            data['afiliacion'],
            especialidades,
            data.get('horario'),
            medicos,
            data.get('calificacion', 0),
            data.get('reseñas', [])
        )

class Cita:
    def __init__(self, paciente_dni, hospital_id, hospital_nombre, especialidad, fecha, hora, estado="Reservada", medico=None, seguro=None, costo=0):
        self.paciente_dni = paciente_dni
        self.hospital_id = hospital_id
        self.hospital_nombre = hospital_nombre
        self.especialidad = especialidad
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.medico = medico  # Nuevo campo para el médico asignado
        self.seguro = seguro  # Seguro del paciente para esta cita
        self.costo = float(costo) if costo is not None else 0.0  # Costo de la cita as float

    def to_dict(self):
        return {
            "paciente_dni": self.paciente_dni,
            "hospital_id": self.hospital_id,
            "hospital_nombre": self.hospital_nombre,
            "especialidad": self.especialidad,
            "fecha": self.fecha,
            "hora": self.hora,
            "estado": self.estado,
            "medico": self.medico,
            "seguro": self.seguro,
            "costo": float(self.costo) if self.costo is not None else 0.0
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d['paciente_dni'], d['hospital_id'], d['hospital_nombre'],
                   d['especialidad'], d['fecha'], d['hora'], d.get('estado', 'Reservada'),
                   d.get('medico'), d.get('seguro'), float(d.get('costo', 0)))

# ----------------------------
# Persistencia simple de usuarios
# ----------------------------
USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            users = {}
            for k, v in data.items():
                paciente = Paciente.from_dict(v)
                # Verificar y corregir posibles problemas con los costos en el historial de citas
                for cita in paciente.historial:
                    if hasattr(cita, 'costo') and cita.costo is not None:
                        try:
                            # Intentar convertir a float, si falla usar 0.0
                            if isinstance(cita.costo, str):
                                # Si es una cadena que representa un número, convertirla
                                cita.costo = float(cita.costo)
                            elif not isinstance(cita.costo, (int, float)):
                                # Si no es numérico, usar 0.0
                                cita.costo = 0.0
                        except (ValueError, TypeError):
                            # Si no se puede convertir, usar 0.0
                            cita.costo = 0.0
                users[k] = paciente
            return users
    except FileNotFoundError:
        return {}
    except Exception as e:
        print("Error cargando users:", e)
        return {}

def load_hospitals():
    """Cargar hospitales desde un archivo o crearlos si no existen"""
    HOSPITALS_FILE = "hospitales.json"
    try:
        with open(HOSPITALS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Hospital.from_dict(h) for h in data]
    except FileNotFoundError:
        # Si no existe el archivo, crear hospitales con médicos
        return build_sample_hospitals_with_doctors()
    except Exception as e:
        print("Error cargando hospitales:", e)
        return build_sample_hospitals_with_doctors()

def save_users(users):
    # Antes de guardar, asegurarse de que los costos sean valores numéricos consistentes
    data = {}
    for k, v in users.items():
        paciente_dict = v.to_dict()
        # Asegurar que los costos en el historial sean valores numéricos
        for cita_dict in paciente_dict.get('historial', []):
            if 'costo' in cita_dict and cita_dict['costo'] is not None:
                try:
                    if isinstance(cita_dict['costo'], str):
                        cita_dict['costo'] = float(cita_dict['costo'])
                    elif not isinstance(cita_dict['costo'], (int, float)):
                        cita_dict['costo'] = 0.0
                except (ValueError, TypeError):
                    cita_dict['costo'] = 0.0
        data[k] = paciente_dict
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def hash_password(pw):
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

# ----------------------------
# Datos de hospitales del Callao (simulados) con horarios realistas
# ----------------------------
def build_sample_hospitals():
    esp_general = Especialidad("Medicina General", 30)
    esp_pediatria = Especialidad("Pediatría", 45)
    esp_gineco = Especialidad("Ginecología", 60)
    esp_cardiologia = Especialidad("Cardiología", 45)
    esp_trauma = Especialidad("Traumatología", 40)

    # Horarios específicos para cada hospital
    horario_hospital_regional = {
        "monday": ["07:00", "19:30"],
        "tuesday": ["07:00", "19:30"],
        "wednesday": ["07:00", "19:30"],
        "thursday": ["07:00", "19:30"],
        "friday": ["07:00", "19:30"],
        "saturday": ["08:00", "14:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_hospital_carrion = {
        "monday": ["08:00", "20:00"],
        "tuesday": ["08:00", "20:00"],
        "wednesday": ["08:00", "20:00"],
        "thursday": ["08:00", "20:00"],
        "friday": ["08:00", "20:00"],
        "saturday": ["09:00", "14:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_clinica_san_juan = {
        "monday": ["08:00", "20:00"],
        "tuesday": ["08:00", "20:00"],
        "wednesday": ["08:00", "20:00"],
        "thursday": ["08:00", "20:00"],
        "friday": ["08:00", "20:00"],
        "saturday": ["09:00", "16:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_posta_salud_a = {
        "monday": ["07:30", "16:00"],
        "tuesday": ["07:30", "16:00"],
        "wednesday": ["07:30", "16:00"],
        "thursday": ["07:30", "16:00"],
        "friday": ["07:30", "16:00"],
        "saturday": ["08:00", "12:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_posta_salud_b = {
        "monday": ["07:00", "17:00"],
        "tuesday": ["07:00", "17:00"],
        "wednesday": ["07:00", "17:00"],
        "thursday": ["07:00", "17:00"],
        "friday": ["07:00", "17:00"],
        "saturday": ["08:00", "13:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_centro_salud_ventanilla = {
        "monday": ["08:00", "17:00"],
        "tuesday": ["08:00", "17:00"],
        "wednesday": ["08:00", "17:00"],
        "thursday": ["08:00", "17:00"],
        "friday": ["08:00", "17:00"],
        "saturday": ["09:00", "13:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    hospitals = [
        Hospital(1, "Hospital Regional del Callao", 0.55, 0.35, "SIS", [esp_general, esp_cardiologia, esp_pediatria], horario_hospital_regional),
        Hospital(2, "Hospital Daniel Alcides Carrión", 0.30, 0.50, "Seguro", [esp_general, esp_trauma], horario_hospital_carrion),
        Hospital(3, "Clínica San Juan (Privado)", 0.75, 0.60, "Privado", [esp_general, esp_gineco], horario_clinica_san_juan),
        Hospital(4, "Posta Salud A (Callao Centro)", 0.45, 0.70, "SIS", [esp_general, esp_pediatria], horario_posta_salud_a),
        Hospital(5, "Posta Salud B (La Perla)", 0.20, 0.25, "Seguro", [esp_general, esp_gineco], horario_posta_salud_b),
        Hospital(6, "Centro de Salud Ventanilla", 0.85, 0.25, "SIS", [esp_general, esp_trauma], horario_centro_salud_ventanilla),
    ]
    return hospitals

def build_seguros():
    """Crear seguros de ejemplo"""
    return [
        Seguro("SIS", "Cobertura para personas sin seguro privado", 0),  # Gratis con SIS
        Seguro("Seguro Privado Básico", "Cobertura básica para consultas", 20),
        Seguro("Seguro Privado Premium", "Cobertura completa para consultas y exámenes", 50),
        Seguro("Seguro para Emergencias", "Cobertura solo para emergencias", 10)
    ]

def build_sample_hospitals_with_doctors():
    esp_general = Especialidad("Medicina General", 30, 100)
    esp_pediatria = Especialidad("Pediatría", 45, 120)
    esp_gineco = Especialidad("Ginecología", 60, 150)
    esp_cardiologia = Especialidad("Cardiología", 45, 200)
    esp_trauma = Especialidad("Traumatología", 40, 180)

    # Horarios específicos para cada hospital
    horario_hospital_regional = {
        "monday": ["07:00", "19:30"],
        "tuesday": ["07:00", "19:30"],
        "wednesday": ["07:00", "19:30"],
        "thursday": ["07:00", "19:30"],
        "friday": ["07:00", "19:30"],
        "saturday": ["08:00", "14:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_hospital_carrion = {
        "monday": ["08:00", "20:00"],
        "tuesday": ["08:00", "20:00"],
        "wednesday": ["08:00", "20:00"],
        "thursday": ["08:00", "20:00"],
        "friday": ["08:00", "20:00"],
        "saturday": ["09:00", "14:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_clinica_san_juan = {
        "monday": ["08:00", "20:00"],
        "tuesday": ["08:00", "20:00"],
        "wednesday": ["08:00", "20:00"],
        "thursday": ["08:00", "20:00"],
        "friday": ["08:00", "20:00"],
        "saturday": ["09:00", "16:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_posta_salud_a = {
        "monday": ["07:30", "16:00"],
        "tuesday": ["07:30", "16:00"],
        "wednesday": ["07:30", "16:00"],
        "thursday": ["07:30", "16:00"],
        "friday": ["07:30", "16:00"],
        "saturday": ["08:00", "12:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_posta_salud_b = {
        "monday": ["07:00", "17:00"],
        "tuesday": ["07:00", "17:00"],
        "wednesday": ["07:00", "17:00"],
        "thursday": ["07:00", "17:00"],
        "friday": ["07:00", "17:00"],
        "saturday": ["08:00", "13:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    horario_centro_salud_ventanilla = {
        "monday": ["08:00", "17:00"],
        "tuesday": ["08:00", "17:00"],
        "wednesday": ["08:00", "17:00"],
        "thursday": ["08:00", "17:00"],
        "friday": ["08:00", "17:00"],
        "saturday": ["09:00", "13:00"],
        "sunday": ["cerrado", "cerrado"]
    }

    # Crear médicos para cada hospital
    medico1 = Medico("Dr. Juan Pérez", "Medicina General", {
        "monday": ["08:00", "15:00"],
        "tuesday": ["08:00", "15:00"],
        "wednesday": ["08:00", "15:00"],
        "thursday": ["08:00", "15:00"],
        "friday": ["08:00", "15:00"],
        "saturday": ["cerrado", "cerrado"],
        "sunday": ["cerrado", "cerrado"]
    }, 4.5)

    medico2 = Medico("Dra. María González", "Pediatría", {
        "monday": ["09:00", "16:00"],
        "tuesday": ["09:00", "16:00"],
        "wednesday": ["cerrado", "cerrado"],
        "thursday": ["09:00", "16:00"],
        "friday": ["09:00", "16:00"],
        "saturday": ["cerrado", "cerrado"],
        "sunday": ["cerrado", "cerrado"]
    }, 4.7)

    medico3 = Medico("Dr. Carlos Mendoza", "Cardiología", {
        "monday": ["cerrado", "cerrado"],
        "tuesday": ["10:00", "17:00"],
        "wednesday": ["10:00", "17:00"],
        "thursday": ["10:00", "17:00"],
        "friday": ["10:00", "17:00"],
        "saturday": ["cerrado", "cerrado"],
        "sunday": ["cerrado", "cerrado"]
    }, 4.2)

    medico4 = Medico("Dra. Ana Rodríguez", "Ginecología", {
        "monday": ["11:00", "18:00"],
        "tuesday": ["cerrado", "cerrado"],
        "wednesday": ["11:00", "18:00"],
        "thursday": ["11:00", "18:00"],
        "friday": ["11:00", "18:00"],
        "saturday": ["cerrado", "cerrado"],
        "sunday": ["cerrado", "cerrado"]
    }, 4.8)

    medico5 = Medico("Dr. Luis Torres", "Traumatología", {
        "monday": ["08:00", "14:00"],
        "tuesday": ["08:00", "14:00"],
        "wednesday": ["08:00", "14:00"],
        "thursday": ["08:00", "14:00"],
        "friday": ["08:00", "14:00"],
        "saturday": ["cerrado", "cerrado"],
        "sunday": ["cerrado", "cerrado"]
    }, 4.3)

    hospitals = [
        Hospital(1, "Hospital Regional del Callao", 0.55, 0.35, "SIS", [esp_general, esp_cardiologia, esp_pediatria], horario_hospital_regional, [medico1, medico2, medico3]),
        Hospital(2, "Hospital Daniel Alcides Carrión", 0.30, 0.50, "Seguro", [esp_general, esp_trauma], horario_hospital_carrion, [medico1, medico5]),
        Hospital(3, "Clínica San Juan (Privado)", 0.75, 0.60, "Privado", [esp_general, esp_gineco], horario_clinica_san_juan, [medico1, medico4]),
        Hospital(4, "Posta Salud A (Callao Centro)", 0.45, 0.70, "SIS", [esp_general, esp_pediatria], horario_posta_salud_a, [medico1, medico2]),
        Hospital(5, "Posta Salud B (La Perla)", 0.20, 0.25, "Seguro", [esp_general, esp_gineco], horario_posta_salud_b, [medico1, medico4]),
        Hospital(6, "Centro de Salud Ventanilla", 0.85, 0.25, "SIS", [esp_general, esp_trauma], horario_centro_salud_ventanilla, [medico1, medico5]),
    ]
    return hospitals

HOSPITALES = load_hospitals()

# ----------------------------
# Aplicación con Tkinter (frames que cambian)
# ----------------------------
class SaludTurnoApp:
    def __init__(self, root):
        self.root = root
        root.title("SaludTurno - Gestión de Citas (Simulado)")
        root.geometry("1000x650")
        root.resizable(False, False)

        self.users = load_users()
        self.current_user = None
        self.selected_hospital = None
        self.face_verified = False

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
        self.face_verified = False
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
    # PANTALLA PRINCIPAL: MAPA SIMULADO + BARRA LATERAL CON MEJORAS
    # ----------------------------
    def show_main_screen(self):
        self.hide_all_frames()
        self.frame_main = ttk.Frame(self.root)
        self.frame_main.pack(fill="both", expand=True)

        # Barra superior con información del usuario y opciones
        top = ttk.Frame(self.frame_main, padding=8)
        top.pack(side="top", fill="x")
        ttk.Label(top, text=f"Usuario: {self.current_user.nombre} ({self.current_user.dni})", font=("Helvetica", 12)).pack(side="left")
        ttk.Button(top, text="Ver historial", command=self.show_historial).pack(side="right", padx=5)
        ttk.Button(top, text="Cerrar sesión", command=self.logout).pack(side="right")

        # Marco para el mapa
        map_frame = ttk.Frame(self.frame_main, padding=8, borderwidth=1, relief="sunken")
        map_frame.pack(side="left", fill="both", expand=True, padx=(10,5), pady=10)

        ttk.Label(map_frame, text="Mapa del Callao (simulado)", font=("Helvetica", 12, "bold")).pack(anchor="nw")
        self.canvas = tk.Canvas(map_frame, width=680, height=520, bg="#e8f3ff")
        self.canvas.pack(pady=8)

        # Agregar una cuadrícula para mejorar la visualización
        self.canvas.create_rectangle(20,20,660,500, fill="#f7f7f7", outline="#bfbfbf")
        # Dibujar elementos del mapa
        self.canvas.create_text(340,40, text="Callao - Mapa Simulado", font=("Helvetica", 12, "bold"))

        # Agregar algunos elementos visuales que simulen calles o áreas
        self.canvas.create_line(20, 100, 660, 100, dash=(2, 2), fill="#cccccc")
        self.canvas.create_line(20, 200, 660, 200, dash=(2, 2), fill="#cccccc")
        self.canvas.create_line(20, 300, 660, 300, dash=(2, 2), fill="#cccccc")
        self.canvas.create_line(20, 400, 660, 400, dash=(2, 2), fill="#cccccc")

        self.canvas.create_line(100, 20, 100, 500, dash=(2, 2), fill="#cccccc")
        self.canvas.create_line(200, 20, 200, 500, dash=(2, 2), fill="#cccccc")
        self.canvas.create_line(300, 20, 300, 500, dash=(2, 2), fill="#cccccc")
        self.canvas.create_line(400, 20, 400, 500, dash=(2, 2), fill="#cccccc")
        self.canvas.create_line(500, 20, 500, 500, dash=(2, 2), fill="#cccccc")

        # Área para información del hospital seleccionado
        info_frame = ttk.Frame(map_frame)
        info_frame.pack(side="bottom", fill="x", pady=5)
        self.info_label = ttk.Label(info_frame, text="Selecciona un hospital para ver información", font=("Helvetica", 9, "italic"))
        self.info_label.pack()

        control = ttk.Frame(self.frame_main, padding=8)
        control.pack(side="right", fill="y", padx=(5,10), pady=10)

        # Búsqueda avanzada
        ttk.Label(control, text="Búsqueda avanzada:", font=("Helvetica", 10, "bold")).pack(anchor="w")

        # Campo de búsqueda
        self.search_var = tk.StringVar()
        search_frame = ttk.Frame(control)
        search_frame.pack(fill="x", pady=4)
        ttk.Label(search_frame, text="Buscar:").pack(side="left")
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=20)
        search_entry.pack(side="right", fill="x", expand=True)
        self.search_var.trace_add("write", lambda *a: self.filtrar_hospitales())

        # Filtros adicionales
        ttk.Label(control, text="Filtrar por:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(10,0))

        ttk.Label(control, text="Afiliación:", font=("Helvetica", 9)).pack(anchor="w")
        self.afiliacion_var = tk.StringVar(value="Todos")
        for v in ["Todos", "Seguro", "SIS", "Privado"]:
            ttk.Radiobutton(control, text=v, variable=self.afiliacion_var, value=v, command=self.render_hospital_list).pack(anchor="w")

        ttk.Label(control, text="Calificación mínima:", font=("Helvetica", 9)).pack(anchor="w", pady=(5,0))
        self.calificacion_var = tk.DoubleVar(value=0.0)
        calif_frame = ttk.Frame(control)
        calif_frame.pack(fill="x", pady=2)
        ttk.Scale(calif_frame, variable=self.calificacion_var, from_=0, to=5, orient="horizontal", length=120).pack(side="left")
        self.calif_label = ttk.Label(calif_frame, text="0.0", width=4)
        self.calif_label.pack(side="right")
        self.calificacion_var.trace_add("write", lambda *a: self.update_calif_label())

        ttk.Label(control, text="Especialidad:", font=("Helvetica", 9)).pack(anchor="w", pady=(5,0))
        self.especialidad_search_var = tk.StringVar(value="Todas")
        especialidades = set()
        for h in HOSPITALES:
            for esp in h.especialidades:
                especialidades.add(esp.nombre)
        especialidades.add("Todas")
        combo_esp = ttk.Combobox(control, textvariable=self.especialidad_search_var, values=sorted(list(especialidades)), state="readonly")
        combo_esp.pack(fill="x", pady=2)
        combo_esp.bind("<<ComboboxSelected>>", lambda e: self.filtrar_hospitales())

        ttk.Separator(control, orient="horizontal").pack(fill="x", pady=6)
        ttk.Label(control, text="Hospitales:", font=("Helvetica", 10, "bold")).pack(anchor="w")

        self.hospital_listbox = tk.Listbox(control, width=35, height=8)
        self.hospital_listbox.pack(pady=4)
        self.hospital_listbox.bind("<<ListboxSelect>>", self.on_hospital_select)

        ttk.Button(control, text="Seleccionar hospital", command=self.select_hospital_button).pack(pady=6)
        ttk.Button(control, text="Reservar cita (siguiente)", command=self.goto_booking_if_selected).pack(pady=6)

        self.canvas_markers = {}
        self.render_map_markers()
        self.render_hospital_list()

    def logout(self):
        self.current_user = None
        self.face_verified = False
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
        filtered = [h for h in HOSPITALES if af == "Todos" or af == h.afiliacion]
        if idx < len(filtered):
            h = filtered[idx]
            self.highlight_hospital(h)
            # Mostrar información detallada del hospital
            self.update_hospital_info(h)

    def update_calif_label(self):
        """Actualizar la etiqueta que muestra la calificación seleccionada"""
        self.calif_label.config(text=f"{self.calificacion_var.get():.1f}")

    def filtrar_hospitales(self):
        """Filtrar hospitales según los criterios seleccionados"""
        self.render_hospital_list()

    def render_hospital_list(self):
        """Actualizar la lista de hospitales según filtros"""
        af = self.afiliacion_var.get()
        calif_min = self.calificacion_var.get()
        especialidad = self.especialidad_search_var.get()
        texto_busqueda = self.search_var.get().lower()

        self.hospital_listbox.delete(0, tk.END)

        for h in HOSPITALES:
            # Aplicar filtros
            if af != "Todos" and h.afiliacion != af:
                continue
            if h.calificacion < calif_min:
                continue
            if especialidad != "Todas":
                # Verificar si el hospital tiene la especialidad buscada
                if not any(esp.nombre == especialidad for esp in h.especialidades):
                    continue
            # Filtro de texto
            if texto_busqueda and texto_busqueda not in h.nombre.lower():
                continue

            # Formatear entrada con calificación
            calificacion_display = f"({'⭐' * int(h.calificacion)} {h.calificacion:.1f})" if h.calificacion > 0 else "(Sin calificación)"
            display = f"{h.nombre} - {h.afiliacion} {calificacion_display}"
            self.hospital_listbox.insert(tk.END, display)

    def update_hospital_info(self, hospital):
        """Actualizar la información del hospital seleccionado"""
        # Obtener horario actual
        dia_actual = calendar.day_name[datetime.today().weekday()].lower()
        horario = hospital.horario.get(dia_actual, ["cerrado", "cerrado"])
        horario_text = f"Horario: {horario[0]} - {horario[1]}" if horario[0] != "cerrado" else "Cerrado hoy"

        # Obtener especialidades
        especialidades = ", ".join([esp.nombre for esp in hospital.especialidades])

        info_text = f"{hospital.nombre}\n{hospital.afiliacion} | {horario_text}\nEspecialidades: {especialidades}\nCalificación: {'⭐' * int(hospital.calificacion)} ({hospital.calificacion}/5.0)"
        self.info_label.config(text=info_text)

    def select_hospital_by_id(self, hid):
        for i,h in enumerate(HOSPITALES):
            if h.id == hid:
                self.highlight_hospital(h)
                # Encontrar el índice en la lista filtrada actual
                af = self.afiliacion_var.get()
                calif_min = self.calificacion_var.get()
                especialidad = self.especialidad_search_var.get()
                texto_busqueda = self.search_var.get().lower()

                # Recrear la lista de hospitales filtrados para encontrar el índice
                filtered = []
                for hh in HOSPITALES:
                    # Aplicar los mismos filtros que render_hospital_list
                    if af != "Todos" and hh.afiliacion != af:
                        continue
                    if hh.calificacion < calif_min:
                        continue
                    if especialidad != "Todas":
                        if not any(esp.nombre == especialidad for esp in hh.especialidades):
                            continue
                    if texto_busqueda and texto_busqueda not in hh.nombre.lower():
                        continue
                    filtered.append(hh)

                try:
                    idx = filtered.index(h)
                    # Actualizar la selección en la lista
                    self.hospital_listbox.selection_clear(0, tk.END)
                    self.hospital_listbox.selection_set(idx)
                    # Actualizar información del hospital
                    self.update_hospital_info(h)
                except ValueError:
                    # En caso de error, simplemente mostrar la información del hospital
                    self.update_hospital_info(h)
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

        # Aplicar los mismos filtros usados en render_hospital_list
        af = self.afiliacion_var.get()
        calif_min = self.calificacion_var.get()
        especialidad = self.especialidad_search_var.get()
        texto_busqueda = self.search_var.get().lower()

        filtered = []
        for h in HOSPITALES:
            # Aplicar los mismos filtros que render_hospital_list
            if af != "Todos" and h.afiliacion != af:
                continue
            if h.calificacion < calif_min:
                continue
            if especialidad != "Todas":
                if not any(esp.nombre == especialidad for esp in h.especialidades):
                    continue
            if texto_busqueda and texto_busqueda not in h.nombre.lower():
                continue
            filtered.append(h)

        if idx < len(filtered):
            self.selected_hospital = filtered[idx]
            self.highlight_hospital(self.selected_hospital)
            # Actualizar información del hospital
            self.update_hospital_info(self.selected_hospital)

    def goto_booking_if_selected(self):
        if not self.selected_hospital:
            messagebox.showwarning("Selecciona", "Selecciona un hospital primero.")
            return
        self.show_booking_screen(self.selected_hospital)

    # ----------------------------
    # PANTALLA DE RESERVA MEJORADA
    # ----------------------------
    def show_booking_screen(self, hospital):
        self.hide_all_frames()
        self.face_verified = False
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
        # Mostrar horario actual
        fecha_actual = self.date_combo.get() if hasattr(self, 'date_combo') and self.date_combo.get() else datetime.today().strftime("%Y-%m-%d")
        dia_semana = calendar.day_name[datetime.strptime(fecha_actual, "%Y-%m-%d").weekday()].lower()
        horario_dia = hospital.horario.get(dia_semana, ["cerrado", "cerrado"])
        horario_text = f"Horario: {horario_dia[0]} - {horario_dia[1]}" if horario_dia[0] != "cerrado" else "Cerrado"
        self.horario_label = ttk.Label(left, text=horario_text)
        self.horario_label.pack(anchor="w", pady=2)

        estado_texto = "Verificación facial pendiente" if CV2_AVAILABLE else "Verificación facial opcional (instala opencv-python)"
        estado_color = "red" if CV2_AVAILABLE else "orange"
        self.face_status_label = ttk.Label(left, text=estado_texto, foreground=estado_color)
        self.face_status_label.pack(anchor="w", pady=2)
        ttk.Button(left, text="Verificar identidad (webcam)", command=self.verificar_identidad).pack(anchor="w", pady=4)

        # Mostrar calificación del hospital
        ttk.Label(left, text=f"Calificación: {'⭐' * int(hospital.calificacion)} ({hospital.calificacion}/5.0)", foreground="orange").pack(anchor="w", pady=2)

        ttk.Label(left, text="Especialidades disponibles:").pack(anchor="w", pady=(8,2))

        self.especialidad_var = tk.StringVar()
        for esp in hospital.especialidades:
            ttk.Radiobutton(left, text=esp.nombre, variable=self.especialidad_var, value=esp.nombre).pack(anchor="w")

        # Mostrar médicos disponibles para la especialidad seleccionada
        ttk.Label(left, text="Médicos disponibles:").pack(anchor="w", pady=(8,2))
        self.medico_var = tk.StringVar()
        self.medico_listbox = tk.Listbox(left, width=30, height=6)
        self.medico_listbox.pack(pady=4)
        self.medico_listbox.bind("<<ListboxSelect>>", self.on_medico_select)

        # Botón para calificar hospital
        ttk.Button(left, text="Calificar hospital", command=lambda: self.abrir_calificacion_hospital(hospital)).pack(pady=6)

        # Sección de seguros y pagos
        ttk.Label(left, text="Seguro médico:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(8,2))
        self.seguro_var = tk.StringVar()

        # Mostrar los seguros disponibles
        seguros = build_seguros()
        for seguro in seguros:
            rb = ttk.Radiobutton(left, text=f"{seguro.nombre} - S/.{seguro.costo_cita}",
                                variable=self.seguro_var, value=seguro.nombre)
            rb.pack(anchor="w")

        # Costo estimado de la cita
        ttk.Label(left, text="Costo estimado:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(8,2))
        self.costo_label = ttk.Label(left, text="S/.0.00", font=("Helvetica", 12, "bold"), foreground="green")
        self.costo_label.pack(anchor="w")

        center = ttk.Frame(body)
        center.pack(side="left", fill="y")
        ttk.Label(center, text="Elige fecha:").pack(anchor="w")
        dates = self.next_seven_days()
        self.date_combo = ttk.Combobox(center, values=dates, state="readonly")
        self.date_combo.pack(pady=6)
        self.date_combo.set(dates[0])  # Establecer el primer valor en lugar de usar current(0)


        # Actualizar horas disponibles cuando se cambie la fecha
        self.date_combo.bind("<<ComboboxSelected>>", lambda e: self.update_time_options(hospital))

        ttk.Label(center, text="Elige hora:").pack(anchor="w")
        # Inicializar con horas del día actual, considerando médico si está seleccionado
        # Usamos la fecha actual del combobox que ya debe estar inicializado
        selected_date = self.date_combo.get()  # Esta debe ser la fecha seleccionada actualmente
        if not selected_date:  # Si aún no hay fecha seleccionada, usar la de hoy
            selected_date = datetime.today().strftime("%Y-%m-%d")
            self.date_combo.set(selected_date)  # Establecer la fecha de hoy como predeterminada

        especialidad_actual = self.especialidad_var.get() if hasattr(self, 'especialidad_var') and self.especialidad_var.get() else None
        doctor_actual = getattr(self, 'medico_seleccionado', None) if hasattr(self, 'medico_seleccionado') else None
        available_times = self.get_available_hours_for_doctor(hospital, especialidad_actual, selected_date, doctor_actual)
        self.hora_combo = ttk.Combobox(center, values=available_times, state="readonly")
        self.hora_combo.pack(pady=6)
        if available_times:
            self.hora_combo.set(available_times[0])
            self.hora_combo.config(state="readonly")
        else:
            self.hora_combo.set("No hay horarios disponibles")
            self.hora_combo.config(state="disabled")

        ttk.Button(center, text="Reservar cita", command=lambda: self.confirm_booking(hospital)).pack(pady=12)

        # Botón para cancelar cita existente
        ttk.Button(center, text="Cancelar cita", command=lambda: self.cancelar_cita(hospital)).pack(pady=6)

        right = ttk.Frame(body)
        right.pack(side="left", fill="y", padx=(20,0))
        ttk.Label(right, text="Resumen:").pack(anchor="w")
        self.resumen_text = tk.Text(right, width=35, height=12, state="disabled")
        self.resumen_text.pack()

        self.especialidad_var.trace_add("write", lambda *a: [self.update_medicos_disponibles(hospital), self.calcular_costo_cita(hospital), self.update_info_horario(hospital)])
        self.date_combo.bind("<<ComboboxSelected>>", lambda e: [self.update_time_options(hospital), self.update_resumen(hospital), self.calcular_costo_cita(hospital), self.update_info_horario(hospital)])
        self.hora_combo.bind("<<ComboboxSelected>>", lambda e: self.update_resumen(hospital))
        self.seguro_var.trace_add("write", lambda *a: self.calcular_costo_cita(hospital))
        self.update_resumen(hospital)
        self.calcular_costo_cita(hospital)  # Calcular costo inicial
        self.update_info_horario(hospital)  # Actualizar información de horario

    def update_info_horario(self, hospital):
        """Actualizar la información de horario según la fecha seleccionada"""
        # Obtener la fecha actual del combobox
        fecha_actual = self.date_combo.get() if hasattr(self, 'date_combo') and self.date_combo.get() else datetime.today().strftime("%Y-%m-%d")
        dia_semana = calendar.day_name[datetime.strptime(fecha_actual, "%Y-%m-%d").weekday()].lower()
        horario_dia = hospital.horario.get(dia_semana, ["cerrado", "cerrado"])
        horario_text = f"Horario: {horario_dia[0]} - {horario_dia[1]}" if horario_dia[0] != "cerrado" else "Cerrado"

        # Actualizar la etiqueta de horario
        self.horario_label.config(text=horario_text)

    def calcular_costo_cita(self, hospital):
        """Calcular el costo estimado de la cita basado en seguro y especialidad"""
        especialidad_nombre = self.especialidad_var.get()
        seguro_nombre = self.seguro_var.get()

        # Buscar la especialidad para obtener su costo base
        costo_base = 0
        for esp in hospital.especialidades:
            if esp.nombre == especialidad_nombre:
                costo_base = esp.costo_base
                break

        # Buscar el seguro para obtener su costo adicional
        costo_seguro = 0
        seguros = build_seguros()
        for seguro in seguros:
            if seguro.nombre == seguro_nombre:
                costo_seguro = seguro.costo_cita
                break

        # Calcular costo total
        costo_total = costo_base + costo_seguro

        # Actualizar la etiqueta de costo
        self.costo_label.config(text=f"S/.{costo_total:.2f}")

    def update_medicos_disponibles(self, hospital):
        """Actualizar la lista de médicos disponibles según la especialidad seleccionada"""
        especialidad_seleccionada = self.especialidad_var.get()
        self.medico_listbox.delete(0, tk.END)

        if especialidad_seleccionada:
            # Filtrar médicos por especialidad
            medicos_especialidad = [med for med in hospital.medicos if med.especialidad == especialidad_seleccionada]

            for medico in medicos_especialidad:
                # Mostrar también la calificación del médico
                calificacion_str = f" ({'⭐' * int(medico.calificacion)} {medico.calificacion}/5.0)" if medico.calificacion > 0 else ""
                self.medico_listbox.insert(tk.END, f"{medico.nombre}{calificacion_str}")

    def on_medico_select(self, evt):
        """Manejar la selección de un médico"""
        sel = evt.widget.curselection()
        if not sel:
            return
        idx = sel[0]
        especialidad_seleccionada = self.especialidad_var.get()

        if especialidad_seleccionada:
            # Obtener el médico correspondiente a la selección
            medicos_especialidad = [med for med in self.selected_hospital.medicos if med.especialidad == especialidad_seleccionada]
            if idx < len(medicos_especialidad):
                self.medico_seleccionado = medicos_especialidad[idx]
                # Actualizar las horas disponibles según el horario del médico
                date_str = self.date_combo.get()
                if not date_str:
                    date_str = datetime.today().strftime("%Y-%m-%d")

                available_times = self.get_available_hours_for_doctor(self.selected_hospital, especialidad_seleccionada, date_str, self.medico_seleccionado)
                self.hora_combo['values'] = available_times
                self.hora_combo.config(state="readonly")

                # Si hay horarios disponibles, seleccionar el primero
                if available_times:
                    self.hora_combo.set(available_times[0])
                    self.hora_combo.config(state="readonly")
                else:
                    self.hora_combo.set("No hay horarios disponibles")
                    self.hora_combo.config(state="disabled")

    def abrir_calificacion_hospital(self, hospital):
        """Abrir ventana para calificar el hospital"""
        def guardar_calificacion():
            try:
                nueva_calificacion = float(calificacion_var.get())
                if 0 <= nueva_calificacion <= 5:
                    # Actualizar calificación del hospital
                    hospital.calificacion = (hospital.calificacion + nueva_calificacion) / 2 if hospital.calificacion > 0 else nueva_calificacion
                    messagebox.showinfo("Éxito", f"¡Gracias por calificar {hospital.nombre}!")
                    calif_window.destroy()
                else:
                    messagebox.showerror("Error", "La calificación debe estar entre 0 y 5")
            except ValueError:
                messagebox.showerror("Error", "Ingresa un número válido")

        calif_window = tk.Toplevel(self.root)
        calif_window.title(f"Calificar {hospital.nombre}")
        calif_window.geometry("300x150")
        calif_window.resizable(False, False)

        ttk.Label(calif_window, text=f"Calificar {hospital.nombre}:").pack(pady=10)

        # Escala de calificación
        calificacion_var = tk.StringVar(value="5")
        ttk.Label(calif_window, text="Tu calificación (0-5):").pack()

        combo = ttk.Combobox(calif_window, textvariable=calificacion_var, values=["0", "1", "2", "3", "4", "5"], state="readonly", width=5)
        combo.pack(pady=5)

        ttk.Button(calif_window, text="Guardar Calificación", command=guardar_calificacion).pack(pady=10)

    def update_time_options(self, hospital):
        """Actualizar las opciones de tiempo cuando se selecciona una nueva fecha"""
        selected_date = self.date_combo.get()
        especialidad_seleccionada = self.especialidad_var.get()

        # Si hay un médico seleccionado, usar su horario, de lo contrario usar el del hospital
        doctor_seleccionado = getattr(self, 'medico_seleccionado', None) if hasattr(self, 'medico_seleccionado') else None

        available_times = self.get_available_hours_for_doctor(hospital, especialidad_seleccionada, selected_date, doctor_seleccionado)

        self.hora_combo['values'] = available_times
        self.hora_combo.config(state="readonly")  # Asegurar que esté en modo readonly

        # Si hay horarios disponibles, seleccionar el primero
        if available_times:
            self.hora_combo.set(available_times[0])
            self.hora_combo.config(state="readonly")
        else:
            self.hora_combo.set("No hay horarios disponibles")
            self.hora_combo.config(state="disabled")

    def cancelar_cita(self, hospital):
        """Función para cancelar la cita actual si existe"""
        # Mostrar un mensaje de confirmación
        if messagebox.askyesno("Cancelar Cita", f"¿Estás seguro de que deseas cancelar la cita en {hospital.nombre}?"):
            # Simular cancelación de cita
            messagebox.showinfo("Cita Cancelada", "La cita ha sido cancelada exitosamente.")
            # Regresar a la pantalla principal
            self.back_to_map()

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

    def dia_semana_ingles_a_espanol(self, dia_ingles):
        """Convierte un día en inglés a su equivalente en español (mantiene compatibilidad)"""
        dias_traduccion = {
            "monday": "lunes",
            "tuesday": "martes",
            "wednesday": "miercoles",
            "thursday": "jueves",
            "friday": "viernes",
            "saturday": "sabado",
            "sunday": "domingo"
        }
        return dias_traduccion.get(dia_ingles.lower(), dia_ingles.lower())

    def possible_hours(self, hospital=None, date_str=None):
        """Obtiene horas posibles según el horario del hospital y la fecha"""
        if hospital and date_str:
            # Obtener el día de la semana en inglés (que es como lo devuelve calendar.day_name)
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            day_of_week = calendar.day_name[date_obj.weekday()].lower()

            # Obtener horario del hospital para ese día
            horario = hospital.horario.get(day_of_week, ["cerrado", "cerrado"])

            if horario[0] == "cerrado":
                return []  # Hospital cerrado

            # Convertir horarios a minutos desde medianoche
            try:
                open_time = int(horario[0][:2]) * 60 + int(horario[0][3:])
                close_time = int(horario[1][:2]) * 60 + int(horario[1][3:])
            except (ValueError, IndexError):
                return []  # Error en el formato de horario

            # Generar horas disponibles en intervalos de 30 minutos
            hours = []
            current_time = open_time
            while current_time < close_time:
                hour = current_time // 60
                minute = current_time % 60
                hours.append(f"{hour:02d}:{minute:02d}")
                current_time += 30  # intervalo de 30 minutos
        else:
            # Horario por defecto
            hours = ["08:00", "08:30", "09:00", "09:30", "10:00", "10:30",
                     "11:00", "11:30", "14:00", "14:30", "15:00", "15:30"]

        return hours

    def get_available_hours_for_doctor(self, hospital, especialidad, date_str, doctor):
        """Obtiene horas disponibles considerando también el horario del médico"""
        # Obtener el día de la semana
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        day_of_week = calendar.day_name[date_obj.weekday()].lower()

        # Obtener horario del hospital para ese día
        horario_hospital = hospital.horario.get(day_of_week, ["cerrado", "cerrado"])

        # Verificar si el hospital está cerrado
        if horario_hospital[0] == "cerrado":
            return []  # Hospital cerrado

        # Obtener horas disponibles del hospital
        horas_hospital = self.possible_hours(hospital, date_str)

        # Si no hay médico seleccionado o la especialidad no coincide, usar solo horario del hospital
        if not doctor or especialidad != doctor.especialidad:
            return horas_hospital

        # Obtener horario del médico para ese día
        horario_medico = doctor.horario_atencion.get(day_of_week, ["cerrado", "cerrado"])

        if horario_medico[0] == "cerrado":
            # Si el médico está cerrado pero el hospital está abierto, devolver las horas del hospital
            return horas_hospital

        # Convertir horarios del médico a minutos (en formato HH:MM)
        try:
            open_time = int(horario_medico[0][:2]) * 60 + int(horario_medico[0][3:])
            close_time = int(horario_medico[1][:2]) * 60 + int(horario_medico[1][3:])
        except (ValueError, IndexError):
            # Si hay error en el formato del horario del médico, devolver las horas del hospital
            return horas_hospital

        # Generar horas disponibles del médico
        horas_medico = []
        current_time = open_time
        while current_time < close_time:
            hour = current_time // 60
            minute = current_time % 60
            horas_medico.append(f"{hour:02d}:{minute:02d}")
            current_time += 30  # intervalo de 30 minutos

        # Intersección de horas disponibles (hospital y médico) - convertir a set para intersección
        horas_comunes = list(set(horas_hospital) & set(horas_medico))

        # Si no hay intersección de horarios, usar las horas del hospital como fallback
        if not horas_comunes:
            return horas_hospital

        return sorted(horas_comunes)

    def update_resumen(self, hospital):
        esp = self.especialidad_var.get() or "(no seleccionado)"
        fecha = self.date_combo.get()
        hora = self.hora_combo.get()
        medico_nombre = getattr(self, 'medico_seleccionado', None)
        medico_nombre = medico_nombre.nombre if medico_nombre else "(no asignado)"
        seguro_nombre = self.seguro_var.get() or "(no seleccionado)"

        # Calcular costo
        costo_cita = 0.0
        for esp_obj in hospital.especialidades:
            if esp_obj.nombre == esp:
                costo_cita += float(esp_obj.costo_base)
                break

        seguros = build_seguros()
        for seguro in seguros:
            if seguro.nombre == seguro_nombre:
                costo_cita += float(seguro.costo_cita)
                break

        texto = f"Hospital: {str(hospital.nombre)}\nAfiliación: {str(hospital.afiliacion)}\nEspecialidad: {str(esp)}\nMédico: {str(medico_nombre)}\nFecha: {str(fecha)}\nHora: {str(hora)}\nSeguro: {str(seguro_nombre)}\nCosto estimado: S/.{float(costo_cita):.2f}\nUsuario: {str(self.current_user.nombre)}\n"
        self.resumen_text.config(state="normal")
        self.resumen_text.delete("1.0", tk.END)
        self.resumen_text.insert(tk.END, texto)
        self.resumen_text.config(state="disabled")

    def verificar_identidad(self):
        """Verificación facial simple utilizando la webcam y Haar cascades de OpenCV."""
        if not self.current_user:
            messagebox.showwarning("No autenticado", "Inicia sesión antes de verificar tu identidad.")
            return

        if not CV2_AVAILABLE:
            messagebox.showinfo(
                "Verificación facial opcional",
                "La librería opencv-python no está instalada. El flujo seguirá sin biometría.",
            )
            self.face_verified = True
            if hasattr(self, "face_status_label"):
                self.face_status_label.config(text="Verificación omitida (sin OpenCV)", foreground="orange")
            return

        cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(cascade_path)

        if detector.empty():
            messagebox.showerror(
                "Falta el modelo de rostros",
                "No se encontró el archivo haarcascade_frontalface_default.xml en tu instalación de OpenCV.",
            )
            return

        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            messagebox.showerror("Cámara no disponible", "No pudimos abrir la cámara web. Verifica permisos y drivers.")
            return

        detectado = False
        frames_leidos = 0
        while frames_leidos < 90:  # ~3 segundos a 30fps
            ret, frame = cam.read()
            if not ret:
                frames_leidos += 1
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
            if len(faces) > 0:
                detectado = True
                break
            frames_leidos += 1

        cam.release()

        if detectado:
            self.face_verified = True
            if hasattr(self, "face_status_label"):
                self.face_status_label.config(text="Verificado ✅ (rostro detectado)", foreground="green")
            messagebox.showinfo("Verificación exitosa", "Detectamos un rostro y habilitamos la reserva.")
        else:
            self.face_verified = False
            if hasattr(self, "face_status_label"):
                self.face_status_label.config(text="No se detectó rostro", foreground="red")
            messagebox.showwarning(
                "Rostro no detectado",
                "No se detectó ningún rostro. Asegúrate de tener buena iluminación y la cámara habilitada.",
            )

    def confirm_booking(self, hospital):
        esp = self.especialidad_var.get()
        if not esp:
            messagebox.showwarning("Elige especialidad", "Selecciona una especialidad.")
            return

        fecha = self.date_combo.get()
        hora = self.hora_combo.get()

        # Verificar que la hora no sea un mensaje de "No hay horarios disponibles"
        if hora == "No hay horarios disponibles" or self.hora_combo['state'] == 'disabled':
            messagebox.showerror("Sin horarios", "No hay horarios disponibles para la fecha seleccionada.")
            return

        # Verificar que la fecha y hora estén dentro del horario del hospital
        date_obj = datetime.strptime(fecha, "%Y-%m-%d")
        day_of_week = calendar.day_name[date_obj.weekday()].lower()
        horario_dia = hospital.horario.get(day_of_week, ["cerrado", "cerrado"])

        if horario_dia[0] == "cerrado":
            messagebox.showerror("Cerrado", f"El hospital está cerrado el día {day_of_week}.")
            return

        if CV2_AVAILABLE and not self.face_verified:
            messagebox.showwarning(
                "Verificación facial requerida",
                "Activa la cámara y presiona 'Verificar identidad' antes de confirmar la cita.",
            )
            return

        # Obtener el médico seleccionado si existe
        medico_nombre = ""
        if hasattr(self, 'medico_seleccionado') and self.medico_seleccionado:
            medico_nombre = self.medico_seleccionado.nombre

        # Obtener la información del seguro
        seguro_nombre = self.seguro_var.get() or "Sin seguro"

        # Calcular el costo de la cita
        costo_cita = 0.0  # Initialize as float
        for esp_obj in hospital.especialidades:
            if esp_obj.nombre == esp:
                costo_cita += float(esp_obj.costo_base)
                break

        seguros = build_seguros()
        for seguro in seguros:
            if seguro.nombre == seguro_nombre:
                costo_cita += float(seguro.costo_cita)
                break

        # Crear la cita con el médico y seguro asignados
        cita = Cita(self.current_user.dni, hospital.id, hospital.nombre, esp, fecha, hora, medico=medico_nombre)
        cita.seguro = seguro_nombre  # Añadir el seguro a la cita
        cita.costo = float(costo_cita) if costo_cita is not None else 0.0  # Añadir el costo a la cita as float

        self.current_user.agregar_cita(cita)
        self.users[self.current_user.dni] = self.current_user
        save_users(self.users)

        # Mensaje de confirmación
        mensaje_confirmacion = f"Cita reservada en {str(hospital.nombre)}\n{str(fecha)} - {str(hora)}\nEspecialidad: {str(esp)}\nMédico: {str(medico_nombre) if medico_nombre else 'No asignado'}\nSeguro: {str(seguro_nombre)}\nCosto: S/.{float(costo_cita):.2f}"
        messagebox.showinfo("Reservado", mensaje_confirmacion)

        # Imprimir ticket de la cita
        self.imprimir_ticket(cita, hospital)
        self.show_main_screen()

    def imprimir_ticket(self, cita, hospital):
        """Generar e imprimir el ticket de la cita"""
        # Siempre mostrar ticket en pantalla, y opcionalmente guardar como PDF si reportlab está funcionando
        try:
            # Asegurar que todos los valores sean cadenas antes de formatear
            hospital_nombre = str(getattr(hospital, 'nombre', 'Desconocido'))
            paciente_nombre = str(getattr(self.current_user, 'nombre', 'Desconocido'))
            paciente_dni = str(getattr(self.current_user, 'dni', 'Desconocido'))
            especialidad = str(getattr(cita, 'especialidad', 'Desconocida'))
            fecha = str(getattr(cita, 'fecha', 'Desconocida'))
            hora = str(getattr(cita, 'hora', 'Desconocida'))
            medico = str(getattr(cita, 'medico', 'No asignado'))
            seguro = str(getattr(cita, 'seguro', 'No asignado'))
            costo = getattr(cita, 'costo', 0)
            costo_float = float(costo) if costo is not None and costo != '' else 0.0
            estado = str(getattr(cita, 'estado', 'Desconocido'))

            ticket_info = f"""
TICKET DE CITA MÉDICA
====================
Hospital: {hospital_nombre}
Paciente: {paciente_nombre}
DNI: {paciente_dni}
Especialidad: {especialidad}
Fecha: {fecha}
Hora: {hora}
Médico: {medico}
Seguro: {seguro}
Costo: S/.{costo_float:.2f}
ID de Cita: {len(self.current_user.historial)}-{fecha.replace('-', '')}
Estado: {estado}
====================
Gracias por usar SaludTurno
            """
            # Mostrar ticket en una ventana emergente
            ticket_window = tk.Toplevel(self.root)
            ticket_window.title("Ticket de Cita")
            ticket_window.geometry("400x400")
            ticket_window.resizable(False, False)

            frame = ttk.Frame(ticket_window, padding=10)
            frame.pack(fill="both", expand=True)

            text_widget = tk.Text(frame, wrap=tk.WORD, font=("Courier", 10))
            text_widget.pack(side="left", fill="both", expand=True)

            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text_widget.yview)
            scrollbar.pack(side="right", fill="y")

            text_widget.config(yscrollcommand=scrollbar.set)
            text_widget.insert(tk.END, ticket_info.strip())
            text_widget.config(state="disabled")

            # Botón para guardar ticket
            ttk.Button(ticket_window, text="Guardar Ticket",
                      command=lambda: self.guardar_ticket_txt(ticket_info, cita)).pack(pady=10)

            if PDF_AVAILABLE:
                try:
                    pdf_filename = f"ticket_cita_{paciente_dni}_{fecha.replace('-', '')}_{hora.replace(':', '')}.pdf"
                    c = canvas.Canvas(pdf_filename, pagesize=A4)
                    text_object = c.beginText(1 * inch, A4[1] - 1 * inch)
                    for line in ticket_info.strip().splitlines():
                        text_object.textLine(line)
                    c.drawText(text_object)
                    c.showPage()
                    c.save()
                    messagebox.showinfo("PDF generado", f"Ticket guardado como {pdf_filename}")
                except Exception as e:
                    messagebox.showwarning(
                        "PDF no generado",
                        f"El ticket se mostró en pantalla, pero no pudimos crear el PDF:\n{str(e)}",
                    )
            else:
                messagebox.showinfo(
                    "PDF opcional",
                    "Instala reportlab (pip install reportlab) para exportar el ticket directamente a PDF.",
                )

            return
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al generar el ticket:\n{str(e)}")

    def imprimir_ultimo_ticket(self, parent_window):
        """Imprimir el ticket de la última cita"""
        if not self.current_user.historial:
            messagebox.showwarning("Sin citas", "No tienes citas registradas.")
            return

        # Tomar la última cita
        ultima_cita = self.current_user.historial[-1]

        # Buscar el hospital correspondiente
        hospital = None
        for h in HOSPITALES:
            if h.id == ultima_cita.hospital_id or h.nombre == ultima_cita.hospital_nombre:
                hospital = h
                break

        if hospital:
            # Crear una copia del hospital con la información del histórico
            self.imprimir_ticket(ultima_cita, hospital)
        else:
            # Si no encontramos el hospital exacto, creamos uno genérico
            hospital_generico = Hospital(ultima_cita.hospital_id, ultima_cita.hospital_nombre, 0, 0, "Desconocido", [])
            self.imprimir_ticket(ultima_cita, hospital_generico)

    def imprimir_todos_los_tickets(self, parent_window):
        """Imprimir tickets de todas las citas"""
        if not self.current_user.historial:
            messagebox.showwarning("Sin citas", "No tienes citas registradas.")
            return

        for cita in self.current_user.historial:
            # Buscar el hospital correspondiente
            hospital = None
            for h in HOSPITALES:
                if h.id == cita.hospital_id or h.nombre == cita.hospital_nombre:
                    hospital = h
                    break

            if hospital:
                self.imprimir_ticket(cita, hospital)
            else:
                # Si no encontramos el hospital exacto, creamos uno genérico
                hospital_generico = Hospital(cita.hospital_id, cita.hospital_nombre, 0, 0, "Desconocido", [])
                self.imprimir_ticket(cita, hospital_generico)

        messagebox.showinfo("Tickets generados", f"Se han generado {len(self.current_user.historial)} tickets.")

    def guardar_ticket_txt(self, ticket_info, cita):
        """Guardar ticket como archivo de texto"""
        filename = f"ticket_cita_{str(cita.paciente_dni)}_{str(cita.fecha).replace('-', '')}_{str(cita.hora).replace(':', '')}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(str(ticket_info).strip())
            messagebox.showinfo("Ticket Guardado", f"El ticket ha sido guardado como:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al guardar el ticket:\n{str(e)}")

    def show_historial(self):
        if not self.current_user:
            messagebox.showwarning("No autenticado", "Inicia sesión para ver historial.")
            return
        hist = self.current_user.historial
        if not hist:
            mensaje = "No tienes citas reservadas."
        else:
            mensaje = "Tus citas reservadas:\n\n"
            for i, c in enumerate(hist):
                estado_badge = "🟢" if c.estado == "Reservada" else "✅" if c.estado == "Atendida" else "❌" if c.estado == "Cancelada" else "⏳"
                mensaje += f"{estado_badge} {c.fecha} {c.hora}\n  {c.hospital_nombre}\n  {c.especialidad}\n  Estado: {c.estado}\n"
                if c.medico:
                    mensaje += f"  Médico: {c.medico}\n"
                if hasattr(c, 'seguro') and c.seguro:
                    mensaje += f"  Seguro: {c.seguro}\n"
                if hasattr(c, 'costo') and c.costo is not None:
                    try:
                        costo_valor = float(c.costo) if c.costo is not None and c.costo != '' else 0.0
                        if costo_valor > 0:
                            mensaje += f"  Costo: S/.{costo_valor:.2f}\n"
                    except (ValueError, TypeError):
                        # Si hay un error al convertir a float, simplemente omitir esta línea
                        pass
                mensaje += "-" * 30 + "\n"

        # Crear ventana personalizada para mostrar el historial
        historial_window = tk.Toplevel(self.root)
        historial_window.title("Historial de Citas")
        historial_window.geometry("600x500")
        historial_window.resizable(False, False)

        frame = ttk.Frame(historial_window, padding=10)
        frame.pack(fill="both", expand=True)

        # Texto con historial
        text_frame = ttk.Frame(frame)
        text_frame.pack(fill="both", expand=True, pady=(0, 10))

        text_widget = tk.Text(text_frame, wrap=tk.WORD)
        text_widget.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")

        text_widget.config(yscrollcommand=scrollbar.set)
        text_widget.insert(tk.END, mensaje)
        text_widget.config(state="disabled")

        # Botones en la parte inferior
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill="x")

        # Botón para imprimir ticket de la última cita
        if self.current_user.historial:
            ttk.Button(button_frame, text="Imprimir último ticket",
                      command=lambda: self.imprimir_ultimo_ticket(historial_window)).pack(side="left", padx=5)

            # Botón para imprimir todos los tickets
            ttk.Button(button_frame, text="Imprimir todos los tickets",
                      command=lambda: self.imprimir_todos_los_tickets(historial_window)).pack(side="left", padx=5)
        else:
            ttk.Label(button_frame, text="No hay citas para imprimir", foreground="gray").pack(side="left", padx=5)

        # Botón para cerrar
        ttk.Button(button_frame, text="Cerrar",
                  command=historial_window.destroy).pack(side="right", padx=5)

# ----------------------------
# Ejecutar app
# ----------------------------
def main():
    root = tk.Tk()
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except:
        pass
    app = SaludTurnoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()