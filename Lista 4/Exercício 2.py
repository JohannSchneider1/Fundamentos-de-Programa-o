#importando a biblioteca aleatória
import random

#gerando um numero aleatório
aleatorio = random.randint(1,10)
tentativa = 0
numero =0
print('Com apenas 3 tentativas')

while tentativa<3 and numero != aleatorio: #loop sendo executado se o numero de tentativas for menor que 3 e se o usuario está errando o numero
    tentativa = tentativa + 1 #umas das condição para sair do loop
    numero=int(input('Adivinhe o número de 1 à 10: ')) #segunda tentativa para sair do loop

    if numero > aleatorio: #se numero for menor que o numero sorteado
        print(numero, ' É maior que o numero sorteado') #exiba o numero que colocou e o texto

    elif numero < aleatorio: #se numero for maior que o numero sorteado
        print(numero, ' É menor que o numero sorteado')#exiba o numero que colocou e o texto

if tentativa == 3: # se tentativas for 3
    print('Suas tentativas acabaram, o número sorteado foi: ',aleatorio) # exiba o testo e o numero aleatorizado
elif numero == aleatorio: # se acertar o número aleatorizado
    print('Parabéns você acertou o número em: ',tentativa,' tentativa(s)') # exiba o texto e em quantas tentativas ele conseguiu