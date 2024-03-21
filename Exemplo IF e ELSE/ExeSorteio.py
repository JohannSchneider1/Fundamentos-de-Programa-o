#Biblioteca que gera números aleatórios
import random

#fazendo a variavel virar um número aleatório
a = random.randint(1,3)

#mostrando o numero aleatorizado
print(a)

numeroSorteado=random.randint(1,3)

numeroLido = int(input('Digite um nímero de 1 a 3: '))

if numeroLido == numeroSorteado:
    print('Você Acertou')
else:
    print('Você Errou, o número sorteado era: ',numeroSorteado)