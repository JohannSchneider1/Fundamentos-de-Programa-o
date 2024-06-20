def imprimirMatriz (M):
    nLinahas = len(M)
    nColunas = len(M[0])

    for i in range (nLinahas):
        for j in range(nColunas):
            print(M[i][j],end = ' ')

        print('\n')


A1 = [1,5,9,2,5]

A2 = [7,4,13,21,6]

A3 = [8,-3,5,7,12]

matriz = []
for i in range(3):
    linha= []
    for j in range (5):
        linha.append(0)
    matriz.append(linha)
    

# Forma 1 e simples de fazer a matriz
#matriz.append(A1)
#matriz.append(A2)
#matriz.append(A3)

#imprimirMatriz(matriz)


# Forma 2 de fazer a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == 0:
            matriz[0][j] = A1[j]
        elif i == 1:
            matriz[1][j] = A2[j]
        elif i == 2:
            matriz[2][j] = A3[j]

       

imprimirMatriz(matriz)


#Exercício 2
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = matriz[i][j] * 7

imprimirMatriz(matriz)

