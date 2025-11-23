import tkinter as tk
from tkinter import ttk

# Configuración de la raíz
root = tk.Tk()
root.config(bd=15)

# Si necesitáramos mostrar un texto más largo o multilíneas entonces deberíamos
# trabajar con un objeto de la clase Text.

# Ejemplo: creamos un texto multilíneas básico

# Multilíneas básico ------------------------------------------
'''
texto = tk.Text(root)
texto.pack()
'''

# Ejemplo: Creamos un campo multilíneas personalizando algunos parámetros con la
# función config().

# Multilíneas personalizado ------------------------------------

texto = tk.Text(root)
texto.config(width=30, height=10, font=("Courier New",12), 
             padx=15, pady=15, selectbackground="grey")
texto.pack()

# Los parámetros width y height nos permiten indicar el tamaño del widgets en número de
# caracteres (y no en pixeles).
# Las características de la fuente de texto las configuramos con el parámetro font donde
# indicamos el tipo y tamaño de la misma.
# Los parámetros padx y pady permiten que indiquemos el espacio en blanco que habrá
# entre el borde del widget y el texto que contenga.
# Y, por último, con el parámetro selectbackground podemos configurar el color a utilizar
# cuando se seleccione un texto del widget.

# Veamos como podemos gestionar los objetos de tipo Text en un programa:
# Inicializar el valor: método insert()
'''
objeto_text.insert(posicion, texto_a_mostrar) # posición -> 'linea.columna'
texto = tk.Text(root)
'''
texto.insert('1.0', 'Hola a tod@s')

# Recuperar el valor: método get()
'''
objeto_text.get(pos_inicial, pos_final) # ambos en formato 'linea.columna'
'''
texto.get('1.0','end') # todo el texto
texto.get('2.1','3.0') # parte del contenido

# Habilitar o deshabilitar: popción state -> 'normal', 'disabled'
# texto['state'] = 'normal'
# texto['state'] = 'disabled'

# borrar el contenido: método delete
'''
objeto_text.delete(pos_inicial,pos_final)
'''
texto.delete('1.0', '1.4')

# Finalmente bucle de la aplicación
root.mainloop()