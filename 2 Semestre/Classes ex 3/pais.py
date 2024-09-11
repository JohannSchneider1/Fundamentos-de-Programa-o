class Pais:
    def __init__(self,iso,nome,populacao,dimencao):
        self.__iso = iso
        self.__nome = nome
        self.__populacao = populacao
        self.__dimencao = dimencao
        self.__fronteira = []

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
    def dimencao(self):
        return self.__dimencao

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
    
    @dimencao.setter
    def dimencao(self,dimencao):
        self.__dimencao = dimencao
    
    @fronteira.setter
    def fronteira(self,fronteira):
        self.__fronteira = fronteira

    def __eq__ (self,pais1):
        if id(self) == id(pais1):
            return True
        elif self.iso == pais1.iso:
            return True
        else:
            return False
        
    def dencidade (self):
        total = self.populacao / self.dimencao
        return total
    
    def limitrofe (self,pais1):
        for i in self.fronteira:
            if i == pais1:
                return True
            else:
                return False
    
    def vizinhos (self,pais1):
        front = []
        for i in pais1.fronteiras:
            for j in self.fronteira:
                if i == j:
                    front.append(j)
        return front
