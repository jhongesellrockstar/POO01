import hashlib
from typing import List


class Paciente:
    def __init__(self, dni: str, correo: str, nombre: str, password_hash: str):
        self.dni = dni
        self.correo = correo
        self.nombre = nombre
        self.password_hash = password_hash
        self.historial: List[Cita] = []  # type: ignore[name-defined]

    def agregar_cita(self, cita: "Cita") -> None:
        self.historial.append(cita)


class Medico:
    def __init__(self, nombre: str, especialidad: "Especialidad"):
        self.nombre = nombre
        self.especialidad = especialidad


class Especialidad:
    def __init__(self, nombre: str):
        self.nombre = nombre


class Hospital:
    def __init__(self, id: int, nombre: str, x: float, y: float, afiliacion: str, especialidades: List[Especialidad]):
        self.id = id
        self.nombre = nombre
        self.x = x
        self.y = y
        self.afiliacion = afiliacion
        self.especialidades = especialidades


class Cita:
    def __init__(
        self,
        paciente_dni: str,
        hospital_id: int,
        hospital_nombre: str,
        especialidad: str,
        fecha: str,
        hora: str,
        estado: str = "Reservada",
    ):
        self.paciente_dni = paciente_dni
        self.hospital_id = hospital_id
        self.hospital_nombre = hospital_nombre
        self.especialidad = especialidad
        self.fecha = fecha
        self.hora = hora
        self.estado = estado


def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()
