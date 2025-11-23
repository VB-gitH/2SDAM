import tkinter as tk
from tkinter import ttk


# Configuración de la raíz
root = tk.Tk()

# Si, en lugar de un texto, queremos mostrar una imagen en la etiqueta entonces debemos
# utilizar una objeto de la clase PhotoImage para crear un objeto imagen y luego pasarlo
# como argumento a la clase Label.

# Si la imagen se encuentra en una carpeta diferente de la del programa de Python,
# deberemos indicar la ruta completa en el parámetro file.
# La clase PhotoImage solo acepta los formatos de imagen pgm, ppm, gif y png. Si
# queremos utilizar otras extensiones deberemos instalar y hacer uso del módulo PIL (Pillow).

# Solo foto con texto ------------------------------------------------
'''
imagen = tk.PhotoImage(file="winter.png")
ttk.Label(root, image=imagen).pack()
'''

# También podríamos crear una etiqueta que contuviese un texto y una imagen a la vez. En
# ese caso deberíamos informar los parámetros text, image y compound. Éste último para
# indicar la manera de disponer el texto y la imagen dentro de la etiqueta.

# Foto con texto -----------------------------------------------------

imagen = tk.PhotoImage(file="polaroid.png")
ttk.Label(root, text="Polaroid",
         font= ("Verdana",24), # parámetros del texto
         foreground= "white",
         background= "grey",
         image=imagen,
         compound="top").pack() # parámetros de la imagen: "bottom", "left", "right" o "top"


# Para modificar la imagen que se muestra en una etiqueta debemos utilizar la propiedad
# config(file=nombre_fichero).
# imagen.config(file="winter.png")

# Bucle de la aplicación
root.mainloop()
