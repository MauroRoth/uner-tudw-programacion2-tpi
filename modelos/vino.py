import json

from modelos import entidadvineria
from modelos import bodega
from modelos import cepa


class Vino(entidadvineria.EntidadVineria):
    # atributos de clase
    # método de inicialización
    def __init__(self, id: str, nombre: str, bodega: 'bodega.Bodega', cepas: 'list[cepa.Cepa]', partidas:list[int]) -> None:
        # atributos de instancia
        super().__init__(id, nombre)
        self.__bodega: 'bodega.Bodega' = bodega
        self.__cepas: 'list[cepa.Cepa]' = cepas
        self.__partidas: list[int] = partidas


    # comandos
    def establecerNombre(self,nombre: str) -> None:
        self._nombre = nombre

    def establecerBodega(self,bodega: str) -> None:
        self.__bodega = bodega

    def establecerCepas(self,cepas: list[cepa.Cepa]) -> None:
        self.__cepas = cepas

    def establecerPartidas(self,partidas: list[int]) -> None:
        self.__partidas = partidas

    # consultas
    
    def obtenerBodega(self) -> 'bodega.Bodega':
        return self.__bodega
    
    def obtenerCepas(self) -> list[cepa.Cepa]:
        return self.__cepas
    
    def obtenerPartidas(self) -> list[int]:
        return self.__partidas

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAdicc(self):
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
        cepas_vino = map(lambda c: c.obtenerNombre(),cepas)
        return list(cepas_vino)
        
       
        
