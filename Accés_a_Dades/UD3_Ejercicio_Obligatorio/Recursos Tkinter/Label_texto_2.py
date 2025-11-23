import tkinter as tk
from tkinter import ttk


# Configuración de la raíz
root = tk.Tk()

root.config(bd=15)

# Las etiquetas sirven para mostrar texto o imágenes al usuario y pertenecen a la clase Label. 
# Cuando se crea una etiqueta, se debe indicar su contenedor o widget padre y una serie de 
# parámetros de configuración. Además, debemos seleccionar el gestor de geometría que queremos utilizar.


#Distintas formas de mostrar una etiqueta con texto -------------------------
#Forma 1:
etiqueta = ttk.Label(root, text="PAISAJE CAMPESTRE")
etiqueta.pack()

#Forma 2: compactamos las dos instrucciones en una sola
#etiqueta = ttk.Label(root, text="PAISAJE CAMPESTRE").pack()

#Forma 3: si no vamos a utilizar la variable para nada más la podemos quitar
#ttk.Label(root, text="PAISAJE CAMPESTRE").pack()


#Configuramos el aspecto del texto ------------------------------------------
'''
ttk.Label(root, text="PAISAJE CAMPESTRE",
         font= ("Verdana",24),
         foreground= "white",
         background= "grey"
         ).pack()
'''

#Si la etiqueta ya existe, podemos cambiar la configuración con config()

etiqueta.config(font= ("Verdana",24),
                foreground= "white",
                background= "grey")




# Bucle de la aplicación
root.mainloop()
