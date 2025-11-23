import tkinter as tk
from tkinter import ttk
    
def sumar():
    pass

# Configuración de la raíz
root = tk.Tk()
root.config(bd=15)

# Los botones son widgets que muestran un texto o una imagen y ejecutan una acción
# cuando se clica sobre ellos. Además, podemos asociarles un atajo de teclado (keyboard
# shortcut).
# Existen muchas opciones para configurar un botón pero aquí nos centraremos en las más
# habituales.



#Botón con texto

# el comando suele ser una función o un método de una clase
#boton1 = ttk.Button(root, text="Sumar", command=sumar)
#boton1.pack()

# el botón lo podemos habilitar o deshabilitar cambiando su atributo 'state'
#boton1['state'] = tk.NORMAL 
#boton1['state'] = tk.DISABLED

#Botón con una imagen
# Si queremos asociar una imagen al botón entonces deberemos crear un objeto
# PhotoImage igual que hicimos con las etiquetas.
'''
imagen = tk.PhotoImage(file="suma.png")
boton1 = ttk.Button(root, image=imagen, command=sumar)
boton1.pack()
'''

#Botón con una imagen y un texto
# Si queremos que se muestren tanto un texto como una imagen, deberemos configurar el
# atributo compound igual que anteriormente.

imagen = tk.PhotoImage(file="suma.png")
boton1 = ttk.Button(root, text="suma ", image=imagen, compound="right", command=sumar)
boton1.pack()


# Finalmente bucle de la aplicación
root.mainloop()
