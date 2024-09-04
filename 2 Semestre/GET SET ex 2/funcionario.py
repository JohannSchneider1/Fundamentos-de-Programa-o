from calculadora import Calculadora

class Funcionario:
    def __init__(self,nome,endereco,calculadora:Calculadora):
        self.__nome = nome
        self.__endereco = endereco
        self.__calculadora = calculadora

    @property
    def nome (self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def calculadora(self):
        return self.__calculadora
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @endereco.setter
    def endereco(self,endereco):
        self.__endereco = endereco
    
    @calculadora.setter
    def calculadora(self,calculadora):
        self.__calculadora = calculadora

    def soma (self,v1,v2):
        resultado = self.calculadora.soma(v1,v2)
        return resultado
    
    def subtracao (self,v1,v2):
        resultado = self.calculadora.subtracao(v1,v2)
        return resultado
    
    def multiplicacao (self,v1,v2):
        resultado = self.calculadora.multiplica(v1,v2)
        return resultado
    
    def divisao (self,v1,v2):
        resultado = self.calculadora.divisao(v1,v2)
        return resultado
    
    def imprime_info (self):
        print('Nome: ',self.nome)
        print('Endereco: ',self.endereco)
        self.calculadora.imprime_info()

def main ():
    nome = input('Digite o seu nome: ')
    endereco = input('Digite seu endereco: ')
    memoria = int(input('Digite quanto de memoria tem a sua calculadora: '))
    cor = input('Digite qual a cor de sua calculadora: ')
    calculadora = Calculadora (cor,memoria)

    pessoa = Funcionario(nome,endereco,calculadora)
    pessoa.imprime_info()

if __name__ == '__main__':
    main()