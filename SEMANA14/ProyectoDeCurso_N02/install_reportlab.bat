@echo off
echo Instalando reportlab para la funcionalidad de tickets PDF...
echo.

pip install reportlab

if %errorlevel% == 0 (
    echo.
    echo Reportlab instalado correctamente!
    echo Ahora podrás generar tickets en formato PDF.
) else (
    echo.
    echo Ocurrió un error al instalar reportlab.
    echo Asegúrate de tener pip instalado y acceso a internet.
)

echo.
pause