alternativa = 's'

while alternativa != 'n': #loop para ficar repetindo até que o usuario queira sair

    #variavel de entrada para saber qual numero o usuário gostaria de fazer a fatoração
    numero = int(input('Digite um número para realizar o farotial: '))
    #resultado sendo 1 para não multiplicar por 0
    resultado = 1
    
    #loop para contar até o numero definido
    for n in range(1,numero+1):
        resultado = resultado * n #Fazendo com que a cada loop multiplique o resultado pelo numero novo assim fazendo a farotação invertida

    #imprimindo resultado
    print(resultado)

    #Condição de saida do loop
    alternativa = input('Deseja continuar? (S/N) ')