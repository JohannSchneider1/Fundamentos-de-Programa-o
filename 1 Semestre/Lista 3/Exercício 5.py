#Criando uma variavel para colocar um número
numero = int(input('Digite um número que queira saber se é par ou ímpar '))

#Criando uma condição para ver se o numero é par ou impar
if numero%2==0:
    print('O número ',numero,' é PAR')
else:
    print('O número ',numero,'é ÍMPAR')