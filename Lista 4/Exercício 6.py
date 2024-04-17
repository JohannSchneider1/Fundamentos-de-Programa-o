#importando a biblioteca de gerar números aleatórios
import random

valores = [] #chat # Variavel coju os valores serão colocados dentro dela / Obs. Tem que ser CHAVES
media = 0

for numero in range(1,6): #loop para gerar os 5 numeros alearótios
    aleatorio = random.randint(0,100) #gerador de numeros aleatórios
    valores.append(aleatorio) #chat #chamando a variavel valores e COLOCANDO/SALVANDO NA MEMÓRIA os valores que são gerados pelo aleatorizador

    #Calculando a média
    media = media + aleatorio
    total = media/numero

print(valores)

menorV = min(valores) #chat #Variavel onde está comparando os numeros dentro da variavel VALORES e salvando o MENOR deles
maiorV = max(valores) #chat #Variavel onde está comparando os numeros dentro da variavel VALORES e salvando o MAIOR deles

#exibindo os valores
print('O menor Valor sorteado foi de ',menorV)
print('O maior Valor sorteado foi de ',maiorV)
print('A média dos numeros aleatórios foi de: ',round(total,2))