import random

########## FUNÇÕES #############
def morto(jogadorvivo):
        
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('Trágico, você sofreu um acidente e acabou morrendo')
    jogadorvivo = False

    return jogadorvivo


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
    
    sorte = random.randint(1,6)
    
    if sorte == 1:
        jogador = jogador + 1

    elif sorte == 3:
        jogador = jogador - 1
       
    elif sorte == 6:

        if escolha == 2 and jogador == jogador1:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('Jogador 1 perde uma rodada')
            
        elif escolha == 2 and jogador == jogador2:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('Jogador 2 perde uma rodada')
    
    print(jogador)
    
    return jogador,sorte


def ganhador(jogador1,jogador2):
    vencedor = 0
    if jogador1 == 21:
        vencedor =1

    if jogador2 == 21:
        if jogador1 <21:
            vencedor = 2

    return vencedor


def primo ():
    #se a variavel teste for um numero primo que será testado depois ao invés disso já considera ele sendo um numero primo
        print('-------------------------------------------------------------------')
        print('Os numeros primos até 100 são:')
        for teste in range(1,101,+1):
            if teste == 2 or teste == 3 or teste == 5 or teste == 7 or teste == 11 or teste == 13 or teste == 17 or teste == 19:
                resultado = True

            elif teste % 2 == 0:        #aqui é a parte que vai avaliar o resultado de cada uma das divisões e verá se é numero primo ou não se for 0 o resultado será false
                resultado = False
            elif teste % 3 == 0:
                resultado = False
            elif teste % 5 == 0:
                resultado = False 
            elif teste % 7 == 0:
                resultado = False
            elif teste % 11 == 0:
                resultado = False
            elif teste % 13 == 0:
                resultado = False
            elif teste % 17 == 0:
                resultado = False
            elif teste % 19 == 0:
                resultado = False   
            else:
                resultado = True
            
            if resultado == True:
                print(teste)

def soma ():
    valor = 0
    print('-------------------------------------------------------------------')
    print('Fazendo a somatória de todos os numeros de 1 até 10 fica: ')
    for numero in range(1,11,+1):
        valor = valor + numero
    
    print(valor)

def fibonacci ():
    ultimo = 1
    penultimo = 1
    print('-------------------------------------------------------------------')
    print('A série de Fibonacci até o 10 elemento é: ')
    for n in range(1,11,+1):
        resultado = penultimo + ultimo
        penultimo = ultimo
        ultimo = resultado
        print (resultado)

def circulo ():
    pi = 3.14159265358979323846
    area = pi * (2.5 * 2.5)
    print('-------------------------------------------------------------------')
    print ('A Área de um circulo com 2,5 de raio é:\n',round(area,2))

def fatorial ():
    valor = 1
    for n in range(1,6):
        valor = valor * n
    print('-------------------------------------------------------------------')
    print('O fatorial de 5 é: \n',valor)

def divisao ():
    print('-------------------------------------------------------------------')
    print('Os 5 primeiros numeros divisiveis por 2 e 5 são:')
    for n in range (1,51):
        if n%2 == 0 and n%5 == 0:
            print(n)

def desafios ():
    sorteado = random.randint(1,6)

    if sorteado == 1:
        primo()
    elif sorteado == 2:
        soma()
    elif sorteado == 3:
        fibonacci()
    elif sorteado == 4:
        circulo()
    elif sorteado == 5:
        fatorial()
    elif sorteado == 6:
        divisao()


def formar (jogadorformado):

    sorteio = random.randint(1,6)
    print('-------------------------------------------------------------------')
    if sorteio == 1:
        jogadorformado = True
        print('Parabéns você se formou em Direito')

    elif sorteio == 2:
        jogadorformado = True
        print('Parabéns você se formou em Medicina')

    elif sorteio == 3:
        jogadorformado = True
        print('Parabéns você se formou em Jogos Digitais')

    elif sorteio == 4:
        jogadorformado = True
        print('Parabéns você se formou em Engenharia Quântica')

    elif sorteio == 5:
        jogadorformado = True
        print('Parabéns você se formou em Engenharia da Computação')

    elif sorteio == 6:
        jogadorformado = True
        print('Parabéns você se formou em Administração')

    return jogadorformado


def famoso (fama):
    
    fama = True
    print('Parabéns você acaba de ficar famoso')

    return fama


def filhos (filho):

    gemeos = random.randint (1,6)
    if gemeos == 5:
        filho = filho + 2
        print('Parabéns você acaba de ter filhos Gêmeos')
    else:
        filho = filho + 1
        print('Parabéns você acaba de ter um filho')
    print('Total de filhos é de ',filho)
    
    return filho


def loteria (dinheiro):
    sorte = random.randint(1,6)

    if sorte == 1:
        dinheiro = 2,50
        print('Você acaba de garnha na loteria um total de R$ 2,50')
    elif sorte == 2:
        dinheiro = 5000
        print('Você acaba de garnha na loteria um total de R$ 5.000')
    elif sorte == 3:
        dinheiro = 50000
        print('Você acaba de garnha na loteria um total de R$ 50.000')
    elif sorte == 4:
        dinheiro = 500000
        print('Você acaba de garnha na loteria um total de R$ 500.000')
    elif sorte == 5:
        dinheiro = 5000000
        print('Você acaba de garnha na loteria um total de R$ 5.000.000')
    elif sorte == 6:
        dinheiro = 100000000
        print('Você acaba de garnha na loteria um total de R$ 100.000.000')

    return dinheiro
            

