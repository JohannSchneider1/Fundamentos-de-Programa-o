from atleta import Atleta

class Nadador(Atleta):
    def __init__(self, nome: str, idade: int,categoria:str):
        super().__init__(nome, idade)
        self.__categoria = categoria
    
    @property
    def categoria (self):
        return self.__categoria
    
    @categoria.setter
    def categoria (self,categoria):
        self.__categoria = categoria
    
    def imprime_info(self):
        super().imprime_info()
        print(f'{self.categoria}')