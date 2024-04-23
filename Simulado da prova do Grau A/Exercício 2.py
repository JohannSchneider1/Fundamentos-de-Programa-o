######## Função #########
#função para testar se é numero primo ou não
def primo (teste):
    #se a variavel teste for um numero primo que será testado depois ao invés disso já considera ele sendo um numero primo
    if teste == 2 or teste == 3 or teste == 5 or teste == 7 or teste == 11 or teste == 13 or teste == 17 or teste == 19:
        resultado = True

    elif teste % 2 == 0:        #aqui é a parte que vai avaliar o resultado de cada uma das divisões e verá se é numero primo ou não se for 0 o resultado será false
        resultado = False
    elif teste % 3 == 0:
        resultado = False
    elif teste % 5 == 0:
        resultado = False 
    elif teste % 7 == 0:
        resultado = False
    elif teste % 11 == 0:
        resultado = False
    elif teste % 13 == 0:
        resultado = False
    elif teste % 17 == 0:
        resultado = False
    elif teste % 19 == 0:
        resultado = False   
    else:
        resultado = True
    
    #retora o resultado, ou seja, a informação que irá sair resá a do resultado final sendo true ou false
    return resultado

######## Programa ##########
saida = 1
quantidade = -1
positivo = 0
negativo = 0
div2 = 0
div5 = 0
numeroprimo = 0

#loop para ficar repetindo enquanto a sainda não for verdadeira
while saida != 0:
    
    escolha = int(input('Precione 0 caso queira sair do programa\nPrecione 1 para continuar\n'))

    if escolha >= 1: #condição para verificar se vai ou não sair do loop
        numero = int(input('Digite um numero para testar: ')) #variavel para armazenar o numero digitado

        if numero>= 0: # condiçlão para ver se o numero é positivou ou negativo
            positivo = positivo + 1
        else:
            negativo = negativo + 1
        
        if numero % 2 ==0: # condição para saber se o numero é divisivel por 2 ou por 5
            div2 = div2 + 1
        elif numero % 5 == 0:
            div5 = div5 +1

        Nprimo = primo (numero) # chamando a função primo para testar e ver se o numero é primo ou não
        # se for primo irá adicionar em 1 o contador de numeros primos
        if Nprimo == True:
            numeroprimo = numeroprimo + 1

        saida = 1


    else:
        saida = 0

    quantidade = quantidade + 1
    

#exibindo os resultados após o usuario terminar de digitar os numeros
print (positivo,' dos ',quantidade, ' são positivos')
print (negativo,' dos ',quantidade, ' são negativos')
print (div2,' dos ',quantidade, ' são divisiveis por 2')
print (div5,' dos ',quantidade, ' são divisiveis por 5')
print (numeroprimo,' dos ',quantidade, ' são primos')