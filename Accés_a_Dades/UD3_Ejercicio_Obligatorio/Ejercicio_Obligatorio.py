
#Reordenamos las importaciones
#-----Librerías standard ----
import csv                          # librería para CSV
import io                           # io.StringIO(texto) para CSV -> OBJ permite tratar el texto como archivo
import json                         # librería para JSON
import pickle                       # librería para pickle
from functools import partial       # para poder pasar parámetros a las funciones de callback

#------ Tkinter ------
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog as tfd
import tkinter.messagebox as tmb

#------- Librerías externas -------
import xml.etree.ElementTree as ET  # librería para XML
from bs4 import BeautifulSoup       # librería para HTML

#----- Dataclass -------
from dataclasses import dataclass   # almacenamiento de datos en objetos Python


# clase para guardar los datos
@dataclass
class Producto():
    """
    Representa un libro de la librería con sus atributos principales.

    Atributos:
        genero (str): Categoría o género literario.
        titulo (str): Título del libro.
        autor (str): Nombre del autor.
        precio (float): Precio del libro.
        disponible (bool): Indica si el libro está disponible (True/False).
    """
    genero: str
    titulo: str
    autor: str
    precio: float
    disponible: bool
    

    def __post_init__(self):
        self.genero = self.genero.strip()
        self.titulo = self.titulo.strip()
        self.autor = self.autor.strip()
        self.precio = float(self.precio)


#
# DEFINICIÓN DE FUNCIONES
#
def seleccionar_fichero(editor):
    '''Diálogo para seleccionar un fichero y mostrarlo en el editor
    Args:
        editor(ScrolledText): zona para visualizar/editar datos
    '''
    dlg_selec = tfd.askopenfilename(
        title='Seleccionar un fichero',
        initialdir='/',
        filetypes= (('Fichero de texto', '*.txt'),
                    ('Todos los ficheros', '*.*')))
    
    # leemos todo el fichero
    with open(dlg_selec, 'r', encoding='utf-8') as fr: #De esta manera nos reconoce los acentos y otros caracteres.
        contenido = fr.read()
    
    # guardamos en el editor
    editor.delete(1.0,'end')
    editor.insert('1.0', contenido)
    
    
def guardar_fichero(editor):
    '''Diálogo para guardar el contenido del editor en un fichero
    Args:
        editor(ScrolledText): zona para visualizar/editar datos
    ''' 
    dlg_save = tfd.asksaveasfilename(
        title="Guardar un fichero", defaultextension=".txt")
    
    # escribimos el fichero con el contenido del editor
    with open(dlg_save, 'w') as fw:        
        fw.write(editor.get('1.0','end'))
    
def extraer_producto_de_xml(producto_xml):
    genero = producto_xml.attrib['genero']
    titulo = producto_xml.find('titulo').text
    autor = producto_xml.find('autor').text
    precio = producto_xml.find('precio').text
    disponible = producto_xml.find('disponible').text
    disponible = True if disponible == 'si' else False
    return Producto(genero, titulo, autor, precio, disponible)


def xml_a_objetos(editor):
    '''Parsea el texto XML y lo convierte en objetos Producto.
    Args:
        editor(ScrolledText): zona para visualizar/editar datos
    '''
    try:
        productos = []
        str_xml_editor = editor.get('1.0', 'end')

        if str_xml_editor =='\n':
            raise Exception('No hay libros o se ha cargado un xml no compatible.')
        
        xml = ET.fromstring(str_xml_editor)
        productos_xml = xml.findall('libro') # retorna una lista de productos
        for producto_xml in productos_xml:
            productos.append(extraer_producto_de_xml(producto_xml))
        if not productos:
            raise Exception("No hay libros o se ha cargado un xml no compatible.")

    except SyntaxError:
        tmb.showerror("Error", "Parece que la sintaxis no es XML.")

    except Exception as e:
        tmb.showerror("Error", f'{e}')
    else:
        # mostramos en el editor
        editor.delete('1.0','end')
        texto_a_insertar = ''
        for producto in productos:
            texto_a_insertar += str(producto) + '\n'
        editor.insert(f'1.0',texto_a_insertar)


