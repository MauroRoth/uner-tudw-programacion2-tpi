from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    # atributos de clases
    # método de inicialización
    @abstractmethod
    def __init__(self,id:str, nombre:str) -> None:
        # atributos de instancia
        super().__init__()
        self._id = id
        self._nombre = nombre
   
    # comandos
    def establecerNombre(self, nombre:str) -> None:
        self._nombre = nombre

    # consultas 
    def obtenerId(self) -> str:
        return self._id
    
    def obtenerNombre(self) -> str:
        return self._nombre

    #@abstractmethod
    def __eq__(self, entidadvineria: 'EntidadVineria') -> bool: 
        eq = self._id == entidadvineria.obtenerId()
        return eq

