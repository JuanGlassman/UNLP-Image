import PySimpleGUI as sg
import os
import io
from PIL import Image

#Color de fondo
sg.theme('LightGrey4')

def coll():
    def abrir_foto(ruta_foto):
        with open(ruta_foto, 'rb') as file:
            img_bytes = file.read()
            image = Image.open(io.BytesIO(img_bytes))
            image.thumbnail((200, 200))
            bio = io.BytesIO()
            image.save(bio, format='PNG')
        return bio.getvalue()
    ruta_fotos1 = os.path.join(os.getcwd(),"Fotos","amorpopup.png")
    ruta_fotos2 = os.path.join(os.getcwd(),"Fotos","naturalezapopup.png")
    ruta_fotos3 = os.path.join(os.getcwd(),"Fotos","cienciapopup.png")
    ruta_fotos4 = os.path.join(os.getcwd(),"Fotos","genericopopup.png")
    ruta_fotos5 = os.path.join(os.getcwd(),"Fotos","familiapopup.png")
    ruta_fotos6 = os.path.join(os.getcwd(),"Fotos","aydpopup.png")
    
    #Layout para acomodar el boton de salir
    
    columna1 = sg.Column ([[sg.Button(key ='amor', button_color=('LightGrey', 'grey'),image_data=abrir_foto(ruta_fotos1),border_width=0,image_size=(150,200), image_subsample=1), 
            sg.Button(key ='naturaleza', button_color=('LightGrey', 'grey'), image_data=abrir_foto(ruta_fotos2),border_width=0,image_size=(150,200),image_subsample=1),
            sg.Button(key ='ciencia', button_color=('LightGrey', 'grey'), image_data=abrir_foto(ruta_fotos3),border_width=0,image_size=(150,200),image_subsample=1)]], 
            element_justification='c')
    columna3 = sg.Column([[sg.Button(key ='familia', button_color=('LightGrey', 'grey'), image_data=abrir_foto(ruta_fotos5),border_width=0,image_size=(150,200),image_subsample=1), 
            sg.Button(key ='ayd', button_color=('LightGrey', 'grey'), image_data=abrir_foto(ruta_fotos6),border_width=0,image_size=(150,200),image_subsample=1),
            sg.Button(key ='generico', button_color=('LightGrey', 'grey'), image_data=abrir_foto(ruta_fotos4),border_width=0,image_size=(150,200),image_subsample=1)]],
            element_justification='c')
    columna4= sg.Column([[ sg.Button("Salir",  size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12), key='salir')]],
            element_justification='c')

    layout = [[sg.Text("Generar collage", font=('Times New Roman', 50), text_color='Black', justification=("c"),size=(20, 1))],
              [sg.Text('')],
              [sg.Text('')],
              [columna1],

              [columna3],
              [sg.Text('')],
              [sg.Text('')],
              [columna4]]
    
    window = sg.Window('',layout, element_justification='c', size=(1366,768), resizable=True)

    while True:
        event, values = window.read()
        if ((event == sg.WIN_CLOSED) or (event == "salir")):
            break
        if event == "amor":
            sg.popup(image=ruta_fotos1)
        if event == "naturaleza":
            sg.popup(image=ruta_fotos2)
        if event == "ciencia":
            sg.popup(image=ruta_fotos3)
        if event == "generico":
            sg.popup(image=ruta_fotos4)
        if event == "familia":
            sg.popup(image=ruta_fotos5)
        if event == "ayd":
            sg.popup(image=ruta_fotos6)
            
    window.close()
