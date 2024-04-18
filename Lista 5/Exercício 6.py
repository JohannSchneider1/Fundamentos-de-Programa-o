import random
############# Funções ##################
def lootbox ():
    comum = 0
    raro = 0
    lendario = 0
    sorte = random.randint(0,100)
    if sorte == 100:
        print('Parabésn Você acaba de ganhar um item LENDÁRIO')
        lendario = lendario + 3
        return lendario

    elif sorte >=0 and sorte<=80:
        print('Você tirou um item COMUM')
        comum = comum + 1
        return comum

    elif sorte >=81 and sorte<=99:
        print ('Você acaba de tirar um item RARO')
        raro = raro + 2
        return raro

def inventario(raridade):
    lendario = 0
    raro = 0
    comum = 0

    if raridade == 3:
        lendario = lendario +1
        
    elif raridade == 2:
        raro = raro +1
        
    elif raridade == 1:
        comum = comum + 1
    print('Itens Lendários: ',lendario )
    print('Itens Raros: ',raro )
    print('Itens Comuns: ',comum )


############ Programa Principal ###############
saida = 1

while saida != 0 :
    print('1 - Caixa de Itens\n2 - Invertário\n0 - Sair do Programa')
    escolha = int(input('Digite a alternativa desejada: '))

    if escolha == 1:
        raridade = lootbox()
        inventario(raridade)

    elif escolha == 2:
        inventario(0)
    else:
        saida = 0