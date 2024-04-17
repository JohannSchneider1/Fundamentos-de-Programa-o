#biblioteca de numeros aleatórios
import random

#A
#utilizando o loop for estamos exibindo um numero de 0 a 100
for numero in range(0,101):
    print(numero)

print('/////////////////////////////////////////////////////////////////////////////')
#B
#Utilizando o loop for estamos exibindo um numero de 20 a 50, mas apenas os pares, pois aumenta de 2 em 2
for numero in range(20,51,+2):
    print(numero)

print('/////////////////////////////////////////////////////////////////////////////')
#C
#Utilizando o loop for estamos exibindo um numero de 70 até 25 ou seja decrecente
for numero in range(70,25-1,-1):
    print(numero)

print('/////////////////////////////////////////////////////////////////////////////')
#D
#Utilizando o loop for estamos exibindo um numero de 95 até 25 ou seja decrecente, mas somente os ímpares
for numero in range (95,25-1,-2):
    print(numero)

print('/////////////////////////////////////////////////////////////////////////////')
#E
cont = 0
total = 0
while cont<15: #loop para contar até 15
    numero = float(input('Digite um número: ')) #armazenando variavel digitada pelo usuário
    cont = cont+1 #condição para que possamos sair do loop
    total = total + numero #Aqui estamos fazendo com que após o usuario digitar um número ele ira somar com o total que no inicio é 0, depois se o usuario digitar 1 e em seguida 2 o total será 0+1 depois 1+2 e assim por diante

media = total/15 #após digitar os 15 numeros será calculado a média
print ('A soma total é de: ',total) # exibindo o total que foi calculado
print('A média é de: ',round(media,2)) # exibindo a média arredondada

print('/////////////////////////////////////////////////////////////////////////////')
#F
cont = 0
contP = 0
contI = 0
while cont<10: #loop para contar até 10
    cont = cont+1 #condição para que possamos sair do loop
    numero = int(input('Digite um número inteiro: ')) # armazena um número
    if numero%2==0: # se o numero for divizivel por 2 então o contador Par aumenta em 1
        contP = contP+1
    else: # caso contrario o contador Impar aumenta em 1
        contI = contI+1

print('A quantidade de números Pares foi de: ',contP,' E de Impar foi de: ',contI) #exibe a quantidade de numeros pares e impares digitados pelo usuário

print('/////////////////////////////////////////////////////////////////////////////')
#G
cont = 0
contP = 0
contN = 0

while cont<20: #loop para contar até 20
    aleatorio = random.randint(-10,10) #Gerador de números aleatórios emtre -10 e 10
    cont = cont + 1 #condição para que possamos sair do loop

    if aleatorio>0: # se o numero for maior que 0 exiba e conte 1 para Positivo
        print (aleatorio,' É Positivo')
        contP = contP + 1

    elif aleatorio <0:# se o numero for menor que 0 exiba e conte 1 para Negativo
        print(aleatorio,'É Negativo')
        contN = contN + 1
    else:# caos contrario é 0
        print (aleatorio, 'É Nulo')

print('A quantidade de números Positivos gerados foi de: ', contP,' E de Negativo foi de: ',contN) #exiba a quantidade de vezes que o numero foi positivo e negativo

print('/////////////////////////////////////////////////////////////////////////////')
#H
#armazenando a variavel para a quantidade de vezes que será executado o loop
quantidade = int(input('Digite a quantidade de numeros que gostaria de digitar: '))
total = 0
while quantidade>0: #enquanto a quantidade for maior que 0 execute
    quantidade = quantidade - 1 #condição para sair do loop
    numero = float(input('Digite um número: ')) #pede por usuario digitar um numero e guardar em uma variavel
    total = total + numero #Pega o numero digitado anteriormente e soma com o digitado atual, repete o processo armazenando a soma e somando com o novo numero digitado

print('O total foi de: ',total)#exibindo a soma todal dos numeros digitados