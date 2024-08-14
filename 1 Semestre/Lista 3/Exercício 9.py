#duas variaveis de entrada para saber quanto esta cada moeda atualmente
dolar = float(input('Digite em Real o valor do Dólar: '))
euro = float(input('Digite em Real o valor do Euro: '))

#saida para informar as alternativas
print('Qual das alternativas corresponde a converção que deseja')
print('1) Converter de Real para Euro \n2) Concerter de Real para Dólar \n3) Converter de Euro para Dólar \n4) Converter de Euro para Real')
print('5) Converter de Dólar para Euro \n6) Converter de Dólar para Real')
#variavel de entrada para sabar qual a escolha do usuario
alternativa = int(input('Digite uma alternativa: '))

#Varias condiçoes para utilizar apenas a alternativa que o usuario escolheu e fazer a converção desejada
if alternativa == 1:
    Vreal = float(input('Digite quantos Reais quer converter para Euro: '))
    convercao = Vreal / euro
    print('O valor R$',Vreal,' Fica €', round(convercao,2))

elif alternativa == 2:
    Vreal = float(input('Digite quantos Reais quer converter para Dólar: '))
    convercao = Vreal / dolar
    print('O valor R$',Vreal,' Fica US$', round (convercao,2))

elif alternativa == 3:
    Veuro = float (input('Digite quantos Euros quer converter para Dólar: '))
    RVeuro = Veuro * euro
    convercao = RVeuro / dolar
    print('O valor €',Veuro,' Fica US$', round(convercao,2))

elif alternativa == 4:
    Veuro = float(input('Digite quantos Euros quer converter para Real: '))
    convercao = Veuro*euro
    print('O valor €',Veuro,' Fica R$', round(convercao,2))

elif alternativa == 5:
    Vdolar = float(input('Digite quantos Dólares quer converter para Euro: '))
    RVdolar = Vdolar * dolar
    convercao = RVdolar/euro
    print('O valor US$',Vdolar,' Fica €', round (convercao,2))

elif alternativa == 6:
    Vdolar = float(input('Digite quantos Dólares quer converter para Real: '))
    convercao = Vdolar * dolar
    print('O valor US$',Vdolar,' Fica R$', round (convercao,2))