from abc import ABC, abstractclassmethod

class Habilidade(ABC):

    @abstractclassmethod
    def comportamento(self):
        pass
    
    @abstractclassmethod
    def nivel_atributo(self):
        pass