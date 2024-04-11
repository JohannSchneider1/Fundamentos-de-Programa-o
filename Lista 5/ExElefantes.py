########## Funções ##########
#Criando uma variavel para cantar a musica e ficar repetindo toda hora igual ao numero desejado
def musica_elefantes (n):
    #criando um loop com o for onde começa no 1 e vai até o numero desejado
    for i in range(1,n):
        #exibindo a variavel i
        print(i,' Elefante(s) incomoda(m) muito agente,')
        #exibindo a variavel i e adicionando +1 e escrevendo elefantes e terminando na mesma linha
        print (i+1,' Elefantes ', end = '')
        #Criando outro loop dentro do anterior, onde armagena na variavel J, iniciando do 1 até o i+1
        for j in range(1,i+1):
            #exibindo na tela até a quantidade de vezes que foi adicionadas na variavel i e encerrando na mesma linha
            print (', Incomodam, ', end = '')
        #exibindo a palavra
        print('muito mais!')

########## Programa Principal ##########
#Armazenando em uma variavel um numero inteiro
numero = int(input('digite um numero: '))
#Chamando a função criada anteriomente e executando o comando sendo o numero o N da função
musica_elefantes(numero)