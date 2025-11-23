import tkinter as tk
from tkinter import ttk

#Configuración de la raíz
root = tk.Tk()
root.config(bd=20)

# Los contenedores, marcos o frames (en inglés) son widgets con forma rectangular que 
# permiten organizar o agrupar otros widgets en su interior. Estos contenedores pueden 
# posicionarse directamente en la raíz o en otro contenedor. 
# En este apartado hablaremos de dos tipos de contenedores pertenecientes a las clases 
# Frame y LabelFrame.

#Marco básico
marco = tk.Frame(root, width='300', height='300')
marco.config(background='pink')
marco['borderwidth'] = 5  #Ancho del borde
marco['relief'] = 'solid' #Relieve, otros: flat, groove, raised, ridge, sunken.
marco.pack()

#Widgets dentro del marco
ttk.Label(marco, text="Estoy dentro del marco").pack(padx=20, pady=20)
ttk.Label(marco, text="Estoy dentro del marco").pack(padx=20, pady=20)

#Widgets fuera del marco
ttk.Label(root, text="Estoy fuera del marco").pack(padx=20, pady=20)

#Bucle de la aplicación
root.mainloop()