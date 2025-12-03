"""Persistencia con SQLite para SaludTurno."""
import sqlite3
from pathlib import Path
from typing import Optional

from models import Paciente, Cita


class Database:
    def __init__(self, db_path: str | Path = "saludturno.db"):
        self.db_path = Path(db_path)

    def connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_schema(self) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    dni TEXT PRIMARY KEY,
                    correo TEXT UNIQUE NOT NULL,
                    nombre TEXT NOT NULL,
                    password_hash TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    paciente_dni TEXT NOT NULL,
                    hospital_id INTEGER NOT NULL,
                    hospital_nombre TEXT NOT NULL,
                    especialidad TEXT NOT NULL,
                    fecha TEXT NOT NULL,
                    hora TEXT NOT NULL,
                    estado TEXT NOT NULL,
                    FOREIGN KEY(paciente_dni) REFERENCES users(dni)
                )
                """
            )

    def get_user_by_identifier(self, identifier: str) -> Optional[Paciente]:
        query = "SELECT * FROM users WHERE dni = ? OR correo = ?"
        with self.connect() as conn:
            row = conn.execute(query, (identifier, identifier)).fetchone()
        if row:
            return self._row_to_paciente(row)
        return None

    def get_user_by_dni(self, dni: str) -> Optional[Paciente]:
        with self.connect() as conn:
            row = conn.execute("SELECT * FROM users WHERE dni = ?", (dni,)).fetchone()
        if row:
            return self._row_to_paciente(row)
        return None

    def get_user_by_correo(self, correo: str) -> Optional[Paciente]:
        with self.connect() as conn:
            row = conn.execute("SELECT * FROM users WHERE correo = ?", (correo,)).fetchone()
        if row:
            return self._row_to_paciente(row)
        return None

    def create_user(self, paciente: Paciente) -> None:
        with self.connect() as conn:
            conn.execute(
                "INSERT INTO users (dni, correo, nombre, password_hash) VALUES (?, ?, ?, ?)",
                (paciente.dni, paciente.correo, paciente.nombre, paciente.password_hash),
            )

    def add_appointment(self, cita: Cita) -> None:
        with self.connect() as conn:
            conn.execute(
                """
                INSERT INTO appointments (paciente_dni, hospital_id, hospital_nombre, especialidad, fecha, hora, estado)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    cita.paciente_dni,
                    cita.hospital_id,
                    cita.hospital_nombre,
                    cita.especialidad,
                    cita.fecha,
                    cita.hora,
                    cita.estado,
                ),
            )

    def list_appointments(self, paciente_dni: str) -> list[Cita]:
        with self.connect() as conn:
            rows = conn.execute(
                "SELECT * FROM appointments WHERE paciente_dni = ? ORDER BY fecha, hora",
                (paciente_dni,),
            ).fetchall()
        return [self._row_to_cita(r) for r in rows]

    def _row_to_paciente(self, row: sqlite3.Row) -> Paciente:
        p = Paciente(row["dni"], row["correo"], row["nombre"], row["password_hash"])
        p.historial = self.list_appointments(p.dni)
        return p

    @staticmethod
    def _row_to_cita(row: sqlite3.Row) -> Cita:
        return Cita(
            row["paciente_dni"],
            row["hospital_id"],
            row["hospital_nombre"],
            row["especialidad"],
            row["fecha"],
            row["hora"],
            row["estado"],
        )
