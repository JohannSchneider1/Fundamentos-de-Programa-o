import random

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
        

#Criando matriz vazia
mat = []

# Ler do usuário o numero de linhas e colunas que a matriz terá 
nLinhas = int(input('Digite o numero de linhas: '))
nColunas = int(input('Digite o numero de colunsa: '))

for l in range (nLinhas):
    novalinha = []

    for c in range (nColunas):
        novoValor = random.randint(0,100)
        novalinha.append(novoValor) #adicionando o novo valor na linha auciliar cujo novalinha

    mat.append(novalinha)

imprimirmatriz(mat)



nLinhas =  random.randint(1,10)
nColunas = random.randint(1,10)

#inicializa a matriz nLinhas X nColunas com zeros
mat2 = [ [0]*nColunas] * nLinhas
imprimirmatriz(mat2)

#sorteia valores para cada posição
for i in range (nLinhas): #Percorrendo as Linhas
        for j in range (nColunas): #Percorrendo as colunas
             
             mat2[i][j] = random.randint (0,100)

imprimirmatriz(mat2)
