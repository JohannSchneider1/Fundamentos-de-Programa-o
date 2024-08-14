valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um segundo valor: '))

if valor1<valor2:
    for n in range(valor1,valor2+1):
        print(n)

if valor1>valor2:
    for n in range(valor2,valor1+1):
        print(n)