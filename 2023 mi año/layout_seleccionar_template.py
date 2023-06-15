import PySimpleGUI as sg
import abrir_foto_meme_collage as abrir_foto
import os

def get_layout(templates):
    """
    Retorna el layout de seleccionar template.
    """
    boton_volver = [[sg.Button(
        "< Volver", 
        size=(20, 2), 
        button_color=('black', 'skyblue'), 
        font=('Helvetica', 12),
        key='-VOLVER-')]]
    boton_guardar = [[sg.Button(
        'Generar', 
        size=(20, 2), 
        button_color=('black', 'skyblue'), 
        font=('Helvetica', 12),
        key='-GENERAR-')]]
    columna= [sg.Column(
        boton_volver, 
        element_justification='left', 
        expand_x=True),
            sg.Column(
        boton_guardar, 
        element_justification='rigth', 
        expand_x=True)]

    layout = [[sg.Text(
        'Generar Meme', 
        size=(20, 1), 
        font=('Times New Roman', 75), 
        text_color='Black', 
        justification=("c"))],
        [sg.Text(
        'Seleccionar template: ', 
        size=(30, 1), 
        font=('Times New Roman', 15), 
        text_color='Black', 
        justification=('left')),
        sg.Text(
        'Previsualización', 
        size=(30, 1), 
        font=('Times New Roman', 15), 
        text_color='Black', 
        justification=('right'))],
            [sg.Listbox(
        [arc["name"] for arc in templates], 
        enable_events=True, 
        size=(40, 20),
        key="-ARCHIVOS-",
        background_color='skyblue',
        text_color='black',
        sbar_arrow_color='black', 
        sbar_background_color='skyblue', 
        highlight_background_color='steelblue',
        highlight_text_color='white'),
            sg.Image(
        data=abrir_foto.abrir(os.path.join(os.getcwd(),"Fotos","Fondo_Meme.png"),(400,400)),
        key='-IMAGE-')],
            [columna]]
    
    return layout