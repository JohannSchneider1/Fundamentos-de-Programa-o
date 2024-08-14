#variaveis de entrada para determinar o numero de vezes que irá aparecer e qual simbolo utilizar
numero = int(input('Digite um numero: '))
caracter = input('Digite um caracter para desenhar: ')

#loop fazendo com que o limite seja o numero informado salvando na variavel N
for n in range(1,numero+1):
    #Exibindo o valor do caracter inicial
    print(caracter)
    #loop para complementar o caracter inicial fazendo co que o numero de vezes repetidas seja o valor da variavel N atual
    for carac in range(1,n+1):
        #condição para exibir estes caracteres em sequencia sem fazer com que se repita 2 vezes a ultima linha
        if n < numero:
            #Exibindo os caracteres reptidos na mesma linha fazendo com que corresponda ao numero da posição
            print(caracter, end = '')
    