import PySimpleGUI as sg
import os
from PIL import Image

lista_perfiles=[]
sg.ChangeLookAndFeel('LightGrey4')

ruta_fotos1 = os.path.join(os.getcwd(),"Fotos","gatopng.png")
ruta_fotos2= os.path.join(os.getcwd(),"Fotos","gatopng2.png")
ruta_fotos3= os.path.join(os.getcwd(),"Fotos","gatotriste.png")

lista_fotos = [ruta_fotos1, ruta_fotos2, ruta_fotos3]


layout = [[sg.Text('UNLP-Image', size=(50, 2), font=('Times New Roman', 20), text_color='Black', justification=("left"))],
          [sg.Button('Agregar perfil', size=(20, 2), button_color=('white', 'grey'), font=('Helvetica', 12), image_filename=lista_fotos[0], image_size=(100,100)), 
           sg.Button('Mostrar datos', size=(20, 2), button_color=('white', 'grey'), font=('Helvetica', 12), image_filename=lista_fotos[1], image_size=(100,100))], 
           [sg.Button('Cerrar',size=(20, 2), button_color=('white', 'grey'), font=('Helvetica', 12), image_filename=lista_fotos[2], image_size=(100,100))]]

window = sg.Window('Inicio', layout, element_justification='c')

while True:
    event,values = window.read()

    if event == ('Cerrar') or event == sg.WIN_CLOSED:
        break
window.close()