#Criando variavel para a divisão
n1 = int(input('Digite um número que queira ser dividido, diferente de 0: '))
n2 = int(input('Digite um número que queira ser o divisor, diferente de 0: '))

#Criando uma condição para testar se o valor digitado no n2 é diferente de 0
if n2!=0:
    nt = n1/n2
    print('O Resultado da divisão de',n1,' por ',n2,' é: ', nt)
else:
    print('O divisor não pode ser 0')
