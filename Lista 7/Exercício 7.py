import random

def imprimirMatriz(M):
    nLinha = (len(M))
    nColuna = (len(M[0]))

    for i in range (nLinha):
        for j in range (nColuna):
            print(M[i][j], end = ' ')
        print('\n')

def sinaisTrocados(M):

    for i in range (len(M)):
        for j in range (len(M[i])):

            M[i][j] = -M[i][j]

            
matriz = []

for i in range (5):
    auxi = []
    for j in range (5):
        auxi.append(0)
    matriz.append(auxi)

imprimirMatriz(matriz)

for i in range(len(matriz)):
    for j in range (len(matriz[0])):
        alea = random.randint(-10,10)
        matriz[i][j] = alea

print('Matriz Original')
imprimirMatriz(matriz)

print('Matriz com os sinais trocados')
sinaisTrocados(matriz)
imprimirMatriz(matriz)
