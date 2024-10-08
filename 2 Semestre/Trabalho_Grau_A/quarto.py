from __future__ import annotations
from produtos import Produtos

class Quartos:
    def __init__(self,numero,categoria,diaria):
        self.__numero = numero
        self.__categoria = categoria
        self.__diaria = diaria
        self.consumo = []

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

    def adiciona_consumo (self,produto_codigo):
        self.consumo.append(produto_codigo)

    def lista_consumo (self):
        print(self.consumo)
        return self.consumo
    
    def valor_total_consumo(self, produtos:Produtos):
        total = 0
        for codigo in self.consumo:
            produto = next((p for p in produtos if p.codigo == codigo), None)
            if produto:
                total += produto.preco
        return total

    def limpa_consumo (self):
        self.consumo = []

    
