import tkinter as tk
from tkinter import ttk

# En los ejemplos anteriores hemos creados etiquetas que tenían un texto concreto pero, ¿y
# si queremos cambiar dicho texto durante la ejecución del programa?
# Una manera habitual de hacerlo es creando un objeto de tipo StringVar y asociándoselo a
# la etiqueta a través del atributo textvariable. De esta forma, cada vez que cambiemos el
# valor del objeto StringVar asociado, cambiará automáticamente el valor de la etiqueta
# correspondiente.

# Configuración de la raíz
root = tk.Tk()

root.config(bd=15)

# Ejemplo: Podemos asociar el objeto StringVar en el momento de crear la etiqueta o
# añadirlo después gracias a la función config() que nos permite modificar la configuración
# de un widget.

etiqueta = ttk.Label(root,  text="PAISAJE CAMPESTRE")
etiqueta.pack()
texto_etiqueta = tk.StringVar()
texto_etiqueta.set("Bienvenid@s")
etiqueta.config(textvariable=texto_etiqueta)

# Si quisiésemos recuperar el valor del widget asociado a la variable texto_etiqueta
# podríamos utilizar la función get(), de la siguiente forma:
# texto_etiqueta.get()

# Esta forma de asociar variables dinámicas a los objetos Label es extrapolable a otros
# widgets tal y como veremos en los siguientes apartados.
# Por último, cabe señalar que la clase StringVar es una variable de control de tipo carácter
# pero existen otras similares: IntVar (Para variables de tipo entero),
# DoubleVar (Para variables de coma flotante), BooleanVar (Para variables de tipo lógico).

# Bucle de la aplicación
root.mainloop()
