#Variavel de entrada para saber o valor
valor = int(input('Digite quandos reais tem que passar de troco: '))

#algund contadores que serão utilizados no while para saber quantas notas será utilizada em cada valor
cont = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0

#loop enquanto o valor não for zero execute os if's que estão dentro, cada if irá reduzir o valor em uma quantidade e contar quantas vezes foram utilizadas
while valor!=0:
    if valor >= 100:
        valor = valor - 100
        cont = cont +1
        
    elif valor >= 50:
        valor = valor - 50
        cont1 = cont1 +1
        
    elif valor >= 20:
        valor = valor - 20
        cont2 = cont2 +1
        
    elif valor >= 10:
        valor = valor - 10
        cont3 = cont3 +1
        
    elif valor >= 5:
        valor = valor - 5
        cont4 = cont4 +1

    elif valor >= 1:
        valor = valor - 1
        cont5 = cont5 +1

    else:
        valor = 0

#Condição se as variavels cont's forem diferente de 0 exiba cada frase
if cont!=0:
    print('Deverá utilizar ',cont,' Notas de R$ 100,00')

if cont1!=0:
    print('Deverá utilizar ',cont1,' Notas de R$ 50,00')

if cont2!=0:
    print('Deverá utilizar ',cont2,' Notas de R$ 20,00')

if cont3!=0:
    print('Deverá utilizar ',cont3,' Notas de R$ 10,00')

if cont4!=0:
    print('Deverá utilizar ',cont4,' Notas de R$ 5,00')

if cont5!=0:
    print('Deverá utilizar ',cont5,' Notas de R$ 1,00')