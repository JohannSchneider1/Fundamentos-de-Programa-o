from calculadora import Calculadora
from funcionario import Funcionario
from empresa import Empresa

def main ():
    calculadora1 = Calculadora ('Vermelho',400)
    calculadora2 = Calculadora ('Amarelo',600)

    nome1 = input('Digite o nome do primeiro funcionario: ')
    endereco1 = input('Digite seu endereco: ')

    nome2 = input('Digite o nome do segundo funcionario: ')
    endereco2 = input('Digite seu endereco: ')

    func1 = Funcionario(nome1,endereco1,calculadora1)
    func2= Funcionario(nome2,endereco2,calculadora2)

    nome_empresa = input('Digite o nome da empresa: ')

    empresa = Empresa(nome_empresa,func1,func2)
    empresa.imprime_info()

    print('Operações realizada pelo funcionario: ',func1.nome)
    print('2 + 2 = {:.2f}'.format(func1.soma(2.0,2.0)))
    print('5 - 4 = {:.2f}'.format(func1.subtracao(5.0,4.0)))
    print('2 X 3 = {:.2f}'.format(func1.multiplicacao(2.0,3.0)))

    print('Operações realizada pelo funcionario: ',func2.nome)
    print('6 / 3 = {:.2f}'.format(func2.divisao(6.0,3.0)))
    print('7 + 2 = {:.2f}'.format(func2.soma(7.0,2.0)))
    print('8 X 3 = {:.2f}'.format(func2.multiplicacao(8.0,3.0)))


if __name__ == '__main__':
    main()
