# SaludTurno (Proyecto de curso N02)

Aplicación de escritorio construida con Tkinter para reservar citas médicas simuladas. Permite que un paciente se registre o inicie sesión, elija un hospital y especialidad, verifique su identidad con la webcam (si tienes OpenCV instalado) y confirme una cita. El historial puede imprimirse como ticket en pantalla o guardarse como texto; opcionalmente se pueden generar tickets PDF si se instala `reportlab`.

## Requisitos rápidos
- Python 3 instalado.
- `pip install -r requirements.txt` para instalar dependencias de PDF (`reportlab`), verificación facial (`opencv-python`), imágenes (`Pillow`) y numéricas (`numpy`).

```bash
pip install -r requirements.txt
```

## Ejecución
Para iniciar la aplicación desde una terminal:

```bash
python run_app.py
```

En Windows también puedes usar `ejecutar_app.bat`.

### Instalación rápida en Anaconda (Windows)
Consulta el archivo `entorno_anaconda_windows.txt` para crear el entorno `UNAC_POO01`, activar el entorno y ejecutar la app desde el Anaconda Prompt.

## Datos de prueba
El archivo `users.json` incluye un usuario de ejemplo (DNI `72460711`) con un par de citas precargadas que sirven para probar el historial y la impresión de tickets.
