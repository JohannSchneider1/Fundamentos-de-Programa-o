#gardando em uma variavel o valor da peça
peca = float(input('Digite o valor da peça de roupa em Reais: '))

#calculando o valor do desconto e depois subtraindo para ter o valor da peça com o desconto de 15%
desconto = peca * 15/100
valor = peca - desconto

#exibindo o valor atual da peça o desconto que é conseguido e também quanto a peça custa com o desconto
print('A peça que custa R$ ',peca,'consegue um desconto de R$ ',desconto,'\nEntão no total a peça custa R$ ',valor)