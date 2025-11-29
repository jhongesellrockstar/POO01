#Importaciones
from tkinter import *
import os

#Carga de directorios
#Carpeta Principal
carpeta_principal=os.path.dirname(__file__)
print(carpeta_principal)

#Carpeta imagenes
carpeta_imagenes=os.path.join(carpeta_principal,'imagenes')
print(carpeta_imagenes)


#Creacion de la Ventana principal
root=Tk()
#Titulo de la ventana
root.title('Modulo Tkinter')
#Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes,'world.ico'))

#Bucle de ejecucion
root.mainloop()