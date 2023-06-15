from PIL import Image
from PIL import ImageDraw
import os
import ajustar_tamano_tipografia as ajustar_tamano_tipografia

# Función para agregar texto a una imagen
def obtener(foto, text1, text2, fuente, textbox):
    """
    Retora en bytes la imagen (pasada por parametros) "dibujada" con los textos y tipografía pasados por parametro.
    """ 
    
    imagen = Image.open(os.path.join(os.getcwd(),"Fotos",foto)).convert("RGB")
    
    draw = ImageDraw.Draw(imagen)

    for posicion in range (1,3):
        #Inicializamos el lugar donde se posiciona el recuadro. 
        pos_x = textbox[posicion-1]["top_left_x"]
        pos_y = textbox[posicion-1]["top_left_y"]
        pos_x_abajo = textbox[posicion-1]["bottom_right_x"]
        pos_y_abajo = textbox[posicion-1]["bottom_right_y"]
        coordenadas= (pos_x, pos_y)

        tamano_textbox = (pos_x_abajo - pos_x, pos_y_abajo - pos_y)
        
        #Inicializamos la letra
        font = ajustar_tamano_tipografia.ajustar(eval(f"text{posicion}"), 25, fuente, tamano_textbox)

        # Crea una nueva imagen con el texto ajustado
        draw.text(coordenadas, eval(f"text{posicion}"), font=font, fill="black")
    
    return imagen