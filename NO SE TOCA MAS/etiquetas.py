import PySimpleGUI as sg
import os.path
from PySimpleGUI.PySimpleGUI import FolderBrowse, Listbox
import io
from PIL import Image

#Se crea esta función para poder abrir las fotos en formatos diferentes al png convirtiendolos en bytes.
def abrir_foto(ruta_foto):
    """
    Se abre la foto desde la ruta (que debe ser pasada por parametro) solo para lectura en formato binario, de esa manera obteniendo los bytes respectivos de la imagen y 
    utilizando el PIL se lee y se la reacomoda en un tamaño de 200x200, guardandandola y enviando a traves del return los bytes de la imagen.
"""
    with open(ruta_foto, 'rb') as file:
        img_bytes = file.read()
        image = Image.open(io.BytesIO(img_bytes))
        image.thumbnail((300, 300))
        bio = io.BytesIO()
        image.save(bio, format='PNG')
    return bio.getvalue()

sg.theme('LightGrey4')
def eti():
    #Usamos variables locales hasta implementar bien el funcionamiento interno
    etiquetas = []
    descripcion = ''

    columna_izquierda = [
        [sg.Text("Directorio de imágenes"),sg.In(size=(25, 1), enable_events=True, key="-CARPETA-"),
         sg.FolderBrowse('Buscar')],
        [sg.Text("Etiquetar imagen"),sg.In(size=(25, 1), enable_events=True, key="-ETIQUETAR TEXT-"),
         sg.Button('Etiquetar', key="-ETIQUETAR-")],
        [sg.Text("Agregar descripcion"),sg.In(size=(25, 1), enable_events=True, key="-DESCRIBIR TEXT-"),
         sg.Button('Modificar', key="-DESCRIBIR-")],
        [sg.Listbox(values=[], enable_events=True, size=(40, 20),key="-ARCHIVOS-")]
    ]

    
    ruta_foto = os.path.join(os.getcwd(),"Fotos","Fondo_Meme.png")

    columna_derecha = [
        [sg.Text(size=(100,1), key="-DESCRIPCION-")],
        [sg.Image(data=abrir_foto(ruta_foto),key="-IMAGEN-")],
        [sg.Text(size=(200,2), key="-ETIQUETAS-")],
        [sg.Text('')]
    ]

    boton_volver = [[sg.Button("< Volver", size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12),key='volver')]]
    boton_guardar = [[sg.Button('Guardar', size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12))]]

    columna= [sg.Column(boton_volver, element_justification='left', expand_x=True),
            sg.Column(boton_guardar, element_justification='rigth', expand_x=True)]
    
    layout = [
        [sg.Text("Etiquetar imagenes", text_color='Black',font=('Comic Sans MS',30), size=(30,0), justification='l', pad=(10,10))], 
        [sg.Column(columna_izquierda),sg.Column(columna_derecha)],
        [columna]
    ]

    window = sg.Window("Etiquetas", layout, size=(1366,768), resizable=True)

    while True:
        event, values = window.read()
        if event == "volver" or event == sg.WIN_CLOSED:
            break
        if event == "-CARPETA-":
            ruta_carpeta = values["-CARPETA-"]
            try:
                file_list = os.listdir(ruta_carpeta)
            except:
                file_list =[]
            
            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(ruta_carpeta, f))
                and f.lower().endswith((".png",".gif"))
            ]
            window["-ARCHIVOS-"].update(fnames)
        elif event == "-ARCHIVOS-":
            try:
                filename = os.path.join(
                    values["-CARPETA-"], values["-ARCHIVOS-"][0]
                )
                window["-IMAGEN-"].update(data=abrir_foto(filename))
            except:
                pass
        if event=='-DESCRIBIR-':
            descripcion = values['-DESCRIBIR TEXT-']
            window["-DESCRIPCION-"].update(descripcion)
        if event=='-ETIQUETAR-':
            etiquetas.append(values['-ETIQUETAR TEXT-'])
            window["-ETIQUETAS-"].update(" #".join(map(str, etiquetas)))

    window.close()