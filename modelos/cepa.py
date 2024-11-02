import json
from . import entidadvineria
from . import vino
import vinoteca

class Cepa(entidadvineria.EntidadVineria):
    # atributos de clase
    # método de inicialización
    def __init__(self, id: str, nombre: str) -> None:
        # atributos de instancia
        super().__init__(id, nombre)

    # comandos
    # consultas
    def obtenerVinos(self) -> list['vino.Vino']:
        vinos = vinoteca.Vinoteca.obtenerVinos()
        vinos_cepa = list()
        for vino in vinos:
            for cepa in vino.obtenerCepas():
                if self._id == cepa.obtenerId():
                    vinos_cepa.append(vino)
        return vinos_cepa
    
    def __mapearVinos(self):
            vinos_cepa = self.obtenerVinos()
            vinosMapa = map(
                lambda v: (v.obtenerNombre()
                + " ("
                + v.obtenerBodega().obtenerNombre()
                + ")"),
                vinos_cepa)
            return list(vinosMapa)
            
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

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})
        
