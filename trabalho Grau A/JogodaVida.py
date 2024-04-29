import random

########## FUNÇÕES #############
def morto(jogador1,jogador2):

    if escolha == 1:
        if jogador1 == 2 or jogador1 == 8 or jogador1 == 18:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('Trágico, Jogador 1 sofreu um acidente e acabou morrendo')
            jogadorvivo1 = False
            jogadorvivo2 = True
        else:
            jogadorvivo1 = True
            jogadorvivo2 = True

    elif escolha == 2:
        if jogador1 == 2 or jogador1 == 8 or jogador1 == 18:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('Trágico, Jogador 1 sofreu um acidente e acabou morrendo')
            jogadorvivo1 = False
        else:
         jogadorvivo1 = True

        if jogador2 == 2 or jogador2 == 8 or jogador2 == 18:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('Trágico, Jogador 2 sofreu um acidente e acabou morrendo')
            jogadorvivo2 = False
        else:
            jogadorvivo2 = True

    return jogadorvivo1, jogadorvivo2


def movimentar (jogador):
    sorteio = random.randint(1,6)

    if sorteio == 1:
        jogador = jogador + 1
    
    elif sorteio == 2:
        jogador = jogador + 2

    elif sorteio == 3:
        jogador = jogador + 3
    
    elif sorteio == 4:
        jogador = jogador + 4
    
    elif sorteio == 5:
        jogador = jogador + 5

    elif sorteio == 6:
        jogador = jogador + 6
            
    
    if jogador < 0:
        jogador = 0
    if jogador > 21:
        jogador = 21
    
    return jogador


def dado (jogador):
    sorteio = random.randint(1,6)

    print(sorteio)
    
    if sorteio == 1:
        jogador = jogador + 1

    elif sorteio == 3:
        jogador = jogador - 1
       
    elif sorteio == 6:

        if escolha == 2 and movimento == 'a':
            pass
            print('!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('Jogador 1 perde uma rodada')
            
        
        elif escolha == 2 and movimento =='s':
            pass
            print('!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('Jogador 2 perde uma rodada')
    
    if jogador < 0:
        jogador = 0
    if jogador > 21:
        jogador = 21
    
    return jogador



def ganhador(jogador1,jogador2):
    vencedor = 0
    if jogador1 == 21:
        vencedor =1

    if jogador2 == 21:
        if jogador1 <21:
            vencedor = 2

    return vencedor





################ PROGRAMA ################

jogador1 = 0
jogador2 = 0
vencedor = 0
jogadorvivo1 = True
jogadorvivo2 = True
parado = 0
saida = 0

escolha = int(input('Digite 1 para apenas um jogador e 2 para dois jogadores '))

while vencedor == 0:

    if escolha == 1:
        print('-------------------------------------------------------------------')
        movimento = (input('Digite a letra A para poder movimentar'))
        if movimento == 'a':
            jogador1 = movimentar(jogador1)
            print(jogador1)

    elif escolha == 2:
        print('-------------------------------------------------------------------')
        movimento = input('Digite a letra A para o jogador 1 poder andar\nDigite a letra S para o jogador 2 poder movimentar:\n ')

        if movimento == 'a':
            jogador1 = movimentar(jogador1)

        elif movimento == 's':
            jogador2 = movimentar(jogador2)

        print(jogador1,jogador2)
        
        if jogador1 == 1 or jogador1 == 3 or jogador1 == 10 or jogador1 == 17:
            jogador1 = dado(jogador1)
            print(jogador1)
            

        if jogador2 == 1 or jogador2 == 3 or jogador2 == 10 or jogador2 == 17:
            jogador2 = dado(jogador2)
            print(jogador2)
            
        
    if jogadorvivo2 == True and jogadorvivo1 == True:
        vencedor = ganhador(jogador1,jogador2)

    if jogadorvivo2 == True and jogadorvivo1 == True:
        jogadorvivo1,jogadorvivo2 = morto(jogador1,jogador2)
        if escolha == 1:
            if jogadorvivo1 == False:
                vencedor = 3
        else:        
            if jogadorvivo1 == False:
                vencedor = 2

            if jogadorvivo2 == False:
                vencedor = 1
            
        
if vencedor == 1:
    print('Jogador 1 é o vencedor')

if vencedor == 2:
    print('Jogador 2 é o vencedor') 

if vencedor == 3:
    print('Game Over')