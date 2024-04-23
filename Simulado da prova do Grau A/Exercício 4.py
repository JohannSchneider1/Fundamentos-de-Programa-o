#importando a biblioteca que aleatoriza as coisas
import random

tentativas = 3
numero = 0

#gerando um numero aleatório
aleatorio = random.randint(1,10)

print('Tente adivinhar o número entre de 1 à 10')

#loop para se repetir até que as tentativas se esgote ou se acertar o numero
while tentativas > 0 and numero!=aleatorio:

    numero = int(input('Digite um número: '))

    tentativas  = tentativas - 1

    #se errou o numero exiba na tela e mostre quantas tentativas restam
    if numero != aleatorio and tentativas != 0:
        print('você errou ainda resta mais ',tentativas)


#se acertou da o parabém e se acabou as tentativas exiba o numero sorteado
if numero == aleatorio:
    print('Parabéns você acertou o número')
else:
    print('Suas tentativasa cabaram o número sorteado foi: ',aleatorio)