def objetos_a_xml(editor):
    '''genera un texto xml a partir de los objetos (en texto) que hay en el editor
    Args:
        editor(ScrolledText): zona para editar/visualizar datos
    '''
    try:
        # creamos el elemento raíz
        raiz_xml = ET.Element('libreria')

        # leemos los objetos del editor
        texto_objetos = editor.get('1.0','end')
        lista_objetos = texto_objetos.split(sep='\n')

        # quito basura 
        while True:
            try:
                lista_objetos.remove('')
            except ValueError:
                break
    
        if not lista_objetos:
            raise Exception("No hay objetos.")
        
    except Exception as e:
        tmb.showerror("Error", f'{e}')

    else:
        # creamos elementos libro
        for libro in lista_objetos:
            try:
                objeto_producto = eval(libro)
            except Exception as e:
                tmb.showerror("Error", f'{e}')
            else:
                libro_xml = ET.Element('libro', attrib=dict(genero=objeto_producto.genero))
                # creamos subelementos libro y los enganchamos
                titulo_xml = ET.Element('titulo')
                titulo_xml.text = objeto_producto.titulo
                autor_xml = ET.Element('autor')
                autor_xml.text = objeto_producto.autor
                precio_xml = ET.Element('precio')
                precio_xml.text = str(objeto_producto.precio)
                disponible_xml = ET.Element('disponible')
                disponible_xml.text = "si" if objeto_producto.disponible else "no"

                libro_xml.extend([titulo_xml, autor_xml, precio_xml, disponible_xml])

                # enganchamos el libro a la raiz
                raiz_xml.append(libro_xml)

        # generamos la cadena con la raiz
        ET.indent(raiz_xml, space="\t", level=0) # prettify
        str_xml = ET.tostring(raiz_xml, encoding="unicode", xml_declaration=True)

        # mostramos en el editor
        editor.delete(1.0,'end')
        editor.insert('1.0', str_xml)    


def html_a_objetos(editor):
    '''Parsea un texto html del editor a objetos
    Args:
        editor(ScrolledText): zona para editar/visualizar datos.

    Analiza un documento HTML y crea objetos Producto a partir de su estructura.

    Utiliza BeautifulSoup para localizar los bloques <div class="libro">,
    obteniendo de cada uno el género, título, autor, precio y disponibilidad.
    Todos los campos se validan antes de crear el Producto. 

    Los objetos resultantes se muestran en el editor.
    '''
    try:
        #Seguimos los siguientes pasos:
        #Obtener el texto del editor

        texto_html = editor.get('1.0', 'end').strip()

        if not texto_html:
            raise Exception("El HTML está vacío.")

        #Parsear HTML con BeautifulSoup, el cual entiende HTML y nos permitirá recorrerlo.

        soup = BeautifulSoup(texto_html, 'html.parser')

        #Encontrar todos los productos con class="libro"

        libros = soup.find_all('div', class_='libro')

        if not libros:
            raise Exception("No se encontraron elementos <div> en el HTML.")

        productos = []

        for libro in libros:
            #Género está en <h2>

            h2 = libro.find('h2')
            if not h2:
                raise Exception("No se encontró la etiqueta <h2> para el género.")
            genero = h2.get_text().strip()

             #Obtenemos el resto de campos desde sus etiquetas específicas

            titulo_div = libro.find('div', class_='titulo')
            autor_div = libro.find('div', class_='autor')
            precio_div = libro.find('div', class_='precio')
            disponible_div = libro.find('div', class_='disponible')

             #Nos aseguramos de que todos los campos existen
            if not titulo_div or not autor_div or not precio_div or not disponible_div:
                raise Exception("Faltan campos obligatorios (titulo, autor, precio o disponible).")

            #Vamos a extraer texto limpio de cada campo
            titulo = titulo_div.get_text().strip()
            autor = autor_div.get_text().strip()

            try:
                precio = float(precio_div.get_text().strip())# Convertimos precio a valor numérico
            except:
                raise Exception("El precio no es válido.")
            
            #...y 'si'/'no' a 'true'/'false'
            disponible_text = disponible_div.get_text().strip().lower()
            disponible = True if disponible_text == "si" else False

            #Creamos y guardamos el objeto "Producto"
            prod = Producto(genero, titulo, autor, precio, disponible)
            productos.append(prod)
        
        #Controlamos posibles errores

    except Exception as e:
        tmb.showerror("Error", str(e))

    else:
        #Mostramos en el editor los objetos guardadso.
        editor.delete('1.0', 'end')
        for p in productos:
            editor.insert('end', str(p) + '\n')


