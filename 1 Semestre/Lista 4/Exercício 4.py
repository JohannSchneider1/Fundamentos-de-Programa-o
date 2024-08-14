#declarando 3 um divisor o inicio e o final do intervalo para ser dividido
divisor = int(input('Entre com o valor do Divisor: '))
inicio = int(input('Inicio do Intervalo: '))
final = int(input('Final do Invervalo: '))

print('Os númeors divisíveis por ',divisor,' no intervalo de ',inicio,' a ' ,final,':')

#loop para que o numero seja dividido começando pelo inicio e terminando no final e sempre adicionando +1 a cada volta
for numero in range (inicio,final+1,+1):
    if numero%divisor == 0: #condição para que possa exibir os numeros que são divididos pelo divisor
        print(numero, end =' / ') #exibindo os numeros tudo na mesma linha e dando uma barra (/) para diferenciar cada número divisível 