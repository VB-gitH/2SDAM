# Como hemos dicho, la raíz (root) o ventana principal es el primer widget que debe crearse. 
# Se trata del contenedor del resto de widgets y su tamaño se adapta al tamaño de los 
# widgets que contiene.

# Para crear la raíz de nuestra aplicación debemos seguir los siguientes pasos: 
#   1. Crear un objeto de la clase Tk(). Habitualmente se almacena en una variable 
#   llamada root, pero puede tener otro nombre. 
#   2. Inicializar los parámetros de la raíz o dejar por defecto. 
#   3. Lanzar el bucle mainloop() que se encarga de atender los eventos generados 
#   durante la ejecución y actualizar la interfaz de usuario.

# librería básica
import tkinter as tk
# widgets tematizados
from tkinter import ttk 

# Cremos la raíz "root"
root = tk.Tk()

# configuramos la raíz "root"
root.title("Bienvenid@s") # título de la ventana
#root.config(bd=15) # Permite especificar el ancho del borde de un widget. 
#                   Si lo utilizamos en la raíz, nos permite controlar el margen que habrá entre el borde de la 
#                   ventana y los widgets que contendrá.

root.geometry('500x150+250+250') # anchoxalto+x+y  NOTA: (x,y) son las coordenadas de la esquina superior izquierda


# bucle de eventos de la aplicación
root.mainloop()