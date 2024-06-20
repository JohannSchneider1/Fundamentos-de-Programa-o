import random
def imprimirMatir(M):
    nLinha = (len(M))
    nColuna = (len(M[0]))

    for i in range(nLinha):
        for j in range(nColuna):
            print(M[i][j], end = ' ')
        print('\n')
    
matriz = []

for i in range (4):
    auxi = []
    for j in range (6):
        auxi.append(0)
    matriz.append(auxi)

imprimirMatir(matriz)

for i in range(len(matriz)):
    for j in range (len(matriz[0])):
        alea = random.randint(-10,10)
        matriz[i][j] = alea

imprimirMatir(matriz)

#A
soma = 0
for i in range (len(matriz)):
    for j in matriz[1]:
         if i == 1:
            soma = soma + j

print (soma)

#B
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if j == 4:
            soma = soma + matriz[i][j]

print (soma)