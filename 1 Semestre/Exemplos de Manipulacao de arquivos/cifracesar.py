def cifraMensagem(msg):
    msgCifrada = ''
    for i in range(len(msg)):
        code = ord(msg[i]) - 1
        msgCifrada = msgCifrada + chr(code)
    
    return msgCifrada

def decifraMensagem(msgCifrada):
    msgDecifrada = ''
    for i in range(len(msgCifrada)):
        code = ord(msgCifrada[i]) + 1
        msgDecifrada += chr(code) #da para utilizar este operador ao invé de escrever msgDecifrada  = msgDecifrada  +  chr(code)
    return msgDecifrada

#####################################################

mensagem = input('Digite uma mensagem: ')

msgCifrada = cifraMensagem(mensagem)

print(msgCifrada)

#Salvar a mensagem cifrada em um arquivo

nomeArq = input('Digite um nome do arquivo que deseja salvar: ')

arqSaida = open(nomeArq, 'w')

arqSaida.write(msgCifrada)

arqSaida.close()

#Ler o arquivo com a mensagem cifrada e decifrar a mensagem

nomeArq = input('Digite um nome do arquivo que deseja abrir: ')

arqEntrada = open(nomeArq, 'r')

mensagemCifrada = arqEntrada.read() #Armazena todo o conteudo do arquivo em uma string

arqEntrada.close()

mensagemDecifrada = decifraMensagem(mensagemCifrada)

print (mensagemDecifrada)