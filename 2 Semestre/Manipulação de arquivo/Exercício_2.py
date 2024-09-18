def main ():
    texto = open('cadastro.txt','r')
    leitura = texto.readlines()
    pessoa = list(leitura)
    texto.close()

    nome = pessoa [0]
    idade = pessoa[1]
    altura = pessoa [2]
    peso = pessoa [3]

    print(nome,idade,altura,peso)

if __name__ == '__main__':
    main()
