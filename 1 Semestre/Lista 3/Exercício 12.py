#variavel de entrada para descobrir a idade dos participantes
idade = int(input('Digite a idade do candidato: '))

#condição para saber em qual categoria o participante deverá competir
if idade>=5 and idade<=7:
    print('Infantil A')
elif idade>=8 and idade <=10:
    print('Infantil B')
elif idade >=11 and idade<=13:
    print('Juvenil A')
elif idade >=14 and idade<=17:
    print('Juvenil B')
elif idade >= 18:
    print('Sênior')