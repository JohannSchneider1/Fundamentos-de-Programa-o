#Biblioteca que gera números aleatórios
import random

#mostrando as opções possiveis para o usuario
print('Qual dos dados você deseja jogar')
print('1) Dade de 4 lados\n2) Dade de 6 lados\n3) Dade de 8 lados\n4) Dade de 10 lados\n5) Dade de 12 lados\n6) Dade de 16 lados')
#colheendo a alternativa do usuario
alternativa = int(input('Digite uma alternativa: '))

#Decidindo qual a quantidade de lados do dado de acordo com a escolha do usuário, e jogando
if alternativa == 1:
    D4 = random.randint(1,4)
    print('O dado escolhido foi um D4 e o valo é: ',D4)

elif alternativa == 2:
    D6 = random.randint(1,6)
    print('O dado escolhido foi um D6 e o valo é: ',D6)

elif alternativa == 3:
    D8 = random.randint(1,8)
    print('O dado escolhido foi um D8 e o valo é: ',D8)

elif alternativa == 4:
    D10 = random.randint(1,10)
    print('O dado escolhido foi um D10 e o valo é: ',D10)

elif alternativa == 5:
    D12 = random.randint(1,12)
    print('O dado escolhido foi um D12 e o valo é: ',D12)

elif alternativa == 6:
    D16 = random.randint(1,16)
    print('O dado escolhido foi um D16 e o valo é: ',D16)