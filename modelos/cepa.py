import json
import modelos.vino as v
from .entidadvineria import EntidadVineria
import vinoteca

class Cepa(EntidadVineria):
    # atributos de clase
    # método de inicialización
    def __init__(self, id: str, nombre: str) -> None:
        # atributos de instancia
        super().__init__(id, nombre)

    # comandos
    # consultas
    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})
    
    def obtenerVinos(self) -> list[v.Vino]:
        vinos = vinoteca.Vinoteca.obtenerVinos()
        vinos_bodega = list(filter(lambda x: x["bodega"]==self._id,vinos))
        return vinos_bodega

    def convertirAJSON(self) -> dict:
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)
