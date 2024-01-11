from typing import Type
from interface.habilidade import Habilidade


class Guerreiro:
    
    def __init__(self, habilidade: Type[Habilidade]):
        self.habilidade = habilidade
    
    def acao(self):
        # Processamento
        self.habilidade.comportamento()
    
    def attributos(self):
        self.habilidade.nivel_atributo()