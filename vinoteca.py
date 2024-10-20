# librerias
import os
import json

# modelos
from modelos import bodega
from modelos import cepa
from modelos import vino


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
    
    def obtenerBodegas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "vinos":
                pass  # completar
        return Vinoteca.__bodegas

    def obtenerCepas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
        return Vinoteca.__cepas

    def obtenerVinos(anio=None, orden=None, reverso=False):
        if isinstance(anio, int):
            pass  # completar
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "bodega":
                pass  # completar
            elif orden == "cepas":
                pass  # completar
        return Vinoteca.__vinos

    def buscarBodega(id):
        return list(filter(lambda bodega: bodega['id']==id,Vinoteca.__bodegas))

    def buscarCepa(id):
        pass  # completar

    def buscarVino(id):
        pass  # completar

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
