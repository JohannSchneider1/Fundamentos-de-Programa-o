#Variavel de entrada para saber qual o salário que sera calculado
salario = float(input('Digite o valor de seu salário: '))

#fazendo o desconto de 11%
desconto = salario *11/100

#Colocando uma condição que se o desconto for menor que 318,20 será o desconto de 11% caso contrario será o valor maximo
if desconto < 318.20:
    VCdesconto = salario - desconto
else:
    VCdesconto = salario - 318.20

#variavel de saida mostrando ao usuário o valor com o desconto já incluso
print('O todal com desconto foi de: R$', VCdesconto)