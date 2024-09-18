class Pessoa:
    def __init__ (self,nome,idade,altura,peso):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__peso = peso

    @property
    def nome (self):
        return self.__nome
    
    @property
    def idade (self):
        return self.__idade
    
    @property
    def altura (self):
        return self.__altura
    
    @property
    def peso (self):
        return self.__peso
    
    @nome.setter
    def nome (self,nome):
        self.__nome = nome
    
    @idade.setter
    def idade (self,idade):
        self.__idade = idade
    
    @altura.setter
    def altura(self,altura):
        self.__altura = altura

    @peso.setter
    def peso(self,peso):
        self.__peso = peso
    
    def visualizar(self):  

        print('Nome: ',self.nome)
        print('Idade: ',self.idade)
        print('Altura: ',self.altura)
        print('Peso: ',self.peso)