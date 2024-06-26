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

#C
soma1 = 0
for i in range (len(matriz)):
    for j in matriz[0]:
         if i == 1:
            soma1 = soma1 + j

soma2 = 0
for i in range (len(matriz)):
    for j in matriz[3]:
         if i == 1:
            soma2 = soma2 + j

produto = soma1*soma2
print(produto)

#D
soma = 0
for i in range(len(matriz)):
    for j in matriz[i]: #percorrer cada elemento de cada linha
        if j%2 ==0:
            soma += j

print(soma)

#E
soma = 0
for i in range(len(matriz)):
    for j in matriz[i]: #percorrer cada elemento de cada linha
        if j%2 !=0:
            soma += j

print(soma)


#Exercício 5
maior = -20
menor = 20
for i in range(len(matriz)):
    for j in matriz[i]:
        if j > maior:
            maior = j
        if j < menor:
            menor = j

print('Maior Valor: ',maior)
print('Menor Valor: ',menor)