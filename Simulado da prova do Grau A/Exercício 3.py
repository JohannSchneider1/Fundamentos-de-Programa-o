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
#Gerando os numeros e testando para saber se é primo ou não
for n in range (1,30):

    #chamando a função para saber se é primo ou não
    saida=primo(n)

    #se for primo exiba na tela
    if saida == True and n!=1:
        print(n)