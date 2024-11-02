#import json
#import sys
#sys.path.append('/home/mauro-roth/github-project/uner-tudw-programacion2-tpi-vinoteca')
#import modelos.bodega as b

#print(vinoteca.Vinoteca.obtenerTodos())


#with open("vinoteca.json", mode="r", encoding="utf-8") as read_file:
#    json_original = read_file
#    diccionario_datos = json.load(json_original)
#    read_file.close()
#    
#print(diccionario_datos)

#bodega = b.Bodega("25","jeg")
#print(bodega.obtenerVinos())


from vinoteca import Vinoteca

Vinoteca.inicializar()
#list(map(lambda b: print(b.buscarNombre('33ccaa9d-4710-9942-002d-1b5cb9912e5d')),Vinoteca.obtenerCepas()))
#for bodega in Vinoteca.obtenerBodegas():
#    print(bodega.convertirAJSONFull())
for bodega in Vinoteca.obtenerBodegas():
    print(bodega.obtenerVinos())
