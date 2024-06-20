def imprimirMatriz (M):
    nLinahas = len(M)
    nColunas = len(M[0])

    for i in range (nLinahas):
        for j in range(nColunas):
            print(M[i][j],end = ' ')

        print('\n')


matriz = []
for i in range(4):
    linha= []
    for j in range (4):
        linha.append(0)
    matriz.append(linha)

imprimirMatriz(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if  i == 0 and j == 0:            
            matriz[0][0] = 1
        elif i == 1 and j == 1:
            matriz[1][1] = 1
        elif i == 2 and j == 2:
            matriz[2][2] = 1
        elif i == 3 and j == 3:
            matriz[3][3] = 1

            
      
imprimirMatriz(matriz)
