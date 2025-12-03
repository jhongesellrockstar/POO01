#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejecutador de la aplicación SaludTurno
Este script inicia la aplicación de gestión de citas médicas
"""

import sys
import os

# Asegurarse de que el directorio actual esté en el path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    try:
        # Importar y ejecutar la aplicación
        from main import main as app_main
        print("Iniciando la aplicación SaludTurno...")
        print("Cargando módulos...")
        app_main()
    except ImportError as e:
        print(f"Error al importar módulos: {e}")
        print("Asegúrate de que el archivo main.py esté en la misma carpeta.")
        input("Presiona Enter para salir...")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()