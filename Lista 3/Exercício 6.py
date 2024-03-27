#Biblioteca que gera números aleatórios
import random

#Fazendo a variavel virar um numero aleatório
numerosorteado = random.randint(0,5)

#Fazendo o usuário decidir se ele quer par ou impar
escolha = int(input('Digite 1 para ÍMPAR e 2 para PAR: '))

#se ele for engraçadinho deverá decidir novamente
if escolha > 2:
    escolha = int(input('Digite novamente sem palhaçada: '))

#escolhendo a condição a qual o usuario decidiu
if escolha == 1:
    print('Você escolheu ÍMPAR')
elif escolha == 2:
    print('Você escolheu PAR')
else:
    print('Escolha novamente: ')

#colocando uma variavel de entrada para perguntar um numero 
numero = int(input('Escolha um número de 0 até 5: '))

#somando os dois resultados e colocando em uma variavel
total = numero + numerosorteado

#Fazendo a condição para ver quem ganhou este mini game
if total%2==0 and escolha == 2:
    print('Parabéns você ganhou, você colocou: ',numero,' e eu coloquei: ',numerosorteado, 'A soma total foi de: ', total, ' Logo deu PAR')
elif total%2!=0 and escolha == 1:
    print('Parabéns você ganhou, você colocou: ',numero,' e eu coloquei: ',numerosorteado, 'A soma total foi de: ', total, ' Logo deu ÍMPAR')
elif total%2 == 0 and escolha == 1:
    print('Parabéns para mim eu ganhei esta, você colocou: ',numero,' e eu coloquei: ',numerosorteado, 'A soma total foi de: ', total, ' Logo deu PAR')
else:
    print('Parabéns para mim eu ganhei esta, você colocou: ',numero,' e eu coloquei: ',numerosorteado, 'A soma total foi de: ', total, ' Logo deu ÍMPAR')