class Produtos:
    #criando o objeto Produtos
    def __init__(self,codigo,nome,preco):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.produtos = []

    #criando get e set
    @property
    def codigo (self):
        return self.__codigo
    
    @codigo.setter
    def codigo (self,codigo):
        self.__codigo = codigo
    
    @property
    def nome (self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def preco (self):
        return self.__preco
    
    @preco.setter
    def preco (self,preco):
        self.__preco = preco
    
