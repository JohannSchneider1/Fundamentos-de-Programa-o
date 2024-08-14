#importando a biblioteca aleatiorizadora
import random

###### Funções ########
#criando a função sorteio com um limitador de inicio em fim
def sorteio (inicio,fim):
    numerosortiado = random.randint(inicio,fim) #gerando o numero aleatório com o limitador definido
    print('O numero sorteado entre ',inicio,' e ',fim,' foi: ',numerosortiado) # exibindo o numero

######## Programa Principal ############
numero = int(input('Digire o 1 numero: ')) #variavel de entrada para saber o inicio do limitador
numero2 = int(input('Digire o 2 numero: '))# variavel de entrada para saber o final do limitador

sorteio(numero,numero2)#chamando a função sorteio para que possa executála