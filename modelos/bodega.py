import json

from .entidadvineria import EntidadVineria
from .vino import Vino
from .cepa import Cepa
import vinoteca

class Bodega(EntidadVineria):
    # atributos de clase
    # método de inicialización
    def __init__(self, id: str, nombre: str) -> None: # doing
        # atributos de instancia
        super().__init__(id, nombre)
    
    # comandos
    # consultas
    def obtenerVinos(self) -> list[Vino]: # doing
        vinos = vinoteca.Vinoteca.obtenerVinos()
        vinos_bodega = list(filter(lambda x: x["bodega"]==self._id,vinos))
        return vinos_bodega
    

    def obtenerCepas() -> list[Cepa]:
        #cepas = Vinoteca.obtenerCepas()
        #return cepas
        ...

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)
