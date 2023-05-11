import PySimpleGUI as sg
import os,io
import json
from PIL import Image

datos =[]

def agregar_perfil():
    global datos
    #imagen predeterminada
    ruta_imagen = os.path.join(os.getcwd(),"Fotos","usuario.png")
    
    #si el archivo esta vacio da error el json.load
    if os.path.getsize('perfiles.json') > 0:
        with open('perfiles.json') as archivo:
            datos = json.load(archivo)

    boton_volver = [[sg.Button("< Volver", size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12),key='volver')]]
    boton_guardar = [[sg.Button('Guardar', size=(20, 2), button_color=('black', 'skyblue'), font=('Helvetica', 12))]]
    columna= [sg.Column(boton_volver, element_justification='left', expand_x=True),
              sg.Column(boton_guardar, element_justification='rigth', expand_x=True)]
                                  

    #layout
    layout = [[sg.Text('Nuevo Perfil', size=(20, 1), font=('Times New Roman', 75), text_color='Black', justification=("c"))],
          [sg.Text('Nick o alias', size=(20, 1), font=('Times New Roman', 25), text_color='Black', justification=("c"))],
          [sg.InputText(background_color='skyblue', size=(50,1), font=('Helvetica', 10))],
          [sg.Text('Nombre',size=(20, 1), font=('Times New Roman', 25), text_color='Black', justification=("c"))],
          [sg.InputText(background_color='skyblue', size=(50,1), font=('Helvetica', 10))],
          [sg.Text('Edad',size=(20, 1), font=('Times New Roman', 25), text_color='Black', justification=("c"))],
          [sg.Input(background_color='skyblue', size=(50,1), font=('Helvetica', 10))],
          [sg.Text('Genero autopercibido',size=(20, 1), font=('Times New Roman', 25), text_color='Black', justification=("c"))],
          [sg.Combo(['Masculino','Femenino','Otro'],default_value='Selecciona una opcion',key='Genero',size=(50,1),readonly=True,background_color='skyblue',font=('Helvetica', 10),button_arrow_color=('black'))], #combo es una lista desplegable
          [sg.Image(ruta_imagen,size=(150,150), key='-AVATAR_IMAGE-',subsample=10)],
          [sg.Button("Seleccionar avatar",key='-AVATAR-',button_color=('black', 'skyblue'), font=('Helvetica', 12))],
          [columna]]
    
    window= sg.Window("Crear nuevo perfil",layout, element_justification='c', size=(1366,768), resizable=True )
    
    while True:
        event,values = window.read()

        #cambio de imagen de usuario
        if event == '-AVATAR-':
            ruta_imagen = sg.popup_get_file('Seleccionar avatar', no_window=True, file_types=(('Imagenes', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff'),))
            print(ruta_imagen)
            print('()')
            if not ruta_imagen:
                ruta_imagen = os.path.join(os.getcwd(),"Fotos","usuario.png")
            elif ruta_imagen:
                try:
                    with open(ruta_imagen, 'rb') as file:
                        img_bytes = file.read()
                        image = Image.open(io.BytesIO(img_bytes))
                        image.thumbnail((150, 150))
                        bio = io.BytesIO()
                        image.save(bio, format='PNG')
                        window['-AVATAR_IMAGE-'].update(data=bio.getvalue())

                except Exception as e:
                    sg.popup_error(f'Error al cargar la imagen: {e}')
        #cerrado
        if event=="CANCELAR" or event== sg.WINDOW_CLOSED or event == "volver":
            break

        #guardado del perfil
        if event=='Guardar':

            #verificacion campos completos
            if any(len(values[key]) == 0 for key in values) or values['Genero'] == 'Selecciona una opcion':
                sg.popup('Por favor complete todos los campos.')
                continue
            alias = values[0]
            nombre=values[1]

            #verificacion edad sea un entero
            while True:
                try:
                    edad = int(values[2])
                    break
                except ValueError:
                    sg.popup('Por favor ingrese un número entero válido para la edad.')
                    event, values = window.read()#se declara de vuelta para que lea el nuevo valor de edad ingresado
                    continue
            foto = ruta_imagen

            #como guardar el genero
            if values['Genero'] == 'Otro':
                genero = sg.popup_get_text("Complete manualmente su genero")
            else:
                genero = values['Genero']

            #guardado de datos
            datos.append({"Nombre": nombre,"Edad": edad,"Alias":alias,"Genero":genero,"Foto":foto})

            #verificar alias unico
            if alias in [d["Alias"] for d in datos[:-1]]:
                while True:
                   nuevo_alias = sg.popup_get_text("Ese alias ya existe, ingrese otro")
                   if nuevo_alias is None or nuevo_alias == '':
                        break
                   elif nuevo_alias not in datos:
                        datos[-1]['Alias'] = nuevo_alias
                        break
            #agregar al archivo JSON
            with open('perfiles.json','w') as archivo:
                json.dump(datos,archivo,indent= 2)
                archivo.write('\n') # se agrega un salto de línea para escribir la siguiente lista en la siguiente línea
            sg.popup('Perfil creado con éxito')         
            break
    window.close()
    #verifica si el usuario no apreto volver y no cargo ningun dato.
    if(datos!=[]):
        return datos[-1]
