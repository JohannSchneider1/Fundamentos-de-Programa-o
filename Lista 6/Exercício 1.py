import random

vetor = []
menorV = 101
maiorV = 1

for i in range(1,11):
    sorteio = random.randint(10,90)
    vetor.append(sorteio)
    #E Uma das formas de resolver
    if sorteio>maiorV:
        maiorV = sorteio
    if sorteio<menorV:
        menorV = sorteio

#A
print(vetor)

#B
teste = False

for valor in vetor:
    if valor == 50:
        teste = True
    
if teste == True:
    print('O numero 50 foi encontrado')
else:
    print('O numero 50 não foi encontado')

#C
cont = 0
for p in vetor:
    if p == 50:
        cont = cont + 1
print('O numero 50 apareceu ',cont,' vezes')

#D
soma = 0
for loop in vetor:
    soma = soma + loop

media = soma/10
print(media)

#E Segunda maneira de resolver

menor = min(vetor) #procura no array vetor o Menor valor possivel
maior = max(vetor) #procura no array vetor o Maior valor possivel
print('O menor valor sorteado foi: ',menorV)
print('O maior valor sorteado foi: ',maiorV)
print('O menor valor sorteado foi: ',menor)
print('O maior valor sorteado foi: ',maior)

#F
print ('A soma total dos valor é de: ',soma)

#G 
for i in range(len(vetor)):
    tras = vetor[len(vetor)-1 -i] # Faz com que o indice dentro do vetor comece da direita para a esquerda na leitura
    print (tras)

#H
auxi = [] # Vetor auxiliar
for i in range(len(vetor)): #loop do tamanho do total de caracteres dentro do Vetor
    tras = vetor[len(vetor) - 1 -i] #Faz com que pegamos e inciamos pelo indice do Ultimo elemento e salvamos de tras para frente no vetor Tras
    auxi.append(tras)#salvamos em um vetor auxiliar os valores de tras para frente

print(auxi) #exibindo os indices

#I
parV = [x for x in vetor if x%2==0]
imparV = [x for x in vetor if x%2!=0]

print('Os numeros pares impressos no vetor são: ',parV)
print('Os numeros Impares impresos no vetor são: ',imparV)