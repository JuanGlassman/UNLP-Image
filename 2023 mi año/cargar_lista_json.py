import os
import json

def cargar_lista_json(nombre):
    """
    Esta función retorna la lista de datos. Puede devolverla vacia en caso de que el archivo no exista o en el caso de que sea vacío.
    """
    #Se verifica si el archivo existe, si es asi se lo abre en modo lectura. En el case de que el archivo no exista se lo abre en modo escritura y se crea la lista de imagenes vacia.
    if os.path.exists(nombre):
        with open(nombre,'r') as archivo:
            #Se verifica si el archivo esta vacio, si es asi se crea la lista de imagenes vacia. Si el archivo no esta vacio se carga lista_imagenes con los datos.
            if (os.stat(nombre).st_size == 0):
                datos_json=[]
            else:
                datos = json.load(archivo)
                datos_json = list(map(lambda elem : elem,datos))
    else:
        with open(nombre,'w') as archivo:
            datos_json=[]

    return datos_json