def objetos_a_html(editor):
    '''Genera un texto html a partir de los objetos (en texto) que hay en el editor
    Args:
        editor(ScrolledText): zona para editar/visualizar datos
    
    Genera un documento HTML con la información de los objetos Producto.

    Toma los objetos escritos en el editor, los valida y construye un HTML
    sencillo con la estructura utilizada en el proyecto: un <div class="libro">
    por producto, con sus campos correspondientes. 
    
    El HTML generado se muestra en el editor.
    '''
    try:
        # Leemos texto del editor
        texto_obj = editor.get('1.0', 'end').strip()

        if not texto_obj:
            raise Exception("No hay objetos en el editor.")

        # Separamos líneas
        lineas = texto_obj.split('\n')

        productos = []

        # Realizamos conversión texto -> objetos Producto
        for linea in lineas:
            if not linea.strip():
                continue

            try:
                obj = eval(linea)
            except:
                raise Exception("Alguna línea no contiene un objeto Producto válido.")

            if not isinstance(obj, Producto):
                raise Exception("El contenido no corresponde a objetos Producto.")

            productos.append(obj)

        if not productos:
            raise Exception("No se pudieron generar objetos Producto.")

        # Vamos a generar el HTML
        html = "<html>\n<body>\n"

        for p in productos:
            html += "  <div>\n"
            html += f"    <p>genero: {p.genero}</p>\n"
            html += f"    <p>titulo: {p.titulo}</p>\n"
            html += f"    <p>autor: {p.autor}</p>\n"
            html += f"    <p>precio: {p.precio}</p>\n"
            html += f"    <p>disponible: {'si' if p.disponible else 'no'}</p>\n"
            html += "  </div>\n\n"

        html += "</body>\n</html>"

    except Exception as e:
        tmb.showerror("Error", str(e))

    else:
        # Mostramos HTML final en el editor
        editor.delete('1.0', 'end')
        editor.insert('1.0', html)


def csv_a_objetos(editor):
    '''Parsea un texto csv del editor a objetos
    Args:
        editor(ScrolledText): zona para editar/visualizar datos.

    Convierte el contenido CSV del editor en una lista de objetos Producto.

    Lee el texto del editor como un CSV con cabecera, valida su estructura
    y convierte cada fila en un objeto Producto. 

    Controla errores de formato,tipos de datos y campos obligatorios.
    El resultado se muestra de nuevo en el editor como una lista legible de objetos.
    '''
    try:
        # 1-Obtenemos el texto del editor, desde el inicio '1.0' hasta el final 'end'
        # ...y eliminamos los saltos de línea con strip().

        texto_csv = editor.get('1.0', 'end').strip()

        if not texto_csv:
            raise Exception("El CSV está vacío.") # Error si el CSV no contiene texto

        # 2-Creamos un objeto StringIO para simular un archivo, ya que DictReader lo necesita.

        f = io.StringIO(texto_csv)

        # 3-DictReader lee el CSV como diccionarios
        lector = csv.DictReader(f)

        productos = [] #En esta lista vacía guardaremos los objetos

        for fila in lector:
            # Comprobamos que la fila tiene todos los campos necesarios
            if not all(clave in fila for clave in ("genero", "titulo", "autor", "precio", "disponible")):
                raise Exception("El CSV no contiene las columnas necesarias.")

            genero = fila["genero"]
            titulo = fila["titulo"]
            autor = fila["autor"]

            # Convertimos precio, ya que lo queremos pasar a valor numérico

            try:
                precio = float(fila["precio"])
            except ValueError:
                raise Exception("El precio no es un número válido.")

            # Convertimos disponible, pues queremos un booleano.

            disponible = True if fila["disponible"].strip().lower() == "si" else False

            # Vamos a crear el objeto Producto

            producto = Producto(genero, titulo, autor, precio, disponible)
            productos.append(producto)

        if not productos:
            raise Exception("No se encontraron productos en el CSV.") #Error en caso de no encontrar productos

    except Exception as e:
        tmb.showerror("Error", str(e))

    else:
        # Se muestran los objetos en el editor
        editor.delete('1.0', 'end')
        for p in productos:
            editor.insert('end', str(p) + '\n')


