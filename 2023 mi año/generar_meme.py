import PySimpleGUI as sg
import os
import io
import configuracion as configuracion
import cargar_lista_json as cargar_lista_json
import ajustar_tamano_tipografia as ajustar_tamano_tipografia
import obtener_imagen_con_texto as obtener_imagen_con_texto
import layout_generar_meme as layout_generar_meme

sg.theme ('LightGrey4')

def window_generar_meme(alias, foto, textbox):
    """
    Retorna la ventana de Generar meme.
    """
    
    text1 = ""
    text2 = ""
    fuente = os.path.join(os.getcwd(),"Tipografias","arial.ttf")

    window = sg.Window('',layout_generar_meme.get_layout(foto), element_justification='c', size=(1366,768), resizable=True)

    while True:
        event,values = window.read()

        if event == ('-VOLVER-') or event == sg.WIN_CLOSED:
            break
        if event == ('-GUARDAR-') or event == sg.WIN_CLOSED: 
            repositorio_memes = ""
            datos_json = cargar_lista_json.cargar_lista_json("directorios.json")
            for dato in datos_json:
                if (dato["Alias"] == alias):
                    repositorio_memes = dato["R_Memes"]
                if (not repositorio_memes):
                    directorios = ""
                    while (not directorios):
                        window.hide()
                        directorios = configuracion.conf(alias)
                        if (not directorios):
                            sg.popup("Se debe cargar el directorio donde se va a guardar el meme.")
                        else:
                            repositorio_memes = directorios["R_Memes"]
                    window.UnHide()
                else:
                    imagen = obtener_imagen_con_texto.obtener(foto, text1, text2, fuente, textbox)
                    imagen.save(os.path.join(repositorio_memes,foto), format='PNG')
                    sg.popup("Se cargó el meme con éxito.")
                    break
            break

        if event == ('-TIPOGRAFIA-'):
            fuente = os.path.join(os.getcwd(),"Tipografias",f"{values['-TIPOGRAFIA-']}.ttf")
        if event == ('-TEXTO1-'):
            text1 = values['-TEXTO1-']
        elif event == ('-TEXTO2-'):
            text2 = values['-TEXTO2-']
        if event == "-VISUALIZAR-":
            #Transformamos la imagen en bytes y la mostramos en pantalla.
            imagen = obtener_imagen_con_texto.obtener(foto, text1, text2, fuente, textbox)
            bio = io.BytesIO()
            imagen.save(bio, format="PNG")
            window["-IMAGE-"].update(size=(400,400),subsample=2 ,data=bio.getvalue())
    window.close()