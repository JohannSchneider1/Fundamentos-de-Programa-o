#função que percorre os elementos do array por indice e imprime o seus valores
def imprimirvetor (V):
    n = len(V)
    for i in range (n):
        print(V[i],end = ' ')
    
#-------------------------------------------------------------------------------------

#percorrendo/varrendo pelo Array

#por elemento / percorrendo os elementos do array E
A = list(range(7,12))
for i in A:
    print('Valor: ',i)

#por Indice / Percorrer o array A acessando os elementos a partir do índice
#Mostra o Indice que esta e o valor armazenado dentro dele
A = list(range(1,6))
for i in range(len(A)):
    print('A[{}] = {}'. format(i,A[i]))

#forma de fazer sem o format
for i in range(len(A)): # O range retorna de 0 até o tamanho -1
    print('Valor de A[',i,']: ',A[i])

#Mesma coisa com o While
i = 0
while i < len(A):
    print('A[{}] = {}'.format(i,A[i]))
    i = i+1

#Criando um Array Vazio
vet = []

# Ler do usuário o numero de elementos do Array

n = int(input('Digite o numeros de elementos do array: '))

# Preencer o vetor com os numeros lidos do usuário
for i in range(n):
    #Ler o valor e armazenar no elemento em uma variavel
    valor = int(input('Digite o valor do elelmento'))
    #append serve para acrecentar no array e assim aumentando o seu tamanho
    vet.append(valor)

imprimirvetor(vet)