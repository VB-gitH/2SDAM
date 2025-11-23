import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as tfd

# En el módulo tkinter.filedialog encontramos funciones para trabajar con el sistema de archivos del
# sistema operativo. Por ejemplo: para abrir un fichero del disco duro o salvarlo.

# Se recogen algunos tipos de ventanas que encontramos en este módulo 


#
# DEFINICIÓN DE FUNCIONES -------------------------------------------
#
def selec():
    #Diálogo para seleccionar un fichero 
    dlg_selec = tfd.askopenfilename(
        title='Seleccionar un fichero',
        initialdir='/',
        filetypes= (('Fichero de texto', '*.txt'),
                    ('Todos los ficheros', '*.*')))
    
    #Instrucciones para gestionar el fichero seleccionado.

def save():
    #Diálogo para guardar el contenido de un fichero 
    dlg_save = tfd.asksaveasfilename(
        title="Guardar un fichero", defaultextension=".txt")
    
    #Instrucciones para salvar en el fichero seleccionado.
    

#
# PROGRAMA PRINCIPAL -------------------------------------------------
#

# Configuración de la raíz
root = tk.Tk()
root.config(bd=15) #tamaño del borde

btn_selec = ttk.Button(root, text="Seleccionar", command=selec).pack()
btn_salvar = ttk.Button(root, text="Guardar", command=save).pack() 

# Bucle de la aplicación
root.mainloop()