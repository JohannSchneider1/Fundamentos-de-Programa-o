class Pessoa:
    def __init__(self, nome, idade, altura, irmaos, endereco):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.irmaos = irmaos
        self.endereco = endereco
    
    def imprime_infos(self):
        print('Nome: ',self.nome,'\nIdade: ',self.idade,'\nAltura: ',self.altura,'\nIrmãos: ',self.irmaos,'\nEndereço: ',self.endereco)
    
    def is_filhos_unicos(self)->bool:
        if self.irmaos != 0:
            return False
        else:
            return True

    
def main():
    
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    irmaos = int(input('Digite a quantidade de irmãos: '))
    endereco = input('Digite seu endereço: ')

    p1 = Pessoa(nome,idade,altura,irmaos,endereco)
    p1.imprime_infos()
    if p1.is_filhos_unicos():
        print(nome,'É filho unico')
    else:
        print(nome,'Não é filho unico')
    

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    irmaos = int(input('Digite a quantidade de irmãos: '))
    endereco = input('Digite seu endereço: ')
    p2 = Pessoa(nome,idade,altura,irmaos,endereco)
    if p2.is_filhos_unicos():
        print(nome,'É filho unico')
    else:
        print(nome,'Não é filho unico')

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    irmaos = int(input('Digite a quantidade de irmãos: '))
    endereco = input('Digite seu endereço: ')
    p3 = Pessoa(nome,idade,altura,irmaos,endereco)
    if p3.is_filhos_unicos():
        print(nome,'É filho unico')
    else:
        print(nome,'Não é filho unico')
    
    

if __name__ == '__main__':
    main()