def objetos_a_csv(editor):
    ''' Genera un CSV a partir de los objetos Producto escritos en el editor.

    Convierte cada línea del editor en un objeto Producto mediante eval(),
    valida su estructura y los transforma en un CSV estándar con su cabecera.
    Los valores booleanos se convierten a 'si'/'no'. 

    El CSV generado se muestra en el editor.
    '''
    try:
        # Se obtiene texto del editor, de nuevo: de principio a fin y evitando saltos.
        texto_obj = editor.get('1.0', 'end').strip()

        if not texto_obj:
            raise Exception("No hay objetos en el editor.")

        # Dividimos líneas
        lineas = texto_obj.split('\n')

        objetos = []
        #Recorremos cada línea y vamos a almacenar resultados en nuestra lista vacía.

        for linea in lineas:
            if not linea.strip():
                continue  # Ignoramos líneas vacías

            try:
                obj = eval(linea) #Converitimos texto a un objeto real...si falla eval, es que el usuario
                                  #ha editado el texto de forma incorrecta.
            except:
                raise Exception("Alguna línea no contiene un objeto Producto válido.")

            if not isinstance(obj, Producto):
                raise Exception("El contenido no es un objeto Producto.")

            objetos.append(obj)

        if not objetos:
            raise Exception("No se pudieron generar objetos Producto.")

        # Creamos CSV con StringIO

        salida = io.StringIO()
        escritor = csv.writer(salida)

        # Se escribe la cabecera

        escritor.writerow(["genero", "titulo", "autor", "precio", "disponible"])

        # Escribimos los objetos

        for p in objetos:
            escritor.writerow([
                p.genero,
                p.titulo,
                p.autor,
                p.precio,
                "si" if p.disponible else "no"
            ])

    except Exception as e:
        tmb.showerror("Error", str(e))

    else:
        # Se muestra CSV en el editor
        editor.delete('1.0', 'end')
        editor.insert('1.0', salida.getvalue())


def como_productos(dct):
    '''Retorna un objeto Producto a partir de un diccionario
    Args:
        dct(dict): diccionario con la información necesaria para crear un objeto Producto
    '''
    return Producto(dct['genero'], dct['titulo'], dct['autor'], dct['precio'], dct['disponible'])

class ProductoEncoder(json.JSONEncoder):
    '''Si el objeto es de tipo Producto lo pasa a dict para que json.JSONEncoder pueda codificarlo.
    En otro caso, json.JOSNEncoder lo codifica directamente
    '''
    def default(self, o):
        if isinstance(o, Producto):
            return dict(genero=o.genero, titulo=o.titulo, autor=o.autor, precio=float(o.precio), disponible=o.disponible)
        return json.JSONEncoder.default(self, o)


