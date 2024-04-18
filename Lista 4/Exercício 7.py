#Variavel onde será armazenado os nomes das pessoas
#outra maneira de resolver
#lista = []
menor = ''
#tabela ascii Maiusculas antes das minusculas
menor = 'Z'

for n in range(5): #loop para que 5 usuários possam colocar os seus nomes
    print('Usuário',n+1, end = '')#exibindo para o usuario numeros digitar o nome
    nome = input(' Digite seu nome(Primeira letra em Maiúscula): ') # salvando o nome digitado em uma variavel
    #if n == 0:
    #   menor = nome
    if nome<menor:
        menor = nome

    #outra maneira de resolver
    #lista.append(nome) #colocando e salvando o nome digitado na variavel lista

print (menor)
#outra maneira de reslver
#lista.sort() #A função do (sort) é definir em ordem alfabétia os nomes, se quisermos colocar do Z até o A precisamos colocar entre parentes o comando (reverse = TRUE)

#outra maneider de resolver
#print('Em ordem alfabética fica: ',lista) #exibindo os nomes salvos da lista, só que agora estão em ordem alfabética