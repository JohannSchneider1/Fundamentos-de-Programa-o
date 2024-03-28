sexo = 'F'
idade = 65

#Testa se a variavel sexo é feminino
if sexo == 'F':
    #Aqui estatão as ações que devem executar se a avaliação do if for veradadeira
    print('É do sexo Feminino')
    if idade >=65:
        print('Possui 65 anos, ou mais, de idade')
    else:
        print('Possui menos de 65 anos de idade')

#Aqui estatão as ações que devem executar se a avaliação do if for falsa   
else:
    print('É do sexo Mascolino')


if sexo == 'F' and idade >=65:
    print('É uma pessoa do sexo Feminino com mais de 65 anos.')


#################
nota = 6.0
frequencia = 0.75

#Testando usando OR
if nota<6.0:
    print('Reprovado por média')
elif frequencia<0.75:
    print('Reprovado por faltas!')
else:
    print('Aprovado!')

if nota<6.0 or frequencia<0.75:
    print('Reprovado')
