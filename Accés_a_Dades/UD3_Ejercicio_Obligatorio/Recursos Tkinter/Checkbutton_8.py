import tkinter as tk
from tkinter import ttk

# Configuración de la raíz
root = tk.Tk()

# Este tipo de botones se utilizan para marcar o desmarcar alguna opción. A diferencia de
# los Radiobutton, éstos no se utilizan en grupo sino que son independientes entre sí.

#Ingredientes pizza
ingredientes = ttk.Label(root, text="INGREDIENTES PIZZA:")
ingredientes.pack(fill='x', padx=10, pady=5)

queso = tk.BooleanVar()
check1 = ttk.Checkbutton(root, text="Queso", variable=queso, onvalue=True, offvalue=False)
check1.pack(fill='x', padx=30, pady=5)

cebolla = tk.BooleanVar()
check2 = ttk.Checkbutton(root, text="Cebolla", variable=cebolla, onvalue=True, offvalue=False)
check2.pack(fill='x', padx=30, pady=5)

guindilla = tk.BooleanVar()
check3 = ttk.Checkbutton(root, text="Guindilla", variable=guindilla, onvalue=True, offvalue=False)
check3.pack(fill='x', padx=30, pady=5)

# También podemos asociarle una función o método a cada Radiobutton, igual como
# hacíamos con los otros botones.

# Finalmente bucle de la aplicación
root.mainloop()