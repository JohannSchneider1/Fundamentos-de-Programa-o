import csv

#função que é o exercício 2
def leitura_do_arquivo():
    #lendo o arquivo e retirando informações
    with open ('file.csv') as file: # abrindo o arquivo
        leitura = csv.reader(file, delimiter = ',') #lendo o arquivo csv que está delimitado o campos com a ,
 
        informacao = [] #array para as informações do arquivo

        for i in leitura: # infinito para varrer o arquivo csv
            lido=[] # array auxiliar para que depois possa ser implementado no array das informações
            #colocando o valor de i nas respectivas colunas no array LIDO 
            lido.append(i[0]) 
            lido.append(i[1])
            lido.append(i[2])
            lido.append(i[3])
            lido.append(i[4])
            #colocando os valores obtidos no arquivo csv que foram passado para o array lido no array informação
            informacao.append(lido)

    #pegando o numero de linhas da matriz informação
    tamanho = len(informacao)

    #letra A
    #colocando mais uma coluna na matriz informação
    informacao[0].append('desempenho')
    for i in range(1,tamanho): #laço de repetição que vai do 1 até o numero de linhas da matriz informação
        d = 10**6 / (float(informacao[i][1]) * 100 + float(informacao[i][2]) + float(informacao[i][3]) + float(informacao[i][4])) #calculo para descobrir o desempenho (esta no exercicio)
        informacao[i].append(d)#colocando os resultados do calculo na matriz informação na linha que do valor de i assim gerando a coluna do desempenho
        print('linguagem: ',informacao[i][0],'   Desempenho: ', round(informacao[i][5],2)) #printando a posição da linguagem e a posição arredondada do valor do desempenho
    
    #letra B
    cpu = 0
    memoria = 0
    tempo = 0
    linha = 0
    desempenho = 0
    for i in range(1,tamanho): #laço de repetição que vai do 1 até o numero de linhas da matriz informação
        #somando todos os valores das respectivas colunas
        cpu = cpu + float(informacao[i][1])
        memoria = memoria  + float(informacao[i][2])
        tempo = tempo + float(informacao[i][3])
        linha = linha  + float(informacao[i][4])
        desempenho = desempenho  + float(informacao[i][5])
    
    #exibindo o nome da metrica nas respectivas colunas e a média dividindo o que foi somado pela quantidade de vezes que foi somado
    print('metrica: ',informacao[0][1],'   Média: {:.3f}'.format(cpu/tamanho)) #print('{:.3f}'.format(variavel)) outra forma para arredondar um valor sem utilizar round(variavel,2)
    print('metrica: ',informacao[0][2],'    Média: {:.3f}'.format(memoria/tamanho))
    print('metrica: ',informacao[0][3], '   Média: {:.3f}'.format(tempo/tamanho))
    print('metrica: ',informacao[0][4],'    Média: {:.3f}'.format(linha/tamanho))
    print('metrica: ',informacao[0][5],'    Média: {:.3f}'.format(desempenho/tamanho))

    #letra C
    maior = -1
    for i in range(1,tamanho):#laço de repetição que vai do 1 até o numero de linhas da matriz informação
        if maior<informacao[i][5]: # condição que se o valor na posição i da coluna 5 for maio que a variavel(maior) execute:
            maior = informacao[i][5] #variavel (maior) receberá o valor na posição i da coluna 5 assim conseguindo o maior desempenho
            print('Linguagem com Melhor desempenho: ',informacao[i][0]) # printando a linguagem com melhor desempenho

    #letra D
    menor = 600
    for i in range(1,tamanho): #laço de repetição que vai do 1 até o numero de linhas da matriz informação
        #obs.: por algum motivo na coluna 4 o python esta considerando como str e não numeros então coloca float para que o python interprete como numero os valores na posição i
        if menor>float(informacao[i][4]): #condição que se o valor na posição i da coluna 4 for menor que a variavel(menor) execute:
            menor = float(informacao[i][4]) ##variavel (menor) receberá o valor na posição i da coluna 4, como numero, assim conseguindo o menor numoer de linhas
            print('Linguagem com Menor quantidade de linhas: ',informacao[i][0])#printando a linguagem com o menor numero de linhas
        

#fazendo com que começa a execução com a função leitura_do_arquivo
if __name__ == '__main__':
    leitura_do_arquivo()