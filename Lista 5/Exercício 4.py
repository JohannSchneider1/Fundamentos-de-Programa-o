import random
###### Funções ########
def sorteio (inicio,fim):
    numerosortiado = random.randint(inicio,fim)
    print('O numero sorteado entre ',inicio,' e ',fim,' foi: ',numerosortiado)

######## Programa Principal ############
numero = int(input('Digire o 1 numero: '))
numero2 = int(input('Digire o 2 numero: '))

sorteio(numero,numero2)