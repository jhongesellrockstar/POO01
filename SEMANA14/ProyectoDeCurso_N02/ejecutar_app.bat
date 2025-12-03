@echo off
echo Iniciando la aplicacion SaludTurno...
echo.

REM Verificar si Python esta instalado
python --version > nul 2>&1
if errorlevel 1 (
    echo Error: Python no esta instalado o no esta en el PATH.
    echo Por favor, instala Python y asegurate de que este en el PATH.
    pause
    exit /b 1
)

REM Ejecutar la aplicacion
python run_app.py

REM Pausar para ver cualquier mensaje de error
pause