from data import Data

class Competicao:
    def __init__(self,nome:str,data:Data):
        self.__nome = nome
        self.__data = data

    @property
    def nome (self):
        return self.__nome
    
    @property
    def data (self):
        return self.__data
    
    @nome.setter
    def nome (self,nome):
        self.__nome = nome
    
    @data.setter
    def data (self,data):
        self.__data = data
    
    def imprime_info (self):
        print(f'{self.nome}')
        self.data.imprime_data()