def json_a_objetos(editor):
    '''Parsea un texto json del editor a objetos
    Args:
        editor(ScrolledText): zona para editar/visualizar datos
    
    Convierte una lista JSON de diccionarios en objetos Producto.

    Valida que el contenido del editor es un JSON correcto, lo carga en
    memoria y transforma cada diccionario en un Producto usando la función
    auxiliar como_productos(). Detecta errores de formato y tipos.

    El resultado se muestra en el editor.
    '''
    try:
        # Llevamos a cabo los siguientes pasos:
        # 1-Obtener el texto del editor

        texto_json = editor.get('1.0', 'end').strip()

        if not texto_json:
            raise Exception("El JSON está vacío.")

        # 2-Intentar la carga del JSON

        try:
            datos = json.loads(texto_json)
        except json.JSONDecodeError:
            raise Exception("El texto no es un JSON válido.")

        # 3-Validar que es una lista

        if not isinstance(datos, list):
            raise Exception("El JSON debe contener una lista de productos.")

        productos = []

        # 4-Convertir diccionarios en objetos Producto

        for d in datos:
            if not isinstance(d, dict):
                raise Exception("El JSON contiene elementos que no son diccionarios.")

            # Convertimos a Producto usando la función auxiliar y controlamos excepciones

            try:
                prod = como_productos(d) #Función auxiliar
            except KeyError:
                raise Exception("Faltan campos en algún diccionario del JSON.")
            except Exception:
                raise Exception("No se pudo convertir un diccionario a Producto.")

            productos.append(prod)

        if not productos:
            raise Exception("No se encontraron productos en el JSON.")

    except Exception as e:
        tmb.showerror("Error", str(e))

    else:
        # Para finalizar, se muestran los objetos en el editor
        editor.delete('1.0', 'end')
        for p in productos:
            editor.insert('end', str(p) + '\n')


def objetos_a_json(editor):
    '''Genera un texto json a partir de los objetos (en texto) que hay en el editor
    Args:
        editor(ScrolledText): zona para editar/visualizar datos

    Convierte los objetos Producto del editor a una lista JSON.

    Interpreta cada línea del editor como un objeto Producto, valida su tipo
    y usa ProductoEncoder para serializarlos a JSON con indentación.

    Se controla que todos los objetos sean válidos. El JSON resultante se
    muestra en el editor de forma clara.
    '''
    try:
        #Esta vez relizamos el camino inverso, vamos a:
        # 1-Obtener texto del editor

        texto_obj = editor.get('1.0', 'end').strip()

        if not texto_obj:
            raise Exception("No hay objetos en el editor.")

        # 2-Dividir en líneas

        lineas = texto_obj.split('\n')

        productos = [] #Convertimos todas las líneas en una lista.

        # 3-Convertir cada línea a un objeto Producto

        for linea in lineas:
            if not linea.strip():
                continue

            try:
                obj = eval(linea) #Convertimos cada línea en un objeto real
            except:
                raise Exception("Alguna línea no contiene un objeto Producto válido.")

            if not isinstance(obj, Producto):
                raise Exception("El contenido no corresponde a objetos Producto.")

            productos.append(obj)

        if not productos:
            raise Exception("No se pudieron generar objetos Producto.")

        # 4-Convertir la lista de objetos a JSON

        json_texto = json.dumps(productos, cls=ProductoEncoder, indent=4)

    except Exception as e:
        tmb.showerror("Error", str(e))

    else:
        # 5-Mostrar el JSON en el editor

        editor.delete('1.0', 'end')
        editor.insert('1.0', json_texto)

# VARIABLE GLOBAL
lista_objetos_pickle = []

