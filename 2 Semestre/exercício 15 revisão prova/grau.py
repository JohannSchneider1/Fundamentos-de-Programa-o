class Grau:
    def __init__(self,data_comeco:str,data_fim:str):
        self.__data_comeco = data_comeco
        self.__data_fim = data_fim
    
    @property
    def data_comeco (self)->str:
        return self.__data_comeco
    
    @property
    def data_fim (self)->str:
        return self.__data_fim

    @data_comeco.setter
    def data_comeco (self, data_comeco)->str:
        self.__data_comeco = data_comeco
    
    @data_fim.setter
    def data_fim (self,data_fim)->str:
        self.__data_fim = data_fim
    
    def __str__(self)->str:
        print(f'Grau(Inicio:{self.data_comeco}, Fim:{self.data_fim})')