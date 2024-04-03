valor = int(input('Digite quandos reais tem que passar de troco: '))

#if valor/100!=0:
#    QN = valor / 100
#    print('Deverá utilizar ',QN,' Notas de R$ 100,00')

#elif valor/50!=0:
#    QN = valor / 50
#    print('Deverá utilizar ',QN,' Notas de R$ 50,00')

cont = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0

while valor!=0:
    if valor >= 100:
        valor = valor - 100
        cont = cont +1
        print('Deverá utilizar ',cont,' Notas de R$ 100,00')
        
    elif valor >= 50:
        valor = valor - 50
        cont1 = cont1 +1
        print('Deverá utilizar ',cont1,' Notas de R$ 50,00')
        
    elif valor >= 20:
        valor = valor - 20
        cont2 = cont2 +1
        print('Deverá utilizar ',cont2,' Notas de R$ 20,00')
        
    elif valor >= 10:
        valor = valor - 10
        cont3 = cont3 +1
        print('Deverá utilizar ',cont3,' Notas de R$ 10,00')
        
    elif valor >= 5:
        valor = valor - 5
        cont4 = cont4 +1
        print('Deverá utilizar ',cont4,' Notas de R$ 5,00')

    elif valor >= 1:
        valor = valor - 1
        cont5 = cont5 +1
        print('Deverá utilizar ',cont5,' Notas de R$ 1,00')

    else:
        valor = 0