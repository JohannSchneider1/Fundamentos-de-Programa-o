from atleta import Atleta
from competicao import Competicao

class Corredor (Atleta):
    def __init__(self, nome: str, idade: int,peso:int,competicao:Competicao):
        super().__init__(nome, idade)
        self.__peso = peso
        self.__competicao = competicao
    
    @property
    def peso (self):
        return self.__peso
    
    @property
    def competicao (self):
        return self.__competicao
    
    @peso.setter
    def peso (self,peso):
        self.__peso = peso
    
    @competicao.setter
    def competicao (self,competicao):
        self.__competicao = competicao
    
    def imprime_competicao (self):
        self.competicao.imprime_info()
    
    def imprime_info(self):
        super().imprime_info()
        print(f'Peso: {self.peso}')
        self.imprime_competicao()
