########### FUNÇÕES ################
#Função para preparar as poções
def preparar (pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio):

    print('-------------------------------------------')
    print('Qual Poção gostaria de preparar?')
    print('1 - Poção de Cura')
    print('2 - Poção Força da Floresta')
    print('3 - Poção Sabedoria da Riqueza')
    print('4 - Poção Sorte no Amor')
    print('5 - Poção Malvada')
    escolha = int(input('Digite a alernativa que deseja: '))

    #condições que varia de acordo com a escolha o usuario, cada alternativa irá executar uma poção diferente
    if escolha == 1:
        #Poção de Cura / Condição para ela ser criada e se criar irá retirar parte dos igredientes
        if pofenix >=30 and essencelestial >= 20 and floressecas >= 20 and lagriunicornio >= 10:
            pofenix = pofenix - 30
            essencelestial = essencelestial - 20
            floressecas = floressecas - 20
            lagriunicornio = lagriunicornio - 10
            print('Sua poção está pronta!')

        #Caso não possa ser criada irá mostar qual ou quais igrediente estão faltando
        else:
            if pofenix < 30:
                print('Está com pouco Pó de Fenix')

            if essencelestial < 20:
                print('Está com pouca Essencia Celestial')

            if floressecas < 20:
                print('Está com poucas Flores Secas')
            
            if lagriunicornio < 10:
                print('Está com pouca Lagrima de Unicórnio')
        
        return pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio
    
    
    elif escolha == 2:
        #Poção Força da Floresta / Condição para ela ser criada e se criar irá retirar parte dos igredientes
        if orvalholunar >= 20 and raizdragao >= 30 and floressecas >= 30:
            orvalholunar = orvalholunar - 20
            raizdragao = raizdragao - 30
            floressecas = floressecas - 30
            print('Sua poção está pronta!')

        #Caso não possa ser criada irá mostar qual ou quais igrediente estão faltando
        else:
            if orvalholunar < 20:
                print('Etá com pouco Orvalho lunar')
            
            if raizdragao < 30:
                print('Está com pouca Raiz de Dragão')

            if floressecas < 30:
                print('Está com poucas Flores Secas')
        return pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio

    elif escolha == 3:
        #Poção Sabedoria da Riqueza / Condição para ela ser criada e se criar irá retirar parte dos igredientes
        if essencelestial >= 30 and pofenix >= 50:
            essencelestial = essencelestial - 30
            pofenix = pofenix - 50
            print ('Sua poção está pronta!')
    
        #Caso não possa ser criada irá mostar qual ou quais igrediente estão faltando
        else:
            if essencelestial < 30:
                print('Está com pouca Essencia Celestial')

            if pofenix < 50:
                print('Está com pouco Pó de Fenix')
        return pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio
    
    elif escolha == 4:
        #Poção Sorte no Amor / Condição para ela ser criada e se criar irá retirar parte dos igredientes
        if orvalholunar >= 10 and floressecas >= 50 and lagriunicornio >= 5:
            orvalholunar = orvalholunar - 10
            floressecas = floressecas - 50
            lagriunicornio = lagriunicornio - 5
            print ('Sua poção está pronta!')
        
        #Caso não possa ser criada irá mostar qual ou quais igrediente estão faltando
        else:
            if orvalholunar < 10:
                print('Etá com pouco Orvalho lunar')

            if floressecas < 50:
                print('Está com poucas Flores Secas')

            if lagriunicornio < 5:
                print('Está com pouca Lagrima de Unicórnio')
        return pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio

    elif escolha == 5:
        #Poção Malvada / Condição para ela ser criada e se criar irá retirar parte dos igredientes
        if elixiramargo >= 10 and raizdragao >= 15:
            elixiramargo = elixiramargo - 10
            raizdragao = raizdragao - 15
            print('Sua poção está pronta!')
        
        #Caso não possa ser criada irá mostar qual ou quais igrediente estão faltando
        else:
            if elixiramargo < 10:
                print('Etá com pouco Elixir Amargo')
            
            if raizdragao < 15:
                print('Está com pouca Raiz de Dragão')
        return pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio


#Função para consultar quanto de cada material o usuário ainda tem
def consultar (pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio):

    #Exibindo as informações
    print('-------------------------------------------')
    print('Qual dos Igredientes gostaria de consultar?')
    print('1 - Pó de Fenix')
    print('2 - Essencia Celestial')
    print('3 - Raiz de Dragão')
    print('4 - Orvalho Lunar')
    print('5 - Flores Secas')
    print('6 - Elixir Amargo')
    print('7 - Lágrimas de Unicórnio')
    escolha = int(input('Digite a alernativa que deseja: '))

    #condições que varia de acordo com a escolha o usuario, irá mostrar informações diferentes sobre cada igrediente
    if escolha == 1:
        print('Você ainda tem ',pofenix,' gramas de Pó de Fenix')

    elif escolha == 2:
        print('Você ainda tem ',essencelestial,' mililitros de Essencia Celestial')
    
    elif escolha == 3:
        print('Você ainda tem ',raizdragao,' gramas de Raiz de Dragão')
    
    elif escolha == 4:
        print('Você ainda tem ',orvalholunar,' mililitros de Orvalho Lunar')
    
    elif escolha == 5:
        print('Você ainda tem ',floressecas,' gramas de Flores Secas')
    
    elif escolha == 6:
        print('Você ainda tem ',elixiramargo,' mililitros de Elixir Amargo')

    elif escolha == 7:
        print('Você ainda tem ',lagriunicornio,' mililitros de Lágrimas de Unicórnio')


############# PROGRAMA ##############
#variaveis onde contem cada igrediente inicial
pofenix = 100
essencelestial = 50
raizdragao = 45
orvalholunar = 30
floressecas = 200
elixiramargo = 20
lagriunicornio = 15
sair = 1

#loop para só sair quando o usuário decidir
while sair != 0:
    
    #Menu
    print('-------------------------------------------')
    print('Escolha uma das alternativas')
    print('1 - Preparar Poção')
    print('2 - Consultar os Igredientes Disponíveis')
    print('3 - Sair')
    escolha = int(input('Digite a alternativa desejada: '))

    #condições que varia de acordo com a escolha o usuario, irá executar funções diferentes
    if escolha == 1:
      #Chamando a Função preparar e salvando as mudanças de variaveis em seus respectivos nomes
      pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio = preparar(pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio)
    
    elif escolha == 2:
        #chamando a função consultar para que o usuário possa averiguar o seu estoque
        consultar(pofenix,essencelestial,raizdragao,orvalholunar,floressecas,elixiramargo,lagriunicornio)
    
    elif escolha == 3:
        #condição de saida do programa
        sair = 0