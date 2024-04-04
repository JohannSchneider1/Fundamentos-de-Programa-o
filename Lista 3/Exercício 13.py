#Duas variavei de entrada para a nota do grau A e grau B
notaA = float(input('Digite a nota do Grau A: '))
notaB = float(input('Digite a nota do Grau B: '))

#fazendo os calculos da media
notaT = (notaA + 2*notaB)/3

#exibindo a nota arredondada
print(round(notaT,1))

#condição para saber se o usuário passou ou não na materia
if notaT>=6:
    print('Parabém você passou por nota')
elif notaT<6:
    print('Você não pasosu por nota')
    print('Você gostaria de substituir a nota do Grau A ou Grau B')
    #se ele não passou, deverá informa qual nota quer mudar e salvar em uma variavel a outra variavel é para digitar a nota nova
    alternativa = input('Digite (A) para Grau A e (B) par grau B: ')
    notaC = float(input('Digite a nota do Grau C: '))

    # condição se escolheu A alterará a nota do Grau A e vera se ele passou ou não
    if alternativa == 'a':
        notaT = (notaC + 2*notaB)/3
        round(notaT,1)
        if notaT>=6:
            print('Parabéns, conseguiu se recuperar, ficou com: ',round(notaT,1))
        else:
            print('Meu pesames, mas você não recuperouficou com: ',round(notaT,1))


    # condição se escolheu B alterará a nota do Grau B e vera se ele passou ou não
    elif alternativa == 'b':
        notaT = (notaA + 2*notaC)/3

        if notaT>=6:
            print('Parabéns, conseguiu se recuperar, ficou com: ',round(notaT,1))
        else:
            print('Meu pesames, mas você não recuperou, ficou com: ',round(notaT,1))
