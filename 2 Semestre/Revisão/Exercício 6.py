solteiras = []
casadas = []
divorciadas = []
viuvas = []
for n in range (0,20):
    nome = input('Digite o seu nome: ')
    estado = input('Digite o seu estado civil utilizando as abreviações: \nS = solteiro(a)\nC = casado(a)\nD = divolciado(a)\nV=viuvo(a): \n')
    
    if estado == 's':
        solteiras. append(nome)

    elif estado == 'c':
        casadas. append(nome)

    elif estado == 'd':
        divorciadas. append(nome)

    elif estado == 'v':
        viuvas. append(nome)

print('As pessoas solteiras são:')
for n in solteiras:
    print(n)

print('As pessoas casadas são:')
for c in casadas:
    print(c)

print('As pessoas divorciadas são: ')
for d in divorciadas:
    print(d)

print('As pessoas viuvas são:')
for v in viuvas:
    print(v)