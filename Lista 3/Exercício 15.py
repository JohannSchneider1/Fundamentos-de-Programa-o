#variavel de entrada para saber o valor do produto
produto = float(input('Digite o valor do produto: '))

#exibindo as alternativas possiveis para a conpra e no filar guardando em uma variavel
print('Qual das formas de pagamento a seguir você deseja?')
print('1 - À vista em dinheiro, recebe (15%) de desconto\n2 - À vista no cartão de crédito, recebe (10%) de desconto\n3 - Em duas vezes, preço normal de etiqueta sem juros\n4 - Em três vezes, preço normal de etiqueta mais (10%) de juros')
alternativa = int(input('Digite o numero da alternativa desejada: '))

#condição para a variavel alternativa para saver qual o valor total a ser pago do produto
if alternativa == 1:
    desconto = produto * 15/100
    valor = produto - desconto

elif alternativa == 2:
    desconto = produto *10/100
    valor = produto - desconto

elif alternativa == 3:
    valor = produto/2

elif alternativa == 4:
    juros = produto * 10/100
    total = produto + juros
    valor = total/3

# condição para não confundir, caso queria parcelar e exibindo na tela o valor a ser pago, ja modificado
if alternativa == 3:
    print('O produto será parcelado em 2 vezes e terá o preço de: R$',valor,' Cada parcela')

elif alternativa == 4:
    print('O produto será parcelado em 3 vezes e terá o preço de: R$',valor,' Cada parcela totalizando: R$',total)

else:
    print ('O valor a ser pago é de: R$',valor)