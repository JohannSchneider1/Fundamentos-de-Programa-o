from funcionario import Funcionario

class Empresa:
    def __init__(self,nome,funcionario1:Funcionario,funcionario2:Funcionario):
        self.__nome = nome
        self.__funcionario1 = funcionario1
        self.__funcionario2 = funcionario2
    
    @property
    def nome (self):
        return self.__nome
    
    @property
    def funcinario1 (self):
        return self.__funcionario1
    
    @property
    def funcionario2 (self):
        return self.__funcionario2
    
    @nome.setter
    def nome (self,nome):
        self.__nome = nome
    
    @funcinario1.setter
    def funcionario1 (self,funcionario1):
        self.__funcionario1 = funcionario1
    
    @funcionario2.setter
    def funcionario2 (self,funcionario2):
        self.__funcionario2 = funcionario2

    def imprime_info(self):
        print('-----------Dados da Empresa-----------')
        print('Dados do primeiro funcinário: ')
        self.funcinario1.imprime_info()
        print('Dados do segundo funcinário: ')
        self.funcionario2.imprime_info()
        print('--------------------------------------')