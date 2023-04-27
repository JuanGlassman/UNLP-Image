import PySimpleGUI as sg
import addPerfil as perfil
import json
import json, io, os
from PIL import Image

sg.ChangeLookAndFeel('LightGrey4')

lista_fotos = []
lista_nick= []

def convert_to_bytes(file_or_bytes, resize=None):
   img = Image.open(file_or_bytes)
   with io.BytesIO() as bio:
      img.save(bio, format="PNG")
      del img
      return bio.getvalue()


with open("miarchivo.json","r") as file:
    dato = json.load(file)
    lista_fotos.append(dato['image_data'])
    lista_nick.append(dato['Nick'])


def perfiles(lista_fotos):
    botonera = []
    aux = []
    if (len(lista_fotos)!=0):
        for i in range(len(lista_fotos)):
            if (i%4==0):
                botonera.append(aux)
                aux=[]
            aux.append(sg.Button(button_color=('white', 'grey'), image_data=convert_to_bytes(lista_fotos[int(i)]), image_size=(150,150),image_subsample=5,button_text=lista_nick[int(i)], border_width=2))
        if(i%4!=0):
                botonera.append(aux)
        if (len(lista_fotos) > 16):
            botonera.append(sg.Button('Ver Más', size=(15, 2), button_color=('white', 'grey'), font=('Comis Sans MS', 15), key='Ver Más'))
    botonera.append(sg.Button('Agregar Perfil', size=(15, 2), button_color=('white', 'grey'), font=('Comis Sans MS', 15), key='Agregar Perfil'))
    return botonera

boton_cerrar = [[sg.Button('Cerrar',size=(20, 2), button_color=('white', 'grey'), font=('Comis Sans MS', 12))]]


layout = [[[sg.Text('UNLP-Image', size=(50, 2), font=('Comis Sans MS', 50), text_color='Black', justification=("c"))]],
        [perfiles(lista_fotos)],
        [[sg.Column(boton_cerrar, element_justification='rigth', expand_x=True)]]]

window = sg.Window('Inicio', layout, element_justification='c', size=(1920,1080))


while True:
    event,values = window.read()

    if event == ('Cerrar') or event == sg.WIN_CLOSED:
        break 
    if event == ('Agregar Perfil'):
        perfil.agregar_perfil()
    if event == ('Ver Más'):
        print()

window.close()