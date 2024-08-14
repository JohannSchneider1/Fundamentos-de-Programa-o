############### Funções ###############
#criando uma função para comprimentar o nome que for implementado
def comprimento(nome):
    print('Olá caro(a): ',nome)

def dupla(nome1,nome2):
    print('Olá ',nome1,'a segunda pessoa se chama: ',nome2)

############### Programa Principal ###############

nome = input('Digite o seu nome: ')

#Chamando a função para que execute o que estiver endro
comprimento(nome)


nome1 = input('Usuario 1 digite o seu nome: ')

nome2 = input('Usuario 2 digite o seu nome: ')

dupla(nome1,nome2)

for i in range(5):
    print('Usuário', i+1, end = '')
    nome = input(', Digite seu nome: ')
    comprimento(nome)