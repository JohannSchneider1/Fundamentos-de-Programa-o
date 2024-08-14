########### FUNÇÕES ##############
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


    
    

######## Programa ########
#pedindo para o usuario digitar um numero e para ser testado e guardando na variavel
numero = int(input('Digite um número: '))

# chamando a função para testar o numero e retornando o valor do return e salvando em uma variavel saida
saida = primo(numero)

# condição para ver se a saida foi verdadeira ou falsa
if saida == True:
    print('O numero é Primo')
elif saida == False:
    print('O numero não é Primo')