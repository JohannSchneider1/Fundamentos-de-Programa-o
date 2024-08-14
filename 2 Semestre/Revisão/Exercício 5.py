quantidade = int(input('Digite quantos itens irá na lista: '))

lista = []
while quantidade > 0:
    conteudo = input('Digite o produto: ')

    lista.append(conteudo) # para utilizar o append 1 coloca onde tu vai acrecentar  e depois coloca o que tu quer acrecentar


    quantidade = quantidade -1


for n in lista:
    print(n)