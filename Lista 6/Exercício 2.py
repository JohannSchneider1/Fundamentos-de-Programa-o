vetor = []
for i in range(0,5):
    valor = int(input('Digite 5 numeros diferentes: '))
    vetor.append(valor)

for j in range(len(vetor)):
    
    resultado = j*vetor[j] #multiplica a Posição do j dentro do vetor com o Valor do j dentro do vetor
    print(resultado)