#Importaciones
from tkinter import *
import os
#descargar el modulo Pillow en la consola
#pip install Pillow
#Sino tienes actualizado el pip.  pip install --upgrade pip
from PIL import ImageTk,ImageColor,Image

#Carga de directorios
#Carpeta Principal
carpeta_principal=os.path.dirname(__file__)
#print(carpeta_principal)

#Carpeta imagenes
carpeta_imagenes=os.path.join(carpeta_principal,'imagenes')
#print(carpeta_imagenes)
carpeta_paisajes=os.path.join(carpeta_imagenes,'paisajes')
print(carpeta_paisajes)


#Creacion de la Ventana principal
root=Tk()
#Titulo de la ventana
root.title('Modulo Tkinter')
#Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes,'world.ico'))

#Carga de imagen
bosque=ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes,'naturaleza.jpg')).resize((850,600)))
etiqueta=Label(image=bosque)
etiqueta.pack()


#Bucle de ejecucion
root.mainloop()