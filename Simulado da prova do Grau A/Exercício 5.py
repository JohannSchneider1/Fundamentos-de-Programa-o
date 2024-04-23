################### FUNÇÕES ####################
def trocar (cafe,agua,leite,cappuccino):
    print('----------------------------------------------')
    print('Qual dos compartimentos gostaria de trocar?')
    print('A) Café')
    print('B) Cappuccino')
    print('C) Leite')
    print('D) Água')
    escolha = input('Digite a alternativa: ')

    if escolha == 'a':
        cafe = 1000
        print('Café reabastecido')
        return cafe,agua,leite,cappuccino
    
    elif escolha == 'b':
        cappuccino = 1000
        print('Cappuccino reabastecido')
        return cafe,agua,leite,cappuccino
    
    elif escolha == 'c':
        leite = 1000
        print('Leite reabastecido')
        return cafe,agua,leite,cappuccino
    
    elif escolha == 'd':
        agua = 1000
        print('Água reabastecido')
        return cafe,agua,leite,cappuccino

def consultar (cafe,agua,leite,cappuccino):
    print('----------------------------------------------')
    print('Qual dos compartimentos gostaria de consultar?')
    print('A) Café')
    print('B) Cappuccino')
    print('C) Leite')
    print('D) Água')
    escolha = input('Digite a sua escolha: ')

    if escolha == 'a':
        print('Esta máquina ainda tem ',cafe,' Gramas')
        
    elif escolha == 'b':
        print('Esta máquina ainda tem ',cappuccino,' Gramas')
        
    elif escolha == 'c':
        print('Esta máquina ainda tem ',leite,' Mililitros')
        
    elif escolha == 'd':
        print('Esta máquina ainda tem ',agua,' Mililitros')
        


def preparar (cafe,agua,leite,cappuccino):
    print('----------------------------------------------')
    print('Qual dos tipos de café gostaria?')
    print('A) Café Preto        R$ 1,00')
    print('B) Café com Leite    R$ 1,50')
    print('C) Cappuccino        R$ 2,00')
    escolha = input('Digite a sua escolha: ')

    if escolha =='a':
        dinheiro = float(input('Coloque o dinheiro: '))

        if dinheiro >= 1.00:
            dinheiro = dinheiro - 1
        
        if cafe >= 15 and agua >= 250:
            cafe = cafe - 15
            agua = agua - 250
            
            print('Café Preto pronto, retire a sua bebida')
            if dinheiro != 0 and dinheiro > 0:
                print('Aqui está seu troco R$',dinheiro)
            
        else:
            dinheiro = dinheiro + 1
            print('Produto indisponível, devolvendo o seu dinheiro... R$',dinheiro)

        return cafe,agua,leite,cappuccino


    if escolha =='b':
        dinheiro = float(input('Coloque o dinheiro: '))

        if dinheiro >= 1.50:
            dinheiro = dinheiro - 1.50

        if cafe >= 20 and leite >= 250:
            cafe = cafe - 20
            leite = leite - 250
            print('Café com Leite pronto, retire a sua bebida')
            if dinheiro != 0 and dinheiro > 0:
                print('Aqui está seu troco R$',dinheiro)
            
        else:
            dinheiro = dinheiro + 1.50
            print('Produto indisponível, devolvendo o seu dinheiro... R$',dinheiro)

        return cafe,agua,leite,cappuccino

    if escolha =='c':
        dinheiro = float(input('Coloque o dinheiro: '))

        if dinheiro >= 2:
            dinheiro = dinheiro - 2
            
        if cappuccino >= 40 and agua >= 300:
            cappuccino = cappuccino - 40
            agua = agua - 300
            print('Café pronto, retire a sua bebida')
            if dinheiro != 0 and dinheiro > 0:
                print('Aqui está seu troco R$',dinheiro)

        else:
            dinheiro = dinheiro + 2
            print('Produto indisponível, devolvendo o seu dinheiro... R$',dinheiro)

        return cafe,agua,leite,cappuccino




############### PROGRAMA #######################
cappuccino = 1000
leite = 1000
agua = 1000
cafe = 1000
dinheiro = 0
saida = ''

while saida != 'd':

    print('----------------------------------------------')
    print('Escolha uma das alternativas a baixo')
    print('A) Troca de Refil')
    print('B) Consultar a quantidade')
    print('C) Preparar o Café')
    print('D) Desligar a Máquina')
    escolha = input('Digite uma das alternativas: ')

    if escolha == 'a':
        cafe,agua,leite,cappuccino = trocar(cafe,agua,leite,cappuccino)

    elif escolha == 'b':
        consultar(cafe,agua,leite,cappuccino)

    elif escolha == 'c':

        cafe,agua,leite,cappuccino = preparar(cafe,agua,leite,cappuccino)

    elif escolha == 'd':
        saida = 'd'