# Importing Image and ImageFont, ImageDraw module from PIL package 
from PIL import Image, ImageFont, ImageDraw,ImagePath
import os
import json
import textwrap



def cargar_lista_json(nombre):
    """
    Esta función retorna la lista de datos. Puede devolverla vacia en caso de que el archivo no exista o en el caso de que sea vacío.
    """
    #Se verifica si el archivo existe, si es asi se lo abre en modo lectura. En el case de que el archivo no exista se lo abre en modo escritura y se crea la lista de imagenes vacia.
    if os.path.exists(nombre):
        with open(nombre,'r') as archivo:
            #Se verifica si el archivo esta vacio, si es asi se crea la lista de imagenes vacia. Si el archivo no esta vacio se carga lista_imagenes con los datos.
            if (os.stat(nombre).st_size == 0):
                datos_json=[]
            else:
                datos = json.load(archivo)
                datos_json = list(map(lambda elem : elem,datos))
    else:
        with open(nombre,'w') as archivo:
            datos_json=[]

    return datos_json

foto = "meme3.png"

# creating a image object 
imagen = Image.open(os.path.join(os.getcwd(),"Fotos",foto))
  
draw = ImageDraw.Draw(imagen) 


texto = 'llego la banda del tartaro. el que se coje a los putos del faraon. pincha puto te queres morirsadashdfkas jhaskj hdklasgdlk agskd gaksg k'

templates = cargar_lista_json("template.json")

for arc in templates:
    if (arc['image'] == foto):
        datos = arc

fuente = "System"

font_path = f"{fuente}.ttf"  # Ruta de la fuente
font_size = datos["default_size"]
font = ImageFont.truetype(font_path, font_size)


pos_x = datos['text_boxes'][0]["top_left_x"]
pos_y = datos['text_boxes'][0]["top_left_y"]
coordenadas= (pos_x, pos_y)
   
centrar = False
# Dividir el texto en líneas más cortas según el ancho de la imagen
if (datos['forma'] == "rectangular"):
    lineas = textwrap.wrap(texto, width=int(imagen.width / font_size * 2))
    centrar = True
elif (datos['forma'] == "cuadrado"):
    lineas = textwrap.wrap(texto, width=int(imagen.width / font_size))

# Dibujar cada línea de texto
for linea in lineas:
    # Calcular la posición de inicio para centrar horizontalmente el texto en cada línea
    bbox = draw.textbbox(coordenadas, linea, font=font)
    if (centrar == True):
        pos_x = int((imagen.width - bbox[2]) / 2)
    draw.text((pos_x, pos_y), linea, font=font, fill=datos['color'])
    pos_y += font_size


imagen.show()