senhacadastrada= 123 #simula a senha que o usuario avia cadastrado

#Duas variaveis que serão utilizadas dentro do While para a senha
cont=0
senha = ''

#loop enquanto o contador for diferente de 3 E a senha n foi a verdadeira execute
#Se senha for verdaderira termine o loop e exiba
#se contador for igual a = termine o loop e exiba
while cont!=3 and senha!=senhacadastrada:
    senha=float(input('Digite a senha: '))
    cont=cont+1

    if senha == senhacadastrada:
        print('Parabéns você entrou!!')

    elif cont ==3 :
        print('Meus pesames, você esgotou o número de tentativas')
    


