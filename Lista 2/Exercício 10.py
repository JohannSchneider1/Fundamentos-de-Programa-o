#Declarando variaveis para cada peça de roupa
camisetas = int(input('Iforme o número total de camisetas que o cliente comprou: '))
calcas = int(input('Iforme o número total de calças que o cliente comprou: '))
cintos = int(input('Iforme o número total de cintos que o cliente comprou: '))

#declarando outras variaveis e colocando os calculos dentro dela de quanto vale cada peça
Vcamisa = camisetas *25
Vcalcas = calcas*100
Vcinto = cintos *40
Vtotal = Vcamisa + Vcalcas + Vcinto

#Calculando o total de desconto que o cliente conseguiu
Desconto = Vtotal *10/100
VCdesconto = Vtotal - Desconto

#Exibindo na tela os valores que foi adquirido
print('O clirente gastou:\nR$',Vcamisa,'em camisas\nR$',Vcalcas,'em calças\nR$',Vcinto,'em cinto\nO desconto foi de R$ ',Desconto)
print('Logo ao invés de gastar R$ ',Vtotal,'\nO Cliente gastou um total de R$ ',VCdesconto)