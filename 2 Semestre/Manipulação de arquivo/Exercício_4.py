class Pessoa:
    def __init__ (self,nome='',idade=0,altura=0.0,peso=0):
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


    def carregar(self, arquivo: str):
        texto = open(arquivo, "r")
        self.nome = texto.readline()
        self.idade = int(texto.readline())
        self.altura = float(texto.readline())
        self.peso = float(texto.readline())
        texto.close()

    def salvar(self, arquivo: str):
        texto = open(arquivo, "w")
        texto.write(self.nome + "\n")
        texto.write(str(self.idade) + "\n")
        texto.write(str(self.altura) + "\n")
        texto.write(str(self.peso))
        texto.close()

def main ():
    p = Pessoa()
    p.carregar("cadastro.txt")
    p.visualizar()
    p.nome = "jhonathan"
    p.idade = 25
    p.altura = 2.10
    p.peso = 150
    p.salvar("cadastro.txt")
    p.visualizar()

if __name__ == '__main__':
    main()