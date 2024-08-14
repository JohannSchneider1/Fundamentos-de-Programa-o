#Escrever o nome 10 vezes
nome = input('DIgite seu nome: ')

#Variavel para a contagem de vezes que foi escrito
cont = 0

while cont<10:
    print(cont+1,nome) #cont+1 começa com o contador partindo do 1 ao invez de 0
    cont = cont + 1 #Incrementa em 1 unidade
    #cont+=1 forma comprimida da linha anterior
    #cont++ utilizado em outras linguagens para fazer a mesma coisa da linha anterior