#Inicializações alternativas

A = [1.1,2.2,3.3] # Delimitador de lista
B = ['a']*5 #Multiplicação de lista mesma coisa que ['a','a','a','a','a']

#listando iniciando com 5 e o proximo indice é o numero mais 3 ou seja indo de 3 em 3
C = list(range(20,5,-3)) #Typecast de uma sequencia Decrecente
D = list(range(5,20,3))#Typecast de uma sequencia Crescente

#faz X ao quadrado é o valor salvo, mas primeiro entra no loop e só faz o calculo se o valor de X for divisivel por 3/resto = 0
#sem o if ele apenas faz os numeros limitaos pelo for que é de 1 a 20 ao quadrado e salva
E = [x**2 for x in range (1,20) if x%3==0] #List Comprehension


print(A)
print(B)
print(C)
print(D)
print(E)

#por elemento / percorrendo os elementos do array E
for i in E:
    print('Valor: ',i)