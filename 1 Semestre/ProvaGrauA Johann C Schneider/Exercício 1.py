########### FUNÇÕES ################
#função para ver se o numero é divisivel por 2
def divisao (div2):
    if div2%2 == 0: #condição para testar se o numero é divisivel por 2
        valor = True #valor vai ser verdadeiro
        print('É divisivel por 2')
    else:
        valor = False #valor vai ser falso
        print('Não é divisivel por 2')
    return valor #sai da função apenas a variavel valor



############# PROGRAMA ###############
#variavel de entrada para que o usuario possa digitar um numero
numero = int(input('Digite um numero inteiro: '))
#chamando a função e guardando o resultado na variavel (verdadeirofalso)
verfal = divisao(numero)

#exibindo na tela o valor da variavel e informando se retornou verdadeiro ou falso
print(verfal)