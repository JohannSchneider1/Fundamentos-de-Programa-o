#biblioteca 1 para deixar random as coisas
#biblioteca 2 para ficar limpando a tela
import random
import os

H1 = 0
H2 = 0
# 0 ninguém venceu ainda
# 1 Humister 1 venceu
# 2 Humister 2 venceu
# 3 empate
vencedor = 0

while vencedor == 0: #continu a 
    #limpando a tela do console a cada ciclo// escolhe onde a tela irá resetar, neste caso no inicio do ciclo//animação
    os.system('cls' if os.name=='nt' else 'clear')

    #fazendo a movimentação do Hamister 1
    H1sorteio = random.randint(1,5) # sorteia um numero entre 1 e 5
    #Aplicar as regras da tabela na posição do hamister 1
    if H1sorteio == 1:
        H1 = H1 + 1
    elif H1sorteio == 2:
        H1 = H1+2
    elif H1sorteio == 3:
        #Não se mexe, pode retirar se quiser
        pass
    elif H1sorteio == 4:
        H1 = H1 -1

    else:
        H1 = H1-2

    #Garantir que não existe posição negativa nem maior que 12
    if H1<0:
        H1 = 0
    if H1>12:
        H1 = 12


    #fazendo a movimentação do Hamister 2
    H2sorteio = random.randint(1,5) # sorteia um numero entre 1 e 5
    #Aplicar as regras da tabela na posição do hamister 2
    if H2sorteio == 1:
        H2 = H2 + 1
    elif H2sorteio == 2:
        H2 = H2+2
    elif H2sorteio == 3:
        #Não se mexe, pode retirar se quiser
        pass
    elif H2sorteio == 4:
        H2 = H2 -1

    else:
        H2 = H2-2

    #Garantir que não existe posição negativa nem maior que 12
    if H2<0:
        H2 = 0
    if H2>12:
        H2 = 12

    #testa quem venceu
    if H1 == 12:
        vencedor =1
        print('Hamister 1 Ganhou')
    
    if H2 == 12:
        if vencedor == 0:
            vencedor =2
        else:
            vencedor =3
    
    #Imprimi na tela o status da corrida
    print('Hamister1: ')
    for n in range(H1):
        print('* ',end =' ')
    print()#quebra de linha

    print('Hamister2: ')
    for n in range(H2):
        print('* ',end =' ')
    print()#quebra de linha
    print('-----------------------------------------------')

#Imprimindo que ganhou fora do while
if vencedor == 1:
    print ('Hamister 1 Venceu')
elif vencedor ==2:
    print('Hamister 2 Venceu')
else:
    print('Houve um empate')