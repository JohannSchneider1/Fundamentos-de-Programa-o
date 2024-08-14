frase = input('Digite um texto: ')

vogais = ['a','A','i','I','u','U','e','E','o','O']

cont= 0

for n in frase: #navega pela variavel frase caracter por caracter
    for j in vogais: #navega pela Matriz caracter por caracter

        if n == j: #se o caracter dentros das duas variaveis forem o mesmo
            cont = cont +1 #adicione 1 no contador

    
print('A palavra: ',frase,' tem: ')
print(cont,' Vogais')