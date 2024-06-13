#Cria um arquivo vazio se não existir ou APAGA 
#O conteudo de um arquivo existente para escrita
#da para criar cum uma variavel
nomeArquivo = 'teste.txt'

arqEscrita = open('teste.txt','w') #apaga o conteudo existente e escreve por cima

arqEscrita.write('\nSalve pessoal')

arqEscrita.close()
#Cria um arquivo se não existir ou MANTÉM
#O conteudo de um arquivo existente para a escrita

arqEscrita = open(nomeArquivo,'a') #Continua escrevendo do lado onde parou não apaga nada

arqEscrita.write('\n15\n')

numero = 15

arqEscrita.write(str(numero))
arqEscrita.write(str(15+15))

arqEscrita.close()


arqEscrita = open(nomeArquivo,'a')

numero = 65
arqEscrita.write(chr(numero))


arqEscrita.close()
