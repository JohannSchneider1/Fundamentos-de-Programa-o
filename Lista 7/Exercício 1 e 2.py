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

matriz = [[0]*5]*3
matriz = []

matriz.append(A1)
matriz.append(A2)
matriz.append(A3)

imprimirMatriz(matriz)

#for i in range(len(matriz)):
#    for j in range(len(matriz[0])):
#        matriz[i][j] = A1[j]

       

#imprimirMatriz(matriz)


#Exercício 2
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = matriz[i][j] * 7

imprimirMatriz(matriz)

