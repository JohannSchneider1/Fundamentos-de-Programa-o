import csv

class Biblioteca:
    def __init__(self,nlivro,nautor,editora,quantidade):
        self.__nlivro = nlivro
        self.__nautor = nautor
        self.__editora = editora
        self.__quantidade = quantidade

    @property
    def nlivro (self):
        return self.__nlivro
    
    @property
    def nautor (self):
        return self.__nautor
    
    @property
    def editora(self):
        return self.__editora
    
    @property
    def quantidade (self):
        return self.__quantidade

    @nlivro.setter
    def nlivro (self,nlivro):
        self.__nlivro = nlivro
    
    @nautor.setter
    def nautor(self,nautor):
        self.__nautor = nautor
    
    @editora.setter
    def editora(self,editora):
        self.__editora = editora

    @quantidade.setter
    def quantidade(self,quantidade):
        self.__quantidade = quantidade

    def consulta(self):
        texto = open('biblioteca.txt','r')
        leitor = texto.readlines()
        lista = list(leitor)
        texto.close()

        print(lista)

        seletor = input('Digite o nome do (livro/autor/editora) para consultar: ')
        if seletor == self.nlivro or seletor == self.nautor or seletor == self.editora:
            print(self.nlivro,self.nautor,self.editora,self.quantidade)
    
    def solicitar (self):
        seletor = input('Digite o nome do livro que queira solicitar: ')

        if seletor == self.nlivro:
            self.quantidade = self.quantidade - 1
            print('Solicitação com sucesso')
            print(self.quantidade)

def main ():
    livro = ('Pequeno_principe','arnold','lgs','3')
    livros = Biblioteca('Pequeno_principe','arnold','lgs',3)
    texto = open('biblioteca.txt','w')
    texto.writelines(','.join(livro))
    texto.close()
    livros.consulta()
    livros.solicitar()

if __name__ == '__main__':
    main()