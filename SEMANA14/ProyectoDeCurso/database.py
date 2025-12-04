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
            try:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS users (
                        dni TEXT PRIMARY KEY,
                        correo TEXT UNIQUE NOT NULL,
                        nombre TEXT NOT NULL,
                        password_hash TEXT NOT NULL,
                        profile_image TEXT
                    )
                    """
                )
            except Exception:
                print("error")
            try:
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
            except Exception:
                print("error")
            self._ensure_profile_image_column(conn)

    def get_user_by_identifier(self, identifier: str) -> Optional[Paciente]:
        query = "SELECT * FROM users WHERE dni = ? OR correo = ?"
        try:
            with self.connect() as conn:
                row = conn.execute(query, (identifier, identifier)).fetchone()
            if row:
                return self._row_to_paciente(row)
            return None
        except Exception:
            print("error")
            return None

    def get_user_by_dni(self, dni: str) -> Optional[Paciente]:
        try:
            with self.connect() as conn:
                row = conn.execute("SELECT * FROM users WHERE dni = ?", (dni,)).fetchone()
            if row:
                return self._row_to_paciente(row)
        except Exception:
            print("error")
        return None

    def get_user_by_correo(self, correo: str) -> Optional[Paciente]:
        try:
            with self.connect() as conn:
                row = conn.execute("SELECT * FROM users WHERE correo = ?", (correo,)).fetchone()
            if row:
                return self._row_to_paciente(row)
        except Exception:
            print("error")
        return None

    def create_user(self, paciente: Paciente) -> None:
        try:
            with self.connect() as conn:
                conn.execute(
                    "INSERT INTO users (dni, correo, nombre, password_hash, profile_image) VALUES (?, ?, ?, ?, ?)",
                    (paciente.dni, paciente.correo, paciente.nombre, paciente.password_hash, paciente.profile_image),
                )
        except Exception:
            print("error")

    def add_appointment(self, cita: Cita) -> None:
        try:
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
        except Exception:
            print("error")

    def list_appointments(self, paciente_dni: str) -> list[Cita]:
        try:
            with self.connect() as conn:
                rows = conn.execute(
                    "SELECT * FROM appointments WHERE paciente_dni = ? ORDER BY fecha, hora",
                    (paciente_dni,),
                ).fetchall()
            return [self._row_to_cita(r) for r in rows]
        except Exception:
            print("error")
            return []

    def _row_to_paciente(self, row: sqlite3.Row) -> Paciente:
        profile_image = None
        try:
            if hasattr(row, "keys") and "profile_image" in row.keys():
                profile_image = row["profile_image"]
        except Exception:
            print("error")
        p = Paciente(row["dni"], row["correo"], row["nombre"], row["password_hash"], profile_image)
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

    def _ensure_profile_image_column(self, conn: sqlite3.Connection) -> None:
        try:
            info = conn.execute("PRAGMA table_info(users)").fetchall()
            cols = {row[1] for row in info}
            if "profile_image" not in cols:
                conn.execute("ALTER TABLE users ADD COLUMN profile_image TEXT")
        except Exception:
            print("error")

    def update_profile_image(self, dni: str, profile_path: str | None) -> None:
        try:
            with self.connect() as conn:
                conn.execute("UPDATE users SET profile_image = ? WHERE dni = ?", (profile_path, dni))
        except Exception:
            print("error")
