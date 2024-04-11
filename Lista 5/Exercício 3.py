###### Funções ########
#Criando uma função que calcula a media do grau A e B e retorna para meida
def media_unision (grauA,grauB):
    media = (grauA + 2*grauB) / 3
    return media



######## Programa Principal ############
#variavel de entrada para saber as notas
grauA = float(input('Digite a sua media do Grau A: '))
grauB = float(input('Digite a sua media do Grau B: '))

#chamando a função criada anteriormete e atribuindo os valors do grau A e B, armazenando em uma variavel o valor que sair
grauFinal = media_unision(grauA,grauB)

#exibindo na tela o grau final com a variavel, citada anteriormente, arredondada em 2 digitos após a virgula
print('Grau Final é: ',round(grauFinal,2))

#Outra forma de fazer a mesma coisa que anteriormente, mas sem precisar guardar em uma variavel
#print('Grau Final é: ',media_unision(grauA,grauB))