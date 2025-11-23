import tkinter as tk
from tkinter import ttk

# Configuración de la raíz
root = tk.Tk()

# Los Radiobutton son widgets que suelen utilizarse en conjunto para mostrar varias
# opciones al usuario. El usuario podrá elegir una de las opciones y solo una. Es decir, solo
# podrá haber una opción seleccionada en cada momento.
# Cada opción representa un objeto de la clase Radiobutton en el que indicamos el texto a
# mostrar por pantalla y el valor que representa (puede ser igual al texto o no).
# La particularidad es que todos los objetos Radiobutton de un conjunto deben compartir la
# misma variable de control (objeto StringVar, IntVar, etc) para conocer el valor seleccionado
# por el usuario.

# También podemos asociarle una función o método a cada Radiobutton, igual como
# hacíamos con los botones sencillos.


#Colores
colores = ttk.Label(root, text="COLORES:")
colores.pack(fill='x', padx=10, pady=5)

opcion = tk.IntVar()
ttk.Radiobutton(root, text="Rojo", value=1, variable=opcion).pack(fill='x', padx=30, pady=5)
ttk.Radiobutton(root, text="Verde", value=2, variable=opcion).pack(fill='x', padx=30, pady=5)
ttk.Radiobutton(root, text="Azul", value=3, variable=opcion).pack(fill='x', padx=30, pady=5)


# Finalmente bucle de la aplicación
root.mainloop()