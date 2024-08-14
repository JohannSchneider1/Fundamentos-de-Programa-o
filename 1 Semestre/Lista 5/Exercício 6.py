#importando a biblioteca de geradores de numeros aleatórios
import random
############# Funções ##################
#função para gerar a lootbox 
def lootbox (comum,raro,lendario):
    sorte = random.randint(0,100) #gerando um numero de 0 a 100

    if sorte == 100: #condição para saber se o numero sorteado foi o 100
        print('Parabésn Você acaba de ganhar um item LENDÁRIO')
        lendario = lendario + 1 #adicionando em 1 a variavel
        return comum,raro,lendario #retornando/saind todas as variáveis, por mais que só saia uma modificada

    elif sorte >=0 and sorte<=80: #condição para saber se o numero sorteado foi entre 0 a 80
        print('Você tirou um item COMUM')
        comum = comum + 1 #adicionando em 1 a variavel
        return comum,raro,lendario #retornando/saindo todas as variáveis, por mais que só saia uma modificada

    elif sorte >=81 and sorte<=99: #condição para saber se o numero sorteado foi entre 81 a 99
        print ('Você acaba de tirar um item RARO')
        raro = raro + 1 #adicionando em 1 a variavel
        return comum,raro,lendario #retornando/saindo todas as variáveis, por mais que só saia uma modificada

def inventario(comum,raro,lendario):
    #exibindo os itens que adquiriu
    print('---------------------------------------------------------')
    print('Itens Lendários: ',lendario )
    print('Itens Raros: ',raro )
    print('Itens Comuns: ',comum )


############ Programa Principal ###############
saida = 1
comum = 0
raro = 0
lendario = 0

while saida != 0 : #loop para ficar repetindo o codigo
    #exibindo as informações
    print('---------------------------------------------------------')
    print('1 - Caixa de Itens\n2 - Invertário\n0 - Sair do Programa')
    escolha = int(input('Digite a alternativa desejada: '))

    if escolha == 1: #condição em relação a escolha
        comum,raro,lendario = lootbox(comum,raro,lendario) #chamando a função e os valores que são retornados da lootbox está salvando nas respectivas variáveis

    elif escolha == 2:
        inventario(comum,raro,lendario) #chamando a função e mostrando o inventário
    else:
        saida = 0