#Criando a variavel Pergunta e colocando em um comando de entrada para poder fazer qualquer pergunta
pergunta = input('Digiite a sua pergunta:\n')

#Criando as variáveis de entrada para ser colocado qualquer alternativa
LetraA = input('Digite a alternativa A: \n')
LetraB = input('Digite a alternativa B: \n')
LetraC = input('Digite a alternativa C: \n')
LetraD = input('Digite a alternativa D: \n')
LetraE = input('Digite a alternativa E: \n')

#Criando uma variável com comando de entrada só para a resposta das alternativas que foram colocado anteriormente
Resposta = input('Digite a letra certa: \n')

#Colocando comando de saida com a pergunta realizada e as alternativas que fora geradas
print(pergunta)
print('\n')
print('Letra A: ', LetraA)
print('Letra B: ', LetraB)
print('Letra C: ', LetraC)
print('Letra D: ', LetraD)
print('Letra E: ', LetraE)

#Comando de entrada novamente para registrar a alternativa que acha que é certa na variável Questão
Questão = input('Digite a alternativa certa: ')

#Criando o comando de saida para mostrar o que foi digitado e comparar com a resposta certa
print('Você digitou: ',Questão,'\nA resposta é: ',Resposta)