
from competicao import Competicao
from corredor import Corredor
from data import Data
from informacoesatletas import InformacoesAtletas
from nadador import Nadador

def main ():
    data = Data('25','09','2024')
    competicao = Competicao('Correr é show',data)
    competicao.imprime_info()

    n1 = Nadador('Cielo',36,'Borboleta')
    n1.imprime_info()

    c1 = Corredor('Josenildo', 91, 68, competicao)
    c1.imprime_info()

    data.mes = '10'

    competicao.imprime_info()

    data2 = Data ('31','12','2024')
    corrida = Competicao('São Silvestre', data2)
    c2 = Corredor('Petrolina',100,60,corrida)

    c2.imprime_info()

    escolha = int(input('Digite 1 para criar um Nadador\nDigite 2 para criar um Corredor'))
    a = None

    if escolha == 1:
        nome = input('Digite um nome: ')
        idade = int(input('Digite uma idade: '))
        categoria = input('Digite a categoria: ')
        a = Nadador(nome,idade,categoria)
    
    if escolha == 2:
        nome = input('Digite um nome: ')
        idade = int(input('Digite uma idade: '))
        peso = float(input('Digite o peso: '))

        a = Corredor(nome,idade,peso,corrida)
    
    InformacoesAtleta = InformacoesAtletas

    InformacoesAtleta.imprime_exclusivo_atleta(a)
    InformacoesAtleta.imprime_informacoes_atleta(a)

    if isinstance(a,Nadador):
        a.categoria = 'Livre'
    
    if isinstance(a,Corredor):
        a.peso = 89
    
    a.imprime_info()

if __name__ == '__main__':
    main()

