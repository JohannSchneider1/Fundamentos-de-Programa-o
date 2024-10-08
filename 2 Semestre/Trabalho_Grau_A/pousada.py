from __future__ import annotations
from produtos import Produtos
from quarto import Quartos
from reserva import Reserva
import os

class Pousada :
    def __init__(self,nome,contato):
        self.__nome = nome
        self.__contato = contato
        self.quartos = []
        self.reservas = []
        self.produtos = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def contato (self):
        return self.__contato
    
    @contato.setter
    def contato(self,contato):
        self.__contato = contato

    def carrega_dados (self):
        #carrega produtos
        prod = open('produtos.txt','r')
        leitura = prod.read().strip().split('\t')
        prod.close()
        if len(leitura) == 3:
            codigo = int(leitura[0])
            nome = leitura[1]
            preco = float(leitura[2])
            self.produtos.append(Produtos(codigo,nome,preco))
        
        #carrega quartos
        quar = open('quartos.txt','r')
        leitura = quar.read().strip().split('\t')
        quar.close()
        if len(leitura) == 3:
            numero = int(leitura[0])
            categoria = leitura[1]
            diaria = float(leitura[2])
            self.quartos.append(Quartos(numero,categoria,diaria))
        
        #carrega reservas
        reser = open('reserva.txt','r')
        leitura = reser.read().strip().split('\t')
        reser.close()
        if len(leitura) == 5:
            dia_inicio = int(leitura[0])
            dia_fim = int(leitura[1])
            cliente = leitura[2]
            quarto_numero = int(leitura[3])
            status = leitura [4]
            quarto = next((i for i in self.quartos if i.numero == quarto_numero),None)
            if quarto:
                self.reservas.append(Reserva(dia_inicio,dia_fim,cliente,quarto,status))
            
        print('Dados carregados:\n', len(self.produtos), 'produtos\n', len(self.quartos), 'quartos\n', len(self.reservas), 'reservas.')
    
    def salva_dados (self):
        #salvando os produtos
        with open('produtos.txt','w')as texto:
            for produto in self.produtos:
                texto.write(produto.codigo,'\t',produto.nome,'\t','{:.2f}'.format(produto.preco),'\n')
        
        #salvando os quartos
        with open('quartos.txt','w')as texto:
            for quarto in self.quartos:
                texto.write(quarto.numero,'\t',quarto.categoria,'\t','{:.2f}'.format(quarto.diaria),'\n')
