#Perguntando ao usuário quanto que ele conseguiu em cada Grau
nota1 = float(input('Digite a nota do Grau A: '))
nota2 = float(input('Digite a nota do Grau B: '))

#Calculando as notas
Resultado = (nota1 + 2*nota2)/3

#Mostrando o resultado
print('O Resultado que você conseguiu foi: ',round (Resultado,2))