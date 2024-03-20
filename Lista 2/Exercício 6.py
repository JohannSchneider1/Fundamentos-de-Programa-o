#Guardando em variaveis a quantidade de produtos vendidos
smart = int(input('Digite quantos smartphones foram vendidos: '))
tablet = int(input('Digite quantos tablets foram vendidos: '))

#Calculando quanto em reais foi vendido
totalsm = smart*1000
totalta = tablet*1500
total = totalsm + totalta

#Mostrando o valor total que foi arrecadado
print('O valor total de smartphone e tablets vendido foi de R$ ',total,'\nSendo R$ ', totalsm,' em smartphone\nE R$ ', totalta,' em tablet')