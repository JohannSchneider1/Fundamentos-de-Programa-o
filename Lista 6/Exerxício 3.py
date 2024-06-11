import random

dado = [0]*6

n = int(input('Digite quantas vezes quer jogar o dado: '))

#vai sortear um numero até que sorterie o valor de n e vai adicionando dentro do Array para que possa se calcular a porcentagem depois
for j in range(n):
    sorteio = random.randint(1,6)

    if sorteio == 1:
        dado[0] = dado[0] + 1
    elif sorteio ==2:
        dado[1] = dado[1]+1
    elif sorteio ==3:
        dado[2] = dado[2]+1
    elif sorteio ==4:
        dado[3] = dado[3]+1
    elif sorteio ==5:
        dado[4] = dado[4]+1
    elif sorteio ==6:
        dado[5] = dado[5]+1

print('A porcentagem de vezes que caiu no numero 1 foi de: ',(dado[0]*100)/n,'%') #calculo da porcentagem direto na impreção para evitar salval em uma variavel desnecessária
print('A porcentagem de vezes que caiu no numero 2 foi de: ',(dado[1]*100)/n,'%')
print('A porcentagem de vezes que caiu no numero 3 foi de: ',(dado[2]*100)/n,'%')
print('A porcentagem de vezes que caiu no numero 4 foi de: ',(dado[3]*100)/n,'%')
print('A porcentagem de vezes que caiu no numero 5 foi de: ',(dado[4]*100)/n,'%')
print('A porcentagem de vezes que caiu no numero 6 foi de: ',(dado[5]*100)/n,'%')

print(dado)