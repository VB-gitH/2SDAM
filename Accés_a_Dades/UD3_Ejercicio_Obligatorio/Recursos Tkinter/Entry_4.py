import tkinter as tk
from tkinter import ttk

# Configuración de la raíz
root = tk.Tk()
root.geometry('300x200+50+50') #anchoxalto+x+y

# La clase Entry de Tkinter nos permite crear cajas de texto o campos de entrada de una
# sola línea. Si, en lugar de eso, quisiésemos utilizar una caja de texto multilínea deberíamos
# utilizar la clase Text.

# Ejemplo: Creamos una caja para solicitar un nombre de usuario.
# usuario
usuario_label = ttk.Label(root, text="Usuario:")
usuario_label.pack()

# Al igual que con las etiquetas, podemos asociar objetos StringVar o similares a una caja de
# texto. De esta forma podremos tener control sobre el valor que contiene, modificarlo,
# validarlo, etc.
# Ejemplo: Creamos un objeto StringVar para la caja de texto del nombre de usuario.
'''
texto_usuario = tk.StringVar()
usuario_entry = ttk.Entry(root, textvariable=texto_usuario)
usuario_entry.pack()
usuario_entry.focus()
'''


usuario_entry = ttk.Entry(root)
#usuario_entry = ttk.Entry(root, justify='right') #configuramos la alineación del texto
usuario_entry.pack()
usuario_entry.focus()

# Otros parámetros que se pueden utilizar son:
# justify: 'left', 'center', 'right'
# state: 'disabled', 'normal'

'''
texto_usuario = tk.StringVar() 
usuario_entry = ttk.Entry(root, textvariable = texto_usuario) #usamos un StringVar para el valor
'''

# contraseña
contra_label = ttk.Label(root, text="Contraseña:")
contra_label.pack()

contra_entry = ttk.Entry(root, show="*") #enmascaramos los caracteres
contra_entry.pack()

# otro
otro_label = ttk.Label(root, text="Otro:")
otro_label.pack()

otro_entry = ttk.Entry(root, state= 'disabled') #deshabilitamos este campo
otro_entry.pack()


# Finalmente bucle de la aplicación
root.mainloop()