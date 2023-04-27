import json, io, os
from PIL import Image


ruta_fotos1 = os.path.join(os.getcwd(),"Fotos","gatopng.png")
ruta_fotos2= os.path.join(os.getcwd(),"Fotos","gatopng2.png")
ruta_fotos3= os.path.join(os.getcwd(),"Fotos","perro.jpg")
ruta_fotos4= os.path.join(os.getcwd(),"Fotos","Gato1.jpg")
ruta_fotos5= os.path.join(os.getcwd(),"Fotos","Gato2.jpg")
ruta_fotos12 = os.path.join(os.getcwd(),"Fotos","gatopng.png")
ruta_fotos22= os.path.join(os.getcwd(),"Fotos","gatopng2.png")
ruta_fotos32= os.path.join(os.getcwd(),"Fotos","perro.jpg")
ruta_fotos42= os.path.join(os.getcwd(),"Fotos","Gato1.jpg")
ruta_fotos52= os.path.join(os.getcwd(),"Fotos","Gato2.jpg")
ruta_fotos123 = os.path.join(os.getcwd(),"Fotos","gatopng.png")
ruta_fotos223= os.path.join(os.getcwd(),"Fotos","gatopng2.png")
ruta_fotos323= os.path.join(os.getcwd(),"Fotos","perro.jpg")
ruta_fotos423= os.path.join(os.getcwd(),"Fotos","Gato1.jpg")
ruta_fotos523= os.path.join(os.getcwd(),"Fotos","Gato2.jpg")
ruta_fotos5234= os.path.join(os.getcwd(),"Fotos","Gato2.jpg")

lista_fotos = [ruta_fotos1, ruta_fotos2, ruta_fotos3, ruta_fotos4, ruta_fotos5, ruta_fotos12, ruta_fotos22, ruta_fotos32, ruta_fotos42, ruta_fotos52, ruta_fotos123, ruta_fotos223, ruta_fotos323, ruta_fotos423, ruta_fotos523,ruta_fotos5234]
lista_nick = ["Juan", "Pepe", "Tito", "Raul", "Jorgito", "Lucas", "Nino", "Carlitos", "Nono", "Lulu", "Lucas", "Nino", "Carlitos", "Nono", "Lulu","Pepe"]

with open("miarchivo.json", "w") as j:
   for i in range(len(lista_fotos)):
      data = {"Nick":lista_nick[i], "image_data": lista_fotos[i]}
      json.dump(data, j, indent=2)
