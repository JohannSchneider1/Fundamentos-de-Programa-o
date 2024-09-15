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

    def soma (self,v1:float, v2:float):
        resultado = v1 + v2
        return resultado
    
    def subtracao (self,v1:float, v2:float):
        resultado = v1 - v2
        return resultado
    
    def multiplica (self,v1 : float, v2 : float):
        resultado = v1 * v2
        return resultado
    
    def divisao (self,v1 : float, v2 : float):
        resultado = v1/v2
        return resultado
    
    def eleva_ao_quadrado (self,v1 : int):
        resultado = v1**2
        return resultado
    
    def eleva_ao_cubo(self,v1 : int):
        resultado = v1**3
        return resultado
    
    def imprime_info (self):
        print('=========Dados da Calculadora===========')
        print('Sua calculadora tem: ',self.memoria,' Memoria')
        print('Sua calculadora tem a cor: ',self.cor)
        print('========================================')
    