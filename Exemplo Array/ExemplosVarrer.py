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