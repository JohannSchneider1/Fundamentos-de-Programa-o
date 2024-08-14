#Criação de um Array já inicializado com 10 valores inteiros
A = [1,2,3,4,5,6,7,8,9,10]

#a função LEN serve para verificar o tamanho do array e armazená-lo em uma variavel
tamanho = len(A)

#Como acessar os Valores dentro de um ARRAY
segundo = A[1] #Variavel = Array[posição desejada]
penultimo = A[tamanho - 2]#Variavel = Array[tamanho do array menos o quanto que queira voltar -1]exemplo, ultimo elemento é tamanho -0 -1 = -1, penultimo é tamanho -1 -1 = -2, assim vai
posissao6 = A[len(A)-5]


#MANEIRAS DE IMPRIMIR ARRAYS
#exibindo o array e o tamanho que ele tem, ou seja, o que tem escrito dentro e o numero de caracteres que ele carrega
print (A,tamanho)
print ('Este ARRAY possui ',tamanho,' Elementos')
print ('Este ARRAY possui ',len(A),' Elementos')
print(segundo)
print(penultimo)
print(posissao6)
print('Imprimindo a posição numero 6 do Array é',A[6])
print('Imprimindo a posição numero 6 do Array é',A[tamanho - 4]) #utilizando a variavel que guarda o tamanho do Array
print('Imprimindo a posição numero 6 do Array é',A[len(A) - 4]) # Chamando diretamente a função que retorna o tamanho 

#imprimir(acessar) um elemento a partir de uma posição (variavel que armazena a posição e não o indice)
pos = 5 #esta variavel é para indicar (no exemplo) que gostariamos da 5 posição do vetor (indice 4)
print('Elemento que esta na posição ',pos,' do Array: ', A[pos-1]) #Lembrar sempre que começa no 0,1,2,3,4,5 ou seja a 5 posição é no indice 4 pois é 5 - 1 = 4


#pode salvar qualquer informação nos arrays
B = [tamanho,45,'a']

print(B)


#Só existe no python
primeiro = A[0]
ultimo = A[-1]
penultimo = A[-2]
print(primeiro,ultimo,penultimo)