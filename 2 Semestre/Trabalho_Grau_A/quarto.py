from __future__ import annotations
from produtos import Produtos

class Quarto:
    #criando o objeto Quarto
    def __init__(self, numero, categoria, diaria):
        self.__numero = numero
        self.__categoria = categoria
        self.__diaria = diaria
        self.consumo = []

    #criando get e set
    @property
    def numero (self):
        return self.__numero
    
    @numero.setter
    def numero (self,numero):
        self.numero = numero
    
    @property
    def categoria (self):
        return self.__categoria
    
    @categoria.setter
    def categoria (self,categoria):
        self.__categoria = categoria
    
    @property
    def diaria (self):
        return self.__diaria
    
    @diaria.setter
    def diaria (self,diaria):
        self.__diaria = diaria

    #criando função para adicionar os produtos na lista consumo
    def adiciona_consumo(self, produto_codigo):
        self.consumo.append(produto_codigo)

    #função para retornar a lista de consumo
    def lista_consumo(self):
        return self.consumo

    #Função que retorna o valor total de gastos no consumo
    def valor_total_consumo(self, produtos):
        total = 0
        #varrendo a lista consumo
        for codigo in self.consumo:
            produto = next((p for p in produtos if p.codigo == codigo), None) # esta linha esta percorrendo a lista produtos e esta retornando cada produto onde o codigo é o mesmo,  
                                                                                #mas o next esta para obter apenas o primeiro produto que passa pela condição
            if produto:
                total += produto.preco
        return total

    #fução para limpar o consumo
    def limpa_consumo(self):
        self.consumo = []
    
