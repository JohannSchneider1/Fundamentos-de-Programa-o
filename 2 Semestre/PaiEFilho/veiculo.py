class Veiculo():
    def __init__(self,ano:int,peso:int,tanque:float,modelo:str):
        self.__ano = ano
        self.__peso = peso
        self.__tanque = tanque
        self.__modelo = modelo
    
    @property
    def ano (self):
        return self.__ano
    
    @property
    def peso (self):
        return self.__peso
    
    @property
    def tanque (self):
        return self.__tanque
    
    @property
    def modelo (self):
        return self.__modelo
    
    @ano.setter
    def ano (self,ano):
        self.__ano = ano
    
    @peso.setter
    def peso (self,peso):
        self.__peso = peso
    
    @tanque.setter
    def tanque (self,tanque):
        self.__tanque = tanque

    @modelo.setter
    def modelo (self,modelo):
        self.__modelo = modelo

    def info(self):
        print(f'Ano: {self.ano}')
        print(f'Peso: {self.peso}')
        print(f'Tanque: {self.tanque}')
        print(f'Modelo: {self.modelo}')
        