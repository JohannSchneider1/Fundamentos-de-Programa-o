#Variavel de entrada para saber a idade a ser calculada
idade = int(input('Digite a sua idade para calcularmos o valor do convenio a ser pago: '))

#condição em relação a variavel idade, cada condição da um valor diferente
if idade < 10:
    valor = 100
elif idade >= 10 and idade <= 30:
    valor = 220
elif idade >= 31 and idade <= 60:
    valor = 395
else: 
    valor = 480

#calculo do valor mais os 300 reais fixos
total = 300 + valor

#Exibindo o valor total a ser pago do convenio apois calcular a o valor em relação a idade
print('O total a se pagar é de: R$',total)