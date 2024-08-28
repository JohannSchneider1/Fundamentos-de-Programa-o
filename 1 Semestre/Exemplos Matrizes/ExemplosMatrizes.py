def imprimirmatriz (M):
    #Armazenando o numer de linhas e numero de colunas
    nLinhas = len(M)
    nColunas = len(M[0])

    #exibindo a matriz completa / Percorrendo/varredura a matriz utilizando os índices de linhas e colunas
    for i in range (nLinhas): #Percorrendo as Linhas
        for j in range (nColunas): #Percorrendo as colunas
            #dentro do contexto do segundo for, podemos acessar o elemento com indice de linhas e colunas
            print (M[i][j],end = ' ')
        #dentro do contesto do primeiro for, podemos fazer operações utilizando a linha inteira
        print('\n')
        
print()


#Criando uma matriz / Matriz 4 x 5
        #Colunas
    #   0  1  2  3  4       
M = [ [ 1, 2, 3, 4, 5],     #0
      [ 6, 7, 8, 9,10],     #1  Linhas
      [11,12,13,14,15],     #2
      [16,17,18,19,20] ]    #3


#Mostrando um numero localizado na matriz sendo o primeiro a Linha = Y e o segundo a Coluna = X
print (M[2][3])

#Mostrando a Matriz
print(M) #mostrando cada linha e coluna da matriz
print(len(M))       #Mostra o numero total de LINHAS
print(len(M[0]))    #Mostra o numero total de COLUNAS
