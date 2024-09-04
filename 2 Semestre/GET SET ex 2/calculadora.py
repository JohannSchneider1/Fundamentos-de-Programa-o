class Calculadora:
    def __init__(self,cor, memoria):
        self.__memoria = memoria
        self.__cor = cor

    @property
    def memoria (self):
        return self.__memoria
    
    @memoria.setter
    def memoria (self,memoria):
        self.__memoria = memoria
    
    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self,cor):
        self.__cor = cor

    def soma (v1:float, v2:float):
        resultado = v1 + v2
        return resultado
    
    def subtracao (v1:float, v2:float):
        resultado = v1 - v2
        return resultado
    
    def multiplica (v1 : float, v2 : float):
        resultado = v1 * v2
        return resultado
    
    def divisao (v1 : float, v2 : float):
        resultado = v1/v2
        return resultado
    
    def eleva_ao_quadrado (v1 : int):
        resultado = v1**2
        return resultado
    
    def eleva_ao_cubo(v1 : int):
        resultado = v1**3
        return resultado
    
    def imprime_info (self):
        print('Sua calculadora tem: ',self.memoria,' Memoria')
        print('Sua calculadora tem a cor: ',self.cor)


def main():
    memoria = int(input('Digite quanto de memoria tem a sua calculadora: '))
    cor = input('Digite qual a cor de sua calculadora: ')
    
    r = Calculadora(cor,memoria)
    r.imprime_info()

if __name__ == '__main__':
    main()