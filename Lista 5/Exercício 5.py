###### Funções ########
def soma (num1,num2):
    total = num1 + num2
    return total

def subtracao (num1,num2):
    total = num1 - num2
    return total

def multiplicacao(num1,num2):
    total = num1 * num2
    return total

def divisao(num1,num2):
    total = num1 / num2
    return total

######## Programa Principal ############
saida = ''
while saida != 'n':

    print('Escolha uma das operações a seguir: ')
    print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
    escolha = int(input('Digite a alternativa desejada: '))

    numero1 = int(input('Digite o 1 numero real: '))
    numero2 = int(input('Digite o 2 numero real: '))

    if escolha == 1:

        soma(numero1,numero2)
        print(numero1,' + ',numero2, ' = ', soma(numero1,numero2))

    elif escolha == 2:
        total = subtracao(numero1,numero2)
        print(numero1,' - ',numero2, ' = ', total)
    
    elif escolha == 3:
        total = multiplicacao(numero1,numero2)
        print(numero1,' * ',numero2, ' = ', total)
    
    elif escolha == 4 and numero2 != 0:
        total = divisao(numero1,numero2)
        print(numero1,' / ',numero2, ' = ', total)
    else:
        print('Resposta Inválida')


    saida = input('Deseja continuar da calculadora ? (S/N) ')