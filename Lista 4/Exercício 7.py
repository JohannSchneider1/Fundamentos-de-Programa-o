#Variavel onde será armazenado os nomes das pessoas
lista = []

for n in range(5): #loop para que 5 usuários possam colocar os seus nomes
    print('Usuário',n+1, end = '')#exibindo para o usuario numeros digitar o nome
    nome = input(' Digite seu nome: ') # salvando o nome digitado em uma variavel
    lista.append(nome) #colocando e salvando o nome digitado na variavel lista

lista.sort() #A função do (sort) é definir em ordem alfabétia os nomes, se quisermos colocar do Z até o A precisamos colocar entre parentes o comando (reverse = TRUE)

print('Em ordem alfabética fica: ',lista) #exibindo os nomes salvos da lista, só que agora estão em ordem alfabética