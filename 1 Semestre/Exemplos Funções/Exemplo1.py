#Área com a implementação das funções que o código vai usar
#Funçoes tem que estar implementadas antes da chamada delas(ou seja, acima do codigo que estiver utilizando)
def minha_funcao ():
    #Comandos que serão executados quando a função (Minha funcao) for chamado
    print('Estou utilizando fuções pela 1 vez')

def funcao_com_parametros(part1,part2,part3):
    print('olá função com parametros')
    print('Parametro 1: ',part1)
    print('Parametro 2: ',part2)
    print('Parametro 3: ',part3)




############### Programa Principal ###############

print('Olá!')

minha_funcao()

funcao_com_parametros(part2=13,part3=24,part1=35)

funcao_com_parametros(13,2.4,'C')

a ='joao'
b = input("Digite alguma coisa: ")

funcao_com_parametros(a,b,True)