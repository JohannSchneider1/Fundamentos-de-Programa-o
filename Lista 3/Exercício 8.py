#Variavel de entrada para saber o valo do produto
produto = float(input('Digite o valor do produto: '))

#Condição para decidir qual a % de lucros que o vendedor irá conseguir em comparação ao valor do produto
if produto < 20:
    lucro = produto *45/100
    VPlucro = produto + lucro
    print('O valor de venda é de: R$',VPlucro)
elif produto >=20 and produto <= 50:
    lucro = produto *35/100
    VPlucro = produto + lucro
    print('O valor de venda é de: R$', VPlucro)
else:
    lucro = produto *25/100
    VPlucro = produto + lucro
    print('O valor de venda é de: R$',VPlucro)