def pickle_a_objetos(editor):
    '''Deserializa los objetos pickle del editor a objetos Python (muestra el resultado en el editor).
    En la variable global lista_objetos_pickle está el resultado de la serialización anterior.

    Args:
        editor(ScrolledText): zona para editar/visualizar datos
    
    Reconstruye objetos Producto a partir de los datos guardados en pickle.

    Lee las serializaciones almacenadas en lista_objetos_pickle y las
    deserializa con pickle.loads(). Valida que cada objeto recuperado sea un
    Producto y los muestra en el editor. 
    
    Informa de errores si la lista está vacía o contiene datos corruptos.
    '''
    try:
        global lista_objetos_pickle #Declaramos la variable local, sin esto no podemos leer los pickle almacenados.

        #Con esta función vamos a:
        # 1-Verificar si hay objetos pickle presentes, sin ejecutar antes obj->pickle, no habrá nada que deserializar.

        if not lista_objetos_pickle:
            raise Exception("No hay objetos pickle serializados. Primero usa 'obj->pickle'.")

        productos = []

        # 2-Deserializar cada objeto.

        for idx, dato in enumerate(lista_objetos_pickle): #'dato' es un bloque de bytes.
            try:
                obj = pickle.loads(dato) #Esto convierte los bytes en un objeto real.
            except Exception:
                raise Exception(f"No se pudo deserializar el objeto pickle número {idx+1}.")

            if not isinstance(obj, Producto):
                raise Exception("El objeto deserializado no es de tipo Producto.")

            productos.append(obj) #Guardamos el objeto reconstruído.

    except Exception as e:
        tmb.showerror("Error", str(e))

    else:
        # 3-Mostrar los objetos reconstruidos en el editor'.

        editor.delete('1.0', 'end')
        for p in productos:
            editor.insert('end', str(p) + '\n')

def objetos_a_pickle(editor):
    '''serializa los objetos del editor a pickle (muestra el resultado en el editor)
    Al mismo tiempo se guarda una variable global lista_objetos_pickle con todas las serializaciones.
    Esto es porque pickle solo serializa un objeto cada vez
    Args:
        editor(ScrolledText): zona para editar/visualizar datos.

    Serializa los objetos Producto del editor a formato pickle.

    Convierte cada línea del editor en un Producto y lo serializa con pickle.
    Todas las serializaciones se almacenan en la variable global
    lista_objetos_pickle. 
    En el editor se muestra un mensaje informativo y una vista parcial del binario generado.
    '''
    try:
        global lista_objetos_pickle   # Necesitamos modificar la variable global

        # Pasos a seguir
        # Leer texto del 
        
        texto_obj = editor.get('1.0', 'end').strip()

        if not texto_obj:
            raise Exception("No hay objetos en el editor.")

        # Separar líneas

        lineas = texto_obj.split('\n')

        lista_objetos_pickle = []   # Vaciar la lista antes de llenarla otra vez

        # Convertir texto -> objetos Producto y serializar

        for linea in lineas:
            if not linea.strip():
                continue

            try:
                obj = eval(linea)
            except:
                raise Exception("Alguna línea no contiene un objeto Producto válido.")

            if not isinstance(obj, Producto):
                raise Exception("El contenido no corresponde a objetos Producto.")

            # Serializar a pickle (binario). Esto genera una secuencia de bytes que representa el objeto.

            serializado = pickle.dumps(obj)

            # Guardar el binario en la variable global

            lista_objetos_pickle.append(serializado)

    except Exception as e:
        tmb.showerror("Error", str(e))

    else:
        # Como no podemos mostrar binario en el editor, mostramos un mensaje de confirmación.

        editor.delete('1.0', 'end')

        editor.insert('end', "Serialización PICKLE completada.\n")
        editor.insert('end', "Objetos serializados guardados en lista_objetos_pickle.\n\n")

        # Mostrar una vista legible (no el binario completo)

        for i, p in enumerate(lista_objetos_pickle):
            editor.insert('end', f"Objeto {i+1}: {str(p[:20])}... (binario)\n")

#
# INTERFAZ GRÁFICA
#

# Configuración de la raíz
root = tk.Tk()
root.geometry("800x600+50+50")
root.title('Files')

# Marco para el texto
marco_texto = tk.Frame(root, height='400')
marco_texto.config(background='white')
marco_texto['borderwidth'] = 5  #Ancho del borde
marco_texto['relief'] = 'sunken' #Relieve, otros: flat, groove, raised, ridge, sunken.
marco_texto.pack(fill='x')

etiqueta_texto = ttk.Label(marco_texto, text="VISOR/EDITOR DE CONTENIDO")
etiqueta_texto.config(background='white')
etiqueta_texto.pack()

# Text + scroll
texto = ScrolledText(marco_texto)
texto.config(state='normal')
texto.pack(fill='both')

# Marco para la botonera
marco_botones = tk.Frame(root, height='150')
marco_botones.config(background='white')
marco_botones['borderwidth'] = 5
marco_botones['relief'] = 'sunken'
marco_botones.pack(fill='x',side='bottom')

# botones
boton_xml_objetos = ttk.Button(marco_botones, text="xml->obj", command=partial(xml_a_objetos, texto))
boton_xml_objetos.config(padding=10, width=15)
boton_xml_objetos.grid(row=0, column=0, padx=5, pady=5)

# Aquí van los botones que faltan de la fila 0

boton_objetos_xml = ttk.Button(marco_botones, text="obj->xml", command=partial(objetos_a_xml, texto))
boton_objetos_xml.config(padding=10, width=15)
boton_objetos_xml.grid(row=1, column=0, padx=5, pady=5)

boton_html_objetos = ttk.Button(marco_botones, text="html->obj", command=partial(html_a_objetos, texto))
boton_html_objetos.config(padding=10, width=15)
boton_html_objetos.grid(row=0, column=1, padx=5, pady=5)

boton_objetos_html = ttk.Button(marco_botones, text="obj->html", command=partial(objetos_a_html, texto))
boton_objetos_html.config(padding=10, width=15)
boton_objetos_html.grid(row=1, column=1, padx=5, pady=5)

boton_csv_objetos = ttk.Button(marco_botones,text="csv->obj",command=partial(csv_a_objetos, texto))
boton_csv_objetos.config(padding=10, width=15)
boton_csv_objetos.grid(row=0, column=2, padx=5, pady=5)

boton_objetos_csv = ttk.Button(marco_botones,text="obj->csv",command=partial(objetos_a_csv, texto))
boton_objetos_csv.config(padding=10, width=15)
boton_objetos_csv.grid(row=1, column=2, padx=5, pady=5)

boton_json_objetos = ttk.Button(marco_botones,text="json->obj",command=partial(json_a_objetos, texto))
boton_json_objetos.config(padding=10, width=15)
boton_json_objetos.grid(row=0, column=3, padx=5, pady=5)

boton_objetos_json = ttk.Button(marco_botones,text="obj->json",command=partial(objetos_a_json, texto))
boton_objetos_json.config(padding=10, width=15)
boton_objetos_json.grid(row=1, column=3, padx=5, pady=5)

boton_pickle_objetos = ttk.Button(marco_botones,text="pickle->obj",command=partial(pickle_a_objetos, texto))
boton_pickle_objetos.config(padding=10, width=15)
boton_pickle_objetos.grid(row=0, column=4, padx=5, pady=5)

boton_objetos_pickle = ttk.Button(marco_botones,text="obj->pickle",command=partial(objetos_a_pickle, texto))
boton_objetos_pickle.config(padding=10, width=15)
boton_objetos_pickle.grid(row=1, column=4, padx=5, pady=5)





# Aquí van los botones que faltan de la fila 1

# Creamos el menú principal
menubar = tk.Menu(root)   #Creamos el objeto Menu
root.config(menu=menubar) #Indicamos que es el menú principal

# Creamos los submenús
archivo_menu = tk.Menu(menubar, tearoff=False)

# Añadimos opciones al submenú "Archivo"
# cada opción tendrá una función o método que ejecutará
archivo_menu.add_command(label="Abrir", command=partial(seleccionar_fichero, texto)) # label es el texto que mostrará
archivo_menu.add_command(label="Guardar", command=partial(guardar_fichero, texto))
archivo_menu.add_separator() # línea separadora
archivo_menu.add_command(label="Salir", command=root.destroy) # command es el comando que se ejecutará

# Asignamos los submenús al menú principal
menubar.add_cascade(label="Archivo", menu=archivo_menu) # label es el texto que se mostrará

# Bucle de la aplicación
root.mainloop()
