##########FUNÇÕES###############
def imprimirMatir(M):
    nLinha = (len(M))
    nColuna = (len(M[0]))

    for i in range(nLinha):
        for j in range(nColuna):
            print(M[i][j], end = ' ')
        print('\n')

def creacao():
    linha = []
    for i in range(0,6):
        linha.append(int(input('Digite numeros inteiros: ')))
    
    return linha

def inversao (matriz):
    
    linha2 = []
    for i in range(6):
        linha2.append(matriz[0][6-i-1])
    
    return linha2

def soma (matriz):
    linha3 = []
    for j in range (len(matriz[0])):
        #somar posição 0 0 com 1 0 / 0 1 com 1 1 / 0 2 com 1 2
        linha3.append(matriz[0][j] + matriz[1][j])
    
    return linha3

def parimpar(matriz):
    linha4 = []
    for j in range (len(matriz[0])):
        if matriz[0][j]%2 != 0:
            linha4.append(matriz[0][j])
    
    for j in range(len(matriz[0])):
        if matriz[0][j]%2 == 0:
            linha4.append(matriz[0][j])
    
    return linha4

def transposta (matriz):

    nLinha = (len(matriz))
    nColuna = (len(matriz[0]))
    print('Matriz Original')
    for i in range(nLinha):
        for j in range(nColuna):
            print(matriz[i][j], end = ' ')
        print('\n')


    mt = [[0 for i in range(len(matriz))] for j in range(len(matriz[0]))]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            mt [j][i] = matriz[i][j]
    print('Matriz transposta')
    nLinha = (len(mt))
    nColuna = (len(mt[0]))
    for i in range(nLinha):
        for j in range(nColuna):
            print(mt[i][j], end = ' ')
        print('\n')

        

        

    
##########CODIGO##############

#matriz = [[0 for i in range(6)]for j in range(4)]
matriz = []

Ex1 = creacao()

matriz.append(Ex1)

La = inversao(matriz)

matriz.append(La)

Lb = soma(matriz)

matriz.append(Lb)  

Lc = parimpar(matriz)

matriz.append(Lc)

transposta(matriz)

