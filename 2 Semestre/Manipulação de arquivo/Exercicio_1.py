def main ():
    pessoa = []
    nome = input('Digite seu nome completo: ')
    idade = input('Digite sua idade: ')
    altura = input('Digite sua altura: ')
    peso = input('Digite seu peso: ')

    pessoa.append(nome)
    pessoa.append(idade)
    pessoa.append(altura)
    pessoa.append(peso)

    #texto = open('cadastro.txt','w')
    #texto.writelines(pessoa)
    #texto.close ()
    texto = open('cadastro.txt','w')
    texto.write('\n'.join(pessoa))
    texto.close ()

if __name__ == '__main__':
    main()