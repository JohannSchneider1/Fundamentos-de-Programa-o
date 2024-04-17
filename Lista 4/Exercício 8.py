alternativa = 's'

while alternativa != 'n':

    numero = int(input('Digite um número para realizar o farotial: '))
    resultado = 1
    
    for n in range(1,numero+1):
        resultado = resultado * n

    print(resultado)

    alternativa = input('Deseja continuar? (S/N) ')