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
    
    def obtnerNombre(self) -> str:
        return self._nombre

    #@abstractmethod
    def __eq__(self, value: object) -> bool: # todo
        # Se debe sobreescribir la consulta __eq__ 
        # para que compare dos objetos
        # de la clase por el atributo de instancia id.
        return super().__eq__(value)

