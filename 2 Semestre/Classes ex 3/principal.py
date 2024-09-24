from pais import Pais
from continente import Continente

def main ():

    brasil = Pais('BR','Brasil',214000000,8515767)
    argentina = Pais ('AR','Argentina',46000000,2780400)
    colombia = Pais ('CO', 'Colombia', 52000000,1141748)
    america_do_sul = Continente('America_do_Sul')
    america_do_sul.adiciona_paises(brasil)
    america_do_sul.adiciona_paises(argentina)
    america_do_sul.adiciona_paises(colombia)

    alemanha = Pais('DE','Alemanha',83000000,357022)
    franca = Pais('FR','França',68000000,643801)
    espanha = Pais('ES','Espanha',48000000,505992)
    europa = Continente('Europa')
    europa.adiciona_paises(alemanha)
    europa.adiciona_paises(franca)
    europa.adiciona_paises(espanha)

    nigeria = Pais('NG','Nigéria',223000000,923768)
    egito = Pais('EG','Egito',110000000,1010408)
    africa_do_sul = Pais('ZA','Africa_do_Sul',60000000,1221037)
    africa = Continente('Africa')
    africa.adiciona_paises(nigeria)
    africa.adiciona_paises(egito)
    africa.adiciona_paises(africa_do_sul)


    brasil.adiciona_fronteira('Argentina')
    brasil.adiciona_fronteira('Bolívia')
    brasil.adiciona_fronteira('Colômbia')
    brasil.adiciona_fronteira('Guiana')
    brasil.adiciona_fronteira('Guiana_Francesa')
    brasil.adiciona_fronteira('Paraguai')
    brasil.adiciona_fronteira('Peru')
    brasil.adiciona_fronteira('Suriname')
    brasil.adiciona_fronteira('Uruguai')
    brasil.adiciona_fronteira('Venezuela')
    
    argentina.adiciona_fronteira('Bolívia')
    argentina.adiciona_fronteira('Brasil')
    argentina.adiciona_fronteira('Chile')
    argentina.adiciona_fronteira('Paraguai')
    argentina.adiciona_fronteira('Uruguai')

    colombia.adiciona_fronteira('Brasil')
    colombia.adiciona_fronteira('Equador')
    colombia.adiciona_fronteira('Panamá')
    colombia.adiciona_fronteira('Peru')
    colombia.adiciona_fronteira('Venezuela')

    alemanha.adiciona_fronteira('Áustria')
    alemanha.adiciona_fronteira('Bélgica')
    alemanha.adiciona_fronteira('Dinamarca')
    alemanha.adiciona_fronteira('França')
    alemanha.adiciona_fronteira('Luxemburgo')
    alemanha.adiciona_fronteira('Holanda')
    alemanha.adiciona_fronteira('Polônia')
    alemanha.adiciona_fronteira('República_Tcheca')
    alemanha.adiciona_fronteira('Suíça')

    franca.adiciona_fronteira('Alemanha')
    franca.adiciona_fronteira('Andorra')
    franca.adiciona_fronteira('Bélgica')
    franca.adiciona_fronteira('Itália')
    franca.adiciona_fronteira('Luxemburgo')
    franca.adiciona_fronteira('Mônaco')
    franca.adiciona_fronteira('Espanha')
    franca.adiciona_fronteira('Suíça')

    espanha.adiciona_fronteira('Andorra')
    espanha.adiciona_fronteira('França')
    espanha.adiciona_fronteira('Gibraltar')
    espanha.adiciona_fronteira('Portugal')
    espanha.adiciona_fronteira('Marrocos')

    nigeria.adiciona_fronteira('Benim')
    nigeria.adiciona_fronteira('Camarões')
    nigeria.adiciona_fronteira('Chade')
    nigeria.adiciona_fronteira('Níger')

    egito.adiciona_fronteira('Israel')
    egito.adiciona_fronteira('Israel')
    egito.adiciona_fronteira('Sudão')
    egito.adiciona_fronteira('Faixa_de_Gaza')

    africa_do_sul.adiciona_fronteira('Botsuana')
    africa_do_sul.adiciona_fronteira('Lesoto')
    africa_do_sul.adiciona_fronteira('Moçambique')
    africa_do_sul.adiciona_fronteira('Namíbia')
    africa_do_sul.adiciona_fronteira('Essuatíni')
    africa_do_sul.adiciona_fronteira('Zimbábue')


    alemanha.limitrofe(franca)
    brasil.limitrofe(espanha)

    print('A dencidade populacional da Argentina é de: ',argentina.dencidade())
    print('As fronteiras em comum entre Brasil e Argentina são: ',brasil.vizinhos(argentina))
    print('A dimensao territorial da Africa é de ',africa.dimensao_continente())
    print('A população da Europa é de ', europa.populacao_continente())
    print('A densidade populacional da América do Sul é de: ', america_do_sul.densicade_continente())
    print('O pais com maior população da Europa é ',europa.maior_populacoa())
    print('O pais com menor população da América do Sul é ', america_do_sul.menor_populacao())
    print('O pais com maior dimensão da Africa é ',africa.maior_dimensao().nome)
    print('O pais com menor dimensão da America do Sul é ',america_do_sul.menor_dimensao().nome)
    print('A razão territorial da Europa é ',europa.divisao_territorial())



if __name__ == '__main__':
    main()