from __future__ import annotations

class Pais:
    def __init__(self,iso:str,nome,populacao:int,dimensao):
        self.__iso = iso
        self.__nome = nome
        self.__populacao = populacao
        self.__dimensao = dimensao
        self.__fronteira: list[Pais] = []

    @property
    def iso(self):
        return self.__iso

    @property
    def nome(self):
        return self.__nome

    @property
    def populacao(self):
        return self.__populacao

    @property
    def dimensao(self):
        return self.__dimensao

    @property
    def fronteira (self):
        return self.__fronteira
    
    @iso.setter
    def iso (self,iso):
        self.__iso = iso

    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @populacao.setter
    def populacao(self,populacao):
        self.__populacao = populacao
    
    @dimensao.setter
    def dimensao(self,dimensao):
        self.__dimensao = dimensao
    
    @fronteira.setter
    def fronteira(self,fronteira):
        self.__fronteira = fronteira

    def adiciona_fronteira (self,pais: Pais): 
        self.fronteira.append(pais)

    def __eq__ (self,pais1: Pais)->bool:

        if not isinstance(pais1, Pais): #Garante que pais1 é um objeto da classe Pais. Se não for, retorna False.
            return False
        elif self.iso == pais1.iso:
            return True
        else:
            return False
        
    def dencidade (self):
        total = self.populacao / self.dimensao
        return total
    
    
    def limitrofe(self, pais1: Pais):
        if pais1 in self.fronteira:
            print('O País:', pais1.nome, 'é limítrofe de', self.nome)
        else:
            print('O País:', pais1.nome, 'não é limítrofe de', self.nome)
            
    
    def vizinhos (self,pais1:Pais):
        front = []
        for i in pais1.fronteira:
            for j in self.fronteira:
                if i == j:
                    front.append(j)
        return front
