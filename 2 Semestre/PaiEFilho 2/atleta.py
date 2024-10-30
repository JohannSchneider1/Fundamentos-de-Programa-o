class Atleta():
    def __init__(self,nome:str,idade:int):
        self.__nome = nome
        self.__idade = idade
    
    @property
    def nome (self):
        return self.__nome
    
    @property
    def idade (self):
        return self.__idade
    
    @nome.setter
    def nome (self,nome):
        self.__nome = nome
    
    @idade.setter
    def idade (self,idade):
        self.__idade = idade
    
    def imprime_info (self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')