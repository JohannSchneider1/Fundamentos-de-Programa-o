import random

#Imprimindo uma matriz olhando CADA indice dentro dela
def imprimirMatriz(M):
    nLinha = (len(M))
    nColuna = (len(M[0]))

    for i in range (nLinha):
        for j in range (nColuna):
            print(M[i][j], end = ' ')
        print('\n')


def gerarToupeiras ():
    matriz=[['-' for x in range(4)] for x in range(4)] #Uma das forma de gerar uma matriz

    toupeiras = 0

    #Criando as Toupeiras
    while toupeiras < 4:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        if matriz[i][j] == '-': #Subistituindo os algoritimos '-' por 'T' #Só adiciona toupeira SE estiver vazio o lugar
            matriz[i][j] = 'T'
            toupeiras += 1 #condição para sair do loop

    return matriz

#Gerando 3 saidas diferentes
for i in range (1,4):
    print('##############')

    matriz = gerarToupeiras()

    imprimirMatriz(matriz)