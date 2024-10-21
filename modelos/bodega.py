import json

from modelos import entidadvineria
from modelos import vino
from modelos import cepa
import vinoteca

class Bodega(entidadvineria.EntidadVineria):
    # atributos de clase
    # método de inicialización
    def __init__(self, id: str, nombre: str) -> None: # doing
        # atributos de instancia
        super().__init__(id, nombre)
    
    # comandos
    # consultas
    def obtenerNombre(self) -> str:
        return super().obtenerNombre()
    
    def obtenerVinos(self) -> list['vino.Vino']: # doing
        vinos = vinoteca.Vinoteca.obtenerVinos()
        vinos_bodega = list()
        for vino in vinos:
            if self._id == vino.obtenerBodega().obtenerId():
                vinos_bodega.append(vino)
        #vinos_cepa = list(filter(lambda c: c.obtenerID()==self._id,map(lambda v: v.obtenerCepas(),vinos)))
        return vinos_bodega
    

    # def obtenerCepas(self) -> list['cepa.Cepa']:
    #     cepas = vinoteca.Vinoteca.obtenerCepas()
    #     return cepas
        
    # def __repr__(self):
    #     return json.dumps(self.convertirAJSON())

    def convertirAdicc(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            #"cepas": self.__mapearCepas(),
            #"vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        #cepas = map(lambda v: v.obtenerCepas(),self.obtenerVinos())
        vinos = self.obtenerVinos()
        cepas_bodega = list()
        for vino in vinos:
            for cepa in vino.obtenerCepas():
                if cepa.obtenerNombre() not in cepas_bodega:
                    cepas_bodega.append(cepa.obtenerNombre())
        return cepas_bodega
        #cepasMapa = map(lambda c: c.obte, cepas)
        #return list(cepas)
        

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinos_bodega = map(lambda v: v.obtenerNombre(),filter(lambda v: v.obtenerBodega().obtenerId()==self.obtenerId(), vinos))
        return list(vinos_bodega)
        
