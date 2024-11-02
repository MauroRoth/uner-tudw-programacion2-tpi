import json
from . import entidadvineria as ev
from . import bodega as b
from . import cepa as c


class Vino(ev.EntidadVineria):
    # atributos de clase
    # método de inicialización
    def __init__(self, id: str, nombre: str, bodega: 'b.Bodega', cepas: list['c.Cepa'], partidas:list[int]) -> None:
        # atributos de instancia
        super().__init__(id, nombre)
        self.__bodega: 'b.Bodega' = bodega
        self.__cepas: 'list[c.Cepa]' = cepas
        self.__partidas: list[int] = partidas

    # comandos
    def establecerBodega(self,bodega: 'b.Bodega') -> None:
        self.__bodega = bodega

    def establecerCepas(self,cepas: list['c.Cepa']) -> None:
        self.__cepas = cepas

    def establecerPartidas(self,partidas: list[int]) -> None:
        self.__partidas = partidas

    # consultas
    def obtenerBodega(self) -> 'b.Bodega':
        return self.__bodega
    
    def obtenerCepas(self) -> list['c.Cepa']:
        return self.__cepas
    
    def __mapearCepas(self) -> list[str]:
        cepas = self.obtenerCepas()
        nombres_cepas_vino = map(lambda c: c.obtenerNombre(),cepas)
        return list(nombres_cepas_vino)
    
    def obtenerPartidas(self) -> list[int]:
        return self.__partidas

    def convertirAJSON(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cantidad_cepas": len(self.obtenerCepas()),
            "cantidad_partidas": len(self.obtenerPartidas()),
        }

    def convertirAJSONFull(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }
    
    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})