def casado (casamento):

    print('-------------------------------------------------------------------')
    print('Parabéns você se casou')
    casamento = True 
    return casamento

def divorcio (casamento):
    print('-------------------------------------------------------------------')
    print('Você acaba de se Divorciar após ver seu/sua parceiro(a) o(a) Traindo')
    casamento = False
    return casamento

def tempo (jogador,filhos,dinheiro,formado,famoso,casado):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('Você acaba de entrar em uma máquina do tempo, retorne ao inicio e perca tudo o que conquistou durante sua vida')
    jogador = 0
    filhos = 0
    dinheiro = 0
    formado = False
    famoso = False
    casado = False

    return jogador,filhos,dinheiro,formado,famoso,casado

################ PROGRAMA ################

jogador1 = 0
jogador2 = 0
vencedor = 0
filhos1 = 0
filhos2 = 0
dinheiro1 = 0
dinheiro2 = 0
passado1 = 0
passado2 = 0
jogador1formado = False
jogador2formado = False
fama1 = False
fama2 = False
casado1 = False
casado2 = False
jogadorvivo1 = True
jogadorvivo2 = True
luck = 0
cont = 2


escolha = int(input('Digite 1 para apenas um jogador e 2 para dois jogadores '))

while vencedor == 0 and jogadorvivo1 == True and jogadorvivo2 == True:

    if escolha == 1:
        print('-------------------------------------------------------------------')
        movimento = (input('Digite a letra A para poder movimentar\n'))
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
        

    if passado1 != jogador1:

        if jogador1 == 1 or jogador1 == 3 or jogador1 == 10 or jogador1 == 17: 
            jogador1,luck = dado(jogador1)
            
        if jogador1 == 20:
            jogador1,filhos1,dinheiro1,jogador1formado,fama1,casado1 = tempo(jogador1,filhos1,dinheiro1,jogador1formado,fama1,casado1)

        if jogador1 == 4 or jogador1 == 11 or jogador1 == 19:
            desafios()

        if jogador1 == 15:
            fama1 = famoso(fama1)
        
        if jogador1 == 5:
            jogador1formado = formar(jogador1formado)
        
        if jogador1 == 6 or jogador1 == 9 or jogador1 == 13:
            filhos1 = filhos(filhos1)
        
        if jogador1 == 14:
            dinheiro1 = loteria(dinheiro1)
        
        if jogador1 == 7 or jogador1 == 16:
            casado1 = casado (casado1)
        
        if jogador2 == 12:
            casado1 = divorcio(casado1)
        
        if jogador1 == 2 or jogador1 == 8 or jogador1 == 18:
            jogadorvivo1 = morto(jogadorvivo1)

        passado1 = jogador1


    if passado2 != jogador2:

        if jogador2 == 1 or jogador2 == 3 or jogador2 == 10 or jogador2 == 17:
            jogador2,luck = dado(jogador2)

        if jogador2 == 20:
            jogador2,filhos2,dinheiro2,jogador2formado,fama2,casado2 = tempo(jogador2,filhos2,dinheiro2,jogador2formado,fama2,casado2)

        if jogador2 == 4 or jogador2 == 11 or jogador2 == 19:
            desafios()

        if jogador2 == 15:
            fama2 = famoso(fama2)
        
        if jogador2 == 5:
            jogador2formado = formar(jogador2formado)
        
        if jogador2 == 6 or jogador2 == 9 or jogador2 == 13:
            filhos2 = filhos(filhos2)
        
        if jogador2 == 14:
            dinheiro2 = loteria(dinheiro2)
        
        if jogador2 == 7 or jogador2 == 16:
            casado2 = casado (casado2)
        
        if jogador2 == 12:
            casado2 = divorcio(casado2)
        
        if jogador2 == 2 or jogador2 == 8 or jogador2 == 18:
            jogadorvivo2 = morto(jogadorvivo2)
        
        passado2 = jogador2

    vencedor = ganhador(jogador1,jogador2)

if jogadorvivo1 == False:
    vencedor = 2
if jogadorvivo2 == False:   
    vencedor = 1
if jogadorvivo1 == False and escolha == 1:
    vencedor = 3


if vencedor == 1:
    print('---------------------------------------------------------')
    print('Jogador 1 é o vencedor')
    print('Veja a sua vida:')
    if casado1 == True:
        print('Você se casou')
    if filhos1 != 0:
        print('Você teve ',filhos1,' Filhos')
    if dinheiro1 != 0:
        print('Você ganhou na loteria um total de R$',dinheiro1)
    if fama1 == True:
        print('Você ficou Famoso')
    if jogador1formado == True:
        print('Você se formou')

if vencedor == 2:
    print('Jogador 2 é o vencedor')
    print('Veja a sua vida:')
    if casado2 == True:
        print('Você se casou')
    if filhos2 != 0:
        print('Você teve ',filhos2,' Filhos')
    if dinheiro2 != 0:
        print('Você ganhou na loteria um total de R$',dinheiro2)
    if fama2 == True:
        print('Você ficou Famoso')
    if jogador2formado == True:
        print('Você se formou') 

if vencedor == 3:
    print('Game Over')