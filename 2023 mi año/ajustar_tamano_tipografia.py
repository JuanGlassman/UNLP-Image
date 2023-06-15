from PIL import ImageFont

def ajustar(texto, max_tamano, font_path, tamano_textbox):
    """
    Ajusta el tamaño de la tipografía pasada por parametro de acuerdo al texto, tamaño maximo, ancho y alto del recuadro.
    """

    font_size = 1
    font = ImageFont.truetype(font_path, font_size)

    #Obtenemos la cadena de texto de largo maximo.
    tamano_texto = max(texto.split('\n'), key=len)

    #Obtenemos la altura del texto multiplicando la cantidad de cadenas por el tamaño de tipografía.
    altura_texto = len(texto.split('\n'))

    # Ajusta gradualmente el tamaño de la tipografía hasta el ancho máximo multiplicado por 0.9 (obtenemos el 90 % de la foto como margen de seguridad). El bucle se realiza mientras la linea mas larga sea menor al tamaño de la imagen o hasta que se haya alcanzado el tamaño de tipografia maximo.
    while ((font.getsize(tamano_texto)[0] < tamano_textbox[0] * 0.9) and 
           (font_size < max_tamano) and
           (altura_texto * font.getsize(tamano_texto)[1]  < tamano_textbox[1] * 0.9)):
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)

    # Reduce el tamaño de la tipografía en una unidad para que se ajuste completamente
    font_size -= 1
    font = ImageFont.truetype(font_path, font_size)

    return font