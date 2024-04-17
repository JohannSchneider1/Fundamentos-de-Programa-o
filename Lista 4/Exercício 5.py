#variavel de entrada para saber a quantidade de alunos
quantidade = int(input('Digite a quantidade de aludos: '))

#fazendo com que 2 variaveis tenham o mesmo valor
cont = quantidade

media = 0

while cont>0: # utilizando uma das variaveis e fazendo o loop

    grauA = float(input('Digite a nota do Grau A: ')) #variavel para as notas do grau A e B
    grauB = float(input('Digite a nota do Grau B: '))

    nota = (grauA + 2*grauB)/3 #calculando a média

    if nota>=6: #condição para conferir se passou 
        print('Passou com ',round(nota,2))
        
    else: # caso a condição de sima não seja verdadeira execute
        troca = int(input('Aprete 1 para trocar a nota do Grau A\nAperte 2 para trocar a nota do Grau B\n'))#variavel para decidir qual nota será substituida

        if troca == 1:# condição para caso for a 1 escolha
            grauC = float(input('Digite a nota do Grau C: ')) #variavel de entrada para guardar a nota
            nota = (grauC + 2*grauB)/3 #calculando a média novamente

            if nota>=6:#condição para saber se passo ou não
                print('Passou com ',round(nota,2))
                

            else:
                print('Reprovou com ',round(nota,2))
                
        else: #Caso não escolha o 1 
            grauC = float(input('Digite a nota do Grau C: ')) #variavel de entrada para guardar a nota
            nota = (grauA + 2*grauC)/3#calculando a média novamente

            if nota>=6:#condição para saber se passo ou não
                print('Passou com ',round(nota,2))
                
            else:
                print('Reprovou com ',round(nota,2))

    media = media + nota #fazendo com que a nota seja armazenado na media inicial 0+nota1 depois nota1+nota2 = resultado1 depois resultado2 = resultado1 + nota3 e assim vai
    total = media/quantidade #sabendo a média total dos alunos
    cont = cont - 1 #condição de saida do loop

#Exibindo a média total dos alunos
print('A média dos alunos foi de ',round(total,2))