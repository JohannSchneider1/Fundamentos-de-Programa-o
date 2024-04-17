##### Funções ######
#função da tabuada onde tem um sistema de repetição para fazer com que imprima na tela do 1 até o 10 e multiplique, ou seja tabuada
def tabuada(numero):
    for i in range(1,11):
        print(numero, ' X ', i,' = ', numero * i)


############ Programa ############

#variavel de entrada para saber um numero 
numero = int(input('Digite um número para descobrir a tabuada: '))

#chamando a função para realizar a tabuada, sem precisar dicar escrevento o tempo todo
tabuada(numero)

#fazendo a tabuada do 0 até 10 chamando a tabuada e impementando a variavel i dentro da função
for i in range (0,11):
    tabuada(i)
    print('-------------------------')