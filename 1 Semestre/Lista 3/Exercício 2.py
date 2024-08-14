#Declarando variaveis A B C e colocando uma variavel de entrada
VarA = float(input('Digite um número para a letra A: '))
VarB = float(input('Digite um número para a letra B: '))
VarC = float(input('Digite um número para a letra C: '))

#Somando os valores colocados 
SomaAB = VarA + VarB
SomaAC = VarA + VarC

#Colocando uma condição para aparecer a soma no visor
if SomaAB<SomaAC:
    print('A soma de A+B: ',SomaAB,' é menor que a soma A+C', SomaAC)