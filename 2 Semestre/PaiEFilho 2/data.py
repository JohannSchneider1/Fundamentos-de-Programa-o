class Data ():
    def __init__(self,dia,mes,ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    @property
    def dia (self):
        return self.__dia

    @property
    def mes (self):
        return self.__mes
    
    @property
    def ano (self):
        return self.__ano
    
    @dia.setter
    def dia (self,dia):
        self.__dia = dia
    
    @mes.setter
    def mes (self,mes):
        self.__mes = mes
    
    @ano.setter
    def ano (self,ano):
        self.__ano = ano
    
    def imprime_data (self):
        print(f'data: {self.dia} / {self.mes} / {self.ano}')