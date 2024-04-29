#biblioteca 1 para deixar random as coisas
#biblioteca 2 para ficar limpando a tela
import random
import os

################### FUNÇÕES ###################
def movimentarhamister(poshamister):

    H1sorteio = random.randint(1,5) # sorteia um numero entre 1 e 5
    #Aplicar as regras da tabela na posição do hamister 1
    if H1sorteio == 1:
        poshamister = poshamister + 1

    elif H1sorteio == 2:
        poshamister = poshamister + 2

    elif H1sorteio == 3:
        #Não se mexe, pode retirar se quiser
        pass

    elif H1sorteio == 4:
        poshamister = poshamister -1

    else:
        poshamister = poshamister - 2

    #Garantir que não existe posição negativa nem maior que 12
    if poshamister<0:
        poshamister = 0
    if poshamister>12:
        poshamister = 12
    #retorna o valor da posição modificada
    return poshamister

def imprimirStatusCorrida(hamister1,hamister2):

    print('Hamister1: ')
    for n in range(hamister1):
        print('* ',end =' ')
    print()#quebra de linha

    print('Hamister2: ')
    for n in range(hamister2):
        print('* ',end =' ')
    print()#quebra de linha
    print('-----------------------------------------------')

def verificaGanhador(hamister1,hamister2):
    vencedor = 0
    if hamister1 == 12:
        vencedor =1
    
    if hamister2 == 12:
        if vencedor == 0:
            vencedor = 2
        else:
            vencedor = 3
    return vencedor



#################### PROGRAMA PRINCIPAL #############################
H1 = 0
H2 = 0
# 0 ninguém venceu ainda
# 1 Humister 1 venceu
# 2 Humister 2 venceu
# 3 empate
vencedor = 0

while vencedor == 0: #continua 
    #limpando a tela do console a cada ciclo// escolhe onde a tela irá resetar, neste caso no inicio do ciclo//animação
    os.system('cls' if os.name=='nt' else 'clear')

    #fazendo a movimentação do Hamister 1
    H1 = movimentarhamister(H1)

    #fazendo a movimentação do Hamister 2
    H2 = movimentarhamister(H2)

    #testa quem venceu
    imprimirStatusCorrida(H1,H2)
    
    #Imprimi na tela o status da corrida
    vencedor = verificaGanhador(H1,H2)

    


#Imprimindo que ganhou fora do while
if vencedor == 1:
    print ('Hamister 1 Venceu')
elif vencedor ==2:
    print('Hamister 2 Venceu')
else:
    print('Houve um empate')