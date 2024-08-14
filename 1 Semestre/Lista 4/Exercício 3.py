escolha = 's'

while escolha!='n': #loop para ficar fazendo a tabuada enquanto o usuário não apertar N
    numero = int(input('Digite um número de 1 a 9 para fazer a tabuada: '))

    if numero>=1 and numero<=9: #condição para que o numero seja 1 a 9

        for n in range(1,11,+1): #loop do numero começa em 1 vai até o 10 adicionando +1 a cada volta
            produto=n*numero # faz a multiplicação
            print(numero, ' X ',n,' = ',produto) #exibe de forma bonitinha a tabuada

    else:
        print('Nùmero inválido') # condição não adequada, digitou alco que não estava entre 1 a 9
    
    escolha = input('Caso queira sair aperte (n): ') # condição para sair do loop