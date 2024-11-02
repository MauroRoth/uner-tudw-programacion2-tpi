import json
from . import entidadvineria
from . import vino
from . import cepa
import vinoteca

class Bodega(entidadvineria.EntidadVineria):
    # atributos de clase
    # método de inicialización
    def __init__(self, id: str, nombre: str) -> None: # doing
        # atributos de instancia
        super().__init__(id, nombre)
    
    # comandos
    # consultas
    def obtenerVinos(self) -> list['vino.Vino']: # doing
        vinos = vinoteca.Vinoteca.obtenerVinos()
        vinos_bodega = list()
        for vino in vinos:
            if self._id == vino.obtenerBodega().obtenerId():
                vinos_bodega.append(vino)
        return vinos_bodega
    
    def __mapearVinos(self) -> list[str]:
        vinos = self.obtenerVinos()
        nombre_vinos_bodega = map(lambda v: v.obtenerNombre(),filter(lambda v: v.obtenerBodega().obtenerId()==self.obtenerId(), vinos))
        return list(nombre_vinos_bodega)
    
    def obtenerCepas(self) -> list['cepa.Cepa']:
        vinos_bodega = self.obtenerVinos()
        cepas_bodega = list()
        for vino in vinos_bodega:
            for cepa in vino.obtenerCepas():
                if cepa not in cepas_bodega:
                    cepas_bodega.append(cepa)
        return cepas_bodega
    
    def __mapearCepas(self) -> list[str]:
        vinos_bodega = self.obtenerVinos()
        cepas_bodega = list()
        for vino in vinos_bodega:
            for cepa in vino.obtenerCepas():
                if cepa.obtenerNombre() not in cepas_bodega:
                    cepas_bodega.append(cepa.obtenerNombre())
        return cepas_bodega  
    
    def convertirAJSON(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "cantidad vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }
        
    def __repr__(self):
        return json.dumps(self.convertirAJSON())