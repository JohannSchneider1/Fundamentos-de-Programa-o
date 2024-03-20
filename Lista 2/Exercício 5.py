#Ler quanto que esta a gasolina e quanto que o usuario quer gastar
preco = float(input('Digite o preco da gasolina: '))
quantidade = float(input('Digite quantos reais tu quer abastecer: '))

#Calcular o valor da gasolina dividindo a quantidade desejada
Litros = quantidade / preco

#variavel de saida respondendo quantos litros irá ter no carro
print('No total fica ', Litros,'Litros', round(Litros,2))