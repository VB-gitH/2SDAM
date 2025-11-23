import tkinter as tk
from tkinter import ttk

# En este apartado vamos a ver cómo recuperar el valor seleccionado por el usuario y,
# además, como crear un conjunto de objetos RadioButton de forma automática.


# DEFINICIÓN DE FUNCIONES --------------------------
# Muestra en la etiqueta "selec_texto" el valor seleccionado.
def selecciona():
    selec_texto.set(opcion_selec.get())


# PROGRAMA PRINCIPAL -------------------------------
# Configuración de la raíz
root = tk.Tk()

#Colores
colores = ttk.Label(root, text="COLORES:")
colores.pack(fill='x', padx=10, pady=5)

# Primero, veremos una forma de generar los botones de forma automática basándonos en
# el uso de una lista.

opcion_selec = tk.IntVar()
opciones = [["Rojo", 1],["Verde", 2],["Azul", 3]]
for opc in opciones:
    r = ttk.Radiobutton(root, text=opc[0], value=opc[1], variable=opcion_selec,
                command=selecciona).pack(fill='x', padx=30, pady=5)

# Fíjate que utilizamos el parámetro command de la clase RadioButton para que se ejecute
# una función llamada selecciona(), que se encargará de tratar el valor seleccionado.
# Para recuperar dicho valor deberemos utilizar el método get() de la variable de control
# asociada a los RadioButton, en este caso opcion_selec.

# Etiqueta que muestra el valor seleccionado:
selec_texto = tk.StringVar()
selec_texto.set('')
etq_seleccionado = tk.Label(root, textvariable = selec_texto).pack()

# Finalmente bucle de la aplicación
root.mainloop()