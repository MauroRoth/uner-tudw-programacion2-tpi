# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:
    # atributos de clase
    __archivoDeDatos = "vinoteca.json"
    __todos: dict = {}
    __bodegas: list = []
    __cepas: list = []
    __vinos: list = []

    # sin atributos de instancia

    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)
        
    def obtenerTodos():
        return Vinoteca.__todos
    
    def obtenerBodegas(orden=None, reverso=False) -> list[Bodega]:
        bodegas: list[Bodega] = list()
        for bodega in Vinoteca.__bodegas:
            bodegas.append(Bodega(bodega['id'],bodega['nombre']))
        if (isinstance(orden, str) and isinstance(reverso, bool)):
            if orden == "nombre":
                bodegas = sorted(bodegas,key=lambda b:b.obtenerNombre(),reverse=reverso)
            #elif orden == "vinos": # ver si esto corresponde, el orden según vinos, para mí no
            #    pass  # completar
        return bodegas

    def obtenerCepas(orden=None, reverso=False):
        cepas: list[Cepa] = list()
        for cepa in Vinoteca.__cepas:
            cepas.append(Cepa(cepa['id'],cepa['nombre']))
        if (isinstance(orden, str) and isinstance(reverso, bool)):
            if orden == "nombre":
                cepas = sorted(cepas,key=lambda c:c.obtenerNombre(),reverse=reverso)
        return cepas

    def obtenerVinos(anio=None, orden=None, reverso=False) -> list[Vino]:
        vinos: list[Vino] = list()
        for vino in Vinoteca.__vinos:
            bodega = Vinoteca.buscarBodega(vino['bodega'])
            cepas = list(map(lambda c: Vinoteca.buscarCepa(c),vino['cepas']))
            vinos.append(Vino(vino['id'],vino['nombre'],bodega,cepas,vino['partidas']))
        if isinstance(anio, int):
            vinos = list(filter(lambda v: anio in v.obtenerPartidas(),vinos))
        if isinstance(orden, str) and isinstance(reverso, bool):
            if orden == "nombre":
                vinos = sorted(vinos,key=lambda v:v.obtenerNombre(),reverse=reverso)
            elif orden == "bodega":
                vinos = sorted(vinos,key=lambda v:v.obtenerBodega().obtenerNombre(),reverse=reverso)
            elif orden == "cepas":
                vinos = sorted(vinos,key=lambda v:v.obtenerCepas()[1].obtenerNombre(),reverse=reverso)
                # revisar tema orden de los vinos según orden de las cepas, ya que son varias cepas.
        return vinos

    def buscarBodega(id) -> 'Bodega':
        for bodega in Vinoteca.__bodegas:
            if bodega['id'] == id:
                bodega_encontrada = Bodega(bodega['id'],bodega['nombre'])
        return bodega_encontrada

    def buscarCepa(id):
        for cepa in Vinoteca.__cepas:
            if cepa['id'] == id:
                cepa_encontrada = Cepa(cepa['id'],cepa['nombre'])
        return cepa_encontrada

    def buscarVino(id):
        for vino in Vinoteca.__vinos:
            if vino['id'] == id:
                bodega = Vinoteca.buscarBodega(vino['bodega'])
                cepas = list(map(lambda c: Vinoteca.buscarCepa(c),vino['cepas']))
                vino_encontrado = Vino(vino['id'],vino['nombre'],bodega,cepas,vino['partidas'])
        return vino_encontrado

    def __parsearArchivoDeDatos() -> dict:
        with open(Vinoteca.__archivoDeDatos, mode="r", encoding="utf-8") as read_file:         
            dicc_datos = json.load(read_file)
            read_file.close()
        return dicc_datos
            
    def __convertirJsonAListas(dicc_datos) -> None:
       Vinoteca.__todos = dicc_datos
       Vinoteca.__bodegas = dicc_datos["bodegas"]
       Vinoteca.__cepas = dicc_datos["cepas"]
       Vinoteca.__vinos = dicc_datos["vinos"] 
