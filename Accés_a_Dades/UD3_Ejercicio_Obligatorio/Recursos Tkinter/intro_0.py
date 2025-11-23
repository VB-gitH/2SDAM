# comprobar si el módulo está instaldo: python3 -m tkinter (python en windows)

# librería básica
import tkinter as tk
# widgets tematizados
from tkinter import ttk 

# Una interfaz gráfica de Tkinter está compuesta por un conjunto de componentes o widgets
# que se corresponden con objetos de clases específicas de la librería Tkinter. Por ejemplo:
# tkinter.Frame, tkinter.Button,tkinter.Checkbutton, etc.

# El widget principal es la raíz o root. Se trata de la ventana principal de la aplicación y, por
# tanto, es el primer widget que debe crearse. Su aspecto dependerá del sistema operativo
# en el que se ejecute el programa.

# También existen otros tipos de widgets como pueden ser etiquetas, cajas de texto, botones, menús, etc.

# Estos widgets pueden alojarse directamente en la ventana principal (por defecto) o dentro 
# de widgets contenedores (por ejemplo: Frame, Labelframe) formando así una jerarquía 
# de widgets cuya raíz será la ventana principal de la aplicación. 

# La forma de ubicar los widgets en la raíz o en los contenedores viene determinada por el 
# Gestor de Geometría (Geometry Management). Existen varios tipos:

#   grid(): Ubica los elementos basándose en una parrilla o tabla e indicando, para cada 
#   uno de ellos, la fila y columna que debe ocupar dentro del contenedor.

#   pack(): Ubica los elementos según la configuración que se utilice. Existen varias: 
#   fill, expand, side, ipadx, ipady, padx, y pady. 
#   Es recomendable para ubicar los elementos de arriba a abajo (en forma de 
#   pila) o cuando queremos ubicarlos contiguos de izquierda a derecha.

#   place(): Ubica los elementos indicando las coordenadas de cada uno de ellos, es decir, 
#   indicando el valor para su posición horizontal (X) y vertical (Y) dentro del contenedor.
#   Es el gestor menos utilizado pero puede ser útil cuando permitimos que el 
#   usuario determine la posición de los elementos en pantalla.

