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

    def carregar (self):
        texto = open('cadastro.txt','r')
        leitura = texto.readline()
        dados = list (leitura)
    
        cadastro = []
        self.nome = dados [0]
        self.idade = dados[1]
        self.altura = dados[2]
        self.peso = dados [3]

        cadastro.append(self.nome)
        cadastro.append(self.idade)
        cadastro.append(self.altura)
        cadastro.append(self.peso)

        return cadastro



def main ():

    
    p = Pessoa

if __name__ == '__main__':
    main()