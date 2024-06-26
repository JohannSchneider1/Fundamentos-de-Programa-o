import random

#função de embaralhar
def shuffle(arr):
    n = len(arr) #Pega o tamanho do array

    for x in range(n): 

        i = random.randint(0, n - 1) #sorteia os numeros
        j = random.randint(0, n - 1)

    arr[i], arr[j] = arr[j], arr[i] #Troca os numeros de lugares

    return arr


array = []
embaralhado = []

quantidade = int(input('Digite o tamanho do seu vetor em numeros: ')) # cria o tamnanho do array desejado

for x in range(quantidade):  #implementa os indices dentro do array
    indice = input('Digite uma letra: ')
    array.append(indice)

print('Array Original')
print(array)

embaralhado = shuffle(array) # chama a função e salva o resultado na variavel

print('Array Embaralhado')
print(embaralhado)