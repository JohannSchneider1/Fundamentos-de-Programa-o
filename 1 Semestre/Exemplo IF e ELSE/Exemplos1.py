#Declando uma variavel inteira e colocando um numero dentro dela
a = int(input('Digite um valor de numero inteiro: '))

#comparando a variavel se ela for (Verdadeira) ira por um caminho se for(Falsa)irá por outro caminho famoso(IF/ELSE)
#Se a variavel A for menor que 10 aparecerá o primeito print
if a > 10:
    print('É maior que 10!')
    #Vai pegar a variavel A, adicionar 10 e reescrever dentro dela o novo valor
    a = a + 5

#Se A for menor ou igual a 10 irá executar o print do else
else:
    print('Valor menor ou igual a 10')
    #Vai pegar a variavel A, adicionar 10 e reescrever dentro dela o novo valor
    a = a+10

#exibindo o novo valor de A FORA do (IF/ELSE)
print('Novo valor dor A é: ',a)

#utilizando o elif para criar uma nova condição e ver se ela é verdadeira, de não conrinua.
if a==10:
     print('Igual a 10')

elif a>10:
     print('Maior que 10')

else:
     print('Menor que 10')
