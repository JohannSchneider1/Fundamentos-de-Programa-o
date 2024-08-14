###### Funções ########
#Criando a função para fazermos a soma da nossa calculadora
def soma (num1,num2):
    total = num1 + num2 # somando os 2 valores pedidos
    return total # o valor que irá sair será este

#Criando a função para fazermos a subtração da nossa calculadora
def subtracao (num1,num2):
    total = num1 - num2 # subtraindo os 2 valores pedidos
    return total # o valor que irá sair será este

#Criando a função para fazermos a multiplicação da nossa calculadora
def multiplicacao(num1,num2):
    total = num1 * num2 # multiplicando os 2 valores pedidos
    return total # o valor que irá sair será este

#Criando a função para fazermos a divisão da nossa calculadora
def divisao(num1,num2):
    total = num1 / num2 # dividindo os 2 falores pedidos
    return total # o valor que irá sair será este

######## Programa Principal ############

saida = ''

#loop para só sairmos do loop se apertarmos a letra N
while saida != 'n':

    #exibindo as opções e perguntando qual ele quer
    print('Escolha uma das operações a seguir: ')
    print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
    escolha = int(input('Digite a alternativa desejada: '))

    #pedindo e salvando em uma variável os numeros que queira ser operados
    numero1 = int(input('Digite o 1 numero real: '))
    numero2 = int(input('Digite o 2 numero real: '))

    #condições para que cada uma das escolhas que o usuário pedir
    if escolha == 1:
        soma(numero1,numero2) #chamando a Função Soma
        print(numero1,' + ',numero2, ' = ', soma(numero1,numero2)) #exibindo a soma visivelmente

    elif escolha == 2:
        total = subtracao(numero1,numero2) #chamando a Função Subtração
        print(numero1,' - ',numero2, ' = ', total) #exibindo a subtração visivelmente
    
    elif escolha == 3:
        total = multiplicacao(numero1,numero2) #chamando a Função Multiplicação
        print(numero1,' * ',numero2, ' = ', total) #exibindo a multiplicação visivelmente
    
    elif escolha == 4 and numero2 != 0:
        total = divisao(numero1,numero2) #chamando a Função Divisão
        print(numero1,' / ',numero2, ' = ', total) #exibindo a divisãovisivelmente
    else:
        print('Resposta Inválida')


    saida = input('Deseja continuar da calculadora ? (S/N) ') #condição para sairmos do loop