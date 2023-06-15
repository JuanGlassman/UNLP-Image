import PySimpleGUI as sg
import os
import generar_meme as generar_meme
import cargar_lista_json as cargar_lista_json
import abrir_foto_meme_collage as abrir_foto
import layout_seleccionar_template as layout_seleccionar_template
sg.theme ('LightGrey4')


def window_seleccionar_template(alias):
    """
    Mustra la ventana de seleccionar_template.
    """

    #Cargamos los templates en una variable.
    templates = cargar_lista_json.cargar_lista_json("template.json")

    window = sg.Window('',layout_seleccionar_template.get_layout(templates), element_justification='c', size=(1366,768), resizable=True )

    while True:
        event,values = window.read()

        if event == ("-VOLVER-") or event == sg.WIN_CLOSED:
            break
        
        if event == "-ARCHIVOS-":
            #Seleccionamos un archivo de la lista y lo mostramos.
            try:
                #Buscamos la información de la foto en el archivo de templates.
                for arc in templates:
                    if (arc['name'] == values["-ARCHIVOS-"][0]):
                        datos = arc
                #Mostramos en panalla el meme seleccionado.
                meme_seleccionado = abrir_foto.abrir(os.path.join(os.getcwd(),"Fotos",datos["image"]),(400,400))
                window["-IMAGE-"].update(data=meme_seleccionado)
            except:
                pass
        if event == "-GENERAR-":
            if (values["-ARCHIVOS-"] != []):
                window.Hide()
                #Buscamos la información de la foto en el archivo de templates.
                for arc in templates:
                    if (arc['name'] == values["-ARCHIVOS-"][0]):
                        datos = arc
                textbox = (datos["text_boxes"])
                generar_meme.window_generar_meme(alias, datos["image"],textbox)
                window.UnHide()
    window.close()