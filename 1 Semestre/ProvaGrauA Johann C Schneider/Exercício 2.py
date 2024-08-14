########### FUNÇÕES ################
#função para fazer a divisão
def divisao (dividendo,divisor):
    #condição para que não possa ser dividido por 2
    if divisor != 0:
        valor = dividendo % divisor
        #condição para saber se o numero é divisivel por 2 ou não e retornar valor
        if valor == 0:
            print ('O numero ',dividendo,' é divisivel por ',divisor)
            return True
        else:
            print('O numero ',dividendo,' não é divisivel por ',divisor)
            return False
    # Se o divisor for 0 exiba e retorne false
    else:
        print('Não é possivel dividir pois o divisor é 0')
        return False





############# PROGRAMA ###############
#pedindo para o usurario escrever os valores desejados
dividendo = int(input('Digite um numeo que será dividido: '))
divisor = int(input('Digite um numero para ser o divisor: '))

#salvando o resultado retornado na variavel
resultado = divisao(dividendo,divisor)

#exibindo o resultado da função divisão
print(resultado)