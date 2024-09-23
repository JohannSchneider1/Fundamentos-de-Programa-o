from pais import Pais

class Continente:

    def __init__ (self,nome):
        self.__nome = nome
        self.__paises: list[Pais] = []
    
    @property
    def nome (self):
        return self.__nome
    
    @property
    def paises (self)->list[Pais]:
        return self.__paises
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    def adiciona_paises(self,pais:Pais):
        self.paises.append(pais)
    
    def dimensao_continente (self):
        total = sum(pais.dimensao for pais in self.paises)
        return total
    
    def populacao_continente(self):
        total = sum(pais.populacao for pais in self.paises)
        return total
    
    def densicade_continente(self):
        total = sum(pais.dencidade() for pais in self.paises)
        return total
    
    def maior_populacoa (self):
        maior = self.paises[0]
        for pais in self.paises:
            if pais.populacao > maior.populacao:
                maior = pais
        
        return maior.nome
    
    def menor_populacao(self):
        menor = self.paises[0]
        for pais in self.paises:
            if pais.populacao < menor.populacao:
                menor = pais
        
        return menor.nome
    
    def maior_dimensao (self):
        maior = self.paises[0]
        for pais in self.paises:
            if pais.dimensao > maior.dimensao:
                maior = pais
        return maior
    
    def menor_dimensao (self):
        menor = self.paises[0]
        for pais in self.paises:
            if pais.dimensao < menor.dimensao:
                menor = pais
        return menor
    
    def divisao_territorial (self):
        return self.maior_dimensao().dimensao/ self.menor_dimensao().dimensao