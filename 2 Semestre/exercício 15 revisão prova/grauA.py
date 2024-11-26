from grau import Grau

class GrauA(Grau):
    def __init__(self, data_comeco: str, data_fim: str,trabalho:float,prova:float):
        super().__init__(data_comeco, data_fim)

        self.__trabalho = trabalho
        self.__prova = prova
    
    @property
    def trabalho (self):
        return self.__trabalho
    
    @property 
    def prova (self):
        return self.__prova
    
    @trabalho.setter
    def trabalho (self,trabalho):
        self.__trabalho = trabalho
    
    @prova.setter
    def prova (self,prova):
        self.__prova = prova

    def calcula_nota_final_grau (self):
        notaF = (self.trabalho*0.3) + (self.prova * 0.7)
        return notaF
    
    def __str__(self):
        print(f'GrauA(Inicio:{self.data_comeco}, Fim:{self.data_fim})\n',
              f'Trabalho:{self.trabalho}, Prova:{self.prova}')