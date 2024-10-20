import json

from modelos import entidadvineria
from modelos import bodega
from modelos import cepa


class Vino(entidadvineria.EntidadVineria):
    # atributos de clase
    # método de inicialización
    def __init__(self, id: str, nombre: str) -> None:
        # atributos de instancia
        super().__init__(id, nombre)

    # comandos
    def establecerNombre(self,nombre: str) -> None:
        ...
    def establecerBodega(self,bodega: str) -> None:
        ...
    def establecerCepas(self,cepas: list[str]) -> None:
        ...
    def establecerPartidas(self,partidas: list[int]) -> None:
        ...

    # consultas
    def obtenerId(self) -> str:
        ...
    def obtenerNombre(self) -> str:
        ...
    def obtenerBodega(self) -> 'bodega.Bodega':
        ...
    def obtenerCepas(self) -> list['cepa.Cepa']:
        ...
    def obtenerPartidas(self) -> list[int]:
        ...

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

