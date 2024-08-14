cont = 0
while cont < 6:
    senha = input('Crie sua senha que tenha de 5 a 10 cadacteres: ')
    numeros = senha.isdigit()
    quantidade = len(senha)


    if quantidade>= 5 and quantidade<=10 and numeros == True:
        cont = cont + 7
        print('sucesso')

    else:
        cont = cont +1
        print('Tente novamente, você ainda tem mais ',6-cont,' tentativas')