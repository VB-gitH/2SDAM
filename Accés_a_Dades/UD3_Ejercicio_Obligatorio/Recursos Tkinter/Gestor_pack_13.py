import tkinter as tk
from tkinter import ttk
    
def sumar():
    pass

# Configuración de la raíz
root = tk.Tk()
root.config(bd=20)
root.geometry('400x150+500+300')

#Configuración de los botones básicos ---------------------------
boton1 = ttk.Button(root, text="Uno", command=sumar)
boton1.pack()

boton2 = ttk.Button(root, text="Dos", command=sumar)
boton2.pack()

# la función pack() sin parámetros ubica los widgets centrados y apilados uno encima de otro.

#Probamos los parámetros <fill> y <expand> ----------------------
#boton1.pack(fill='x')
#boton2.pack(fill='both', expand=True)

# El parámetro fill sirve para indicar si queremos que el widget rellene todo el espacio 
# disponible. Podemos seleccionar si queremos que se expanda a lo largo del eje de 
# coordenadas X, a lo largo del eje de coordenadas Y o a lo largo de los dos ejes (both).
# Si queremos que el widget pueda crecer verticalmente debemos utilizar el parámetro fill 
# junto con el parámetro expand.

#Probamos los parámetros <ipadx> e <ipady> ----------------------
# boton1.pack(ipadx=40, ipady=20)

# Los parámetros ipadx e ipady sirven para indicar el relleno que habrá entre el contenido 
# del widget y su borde externo. Podemos indicar el relleno en el eje de coordenadas X 
# (ipadx) y en el eje de coordenadas Y (ipadx).

#Probamos side='left' -------------------------------------------
# boton1.pack(side='left')
# boton2.pack(side='left')

#Probamos side='right' -------------------------------------------
# boton1.pack(side='right')
# boton2.pack(side='right')

#Probamos side='bottom' -------------------------------------------
# boton1.pack(side='bottom')
# boton2.pack(side='bottom')

# el parámetro side que nos permite indicar qué lado del widget 
# alinearemos con su contenedor. Los posibles valores son los siguientes: left, right, top, 
# bottom. Tal y como hemos podido comprobar, el valor por defecto es top.


# Bucle de la aplicación
root.mainloop()