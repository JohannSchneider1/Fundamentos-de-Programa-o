from grau import Grau

class GrauB (Grau):
    def __init__(self, data_comeco: str, data_fim: str,atividades:float, seminario:float, participacao:float):
        super().__init__(data_comeco, data_fim)
        self.__atividades = atividades
        self.__seminario = seminario
        self.__participacao = participacao
    
    @property
    def atividades (self):
        return self.__atividades
    
    @property
    def seminario (self):
        return self.__seminario
    
    @property
    def participacao (self):
        return self.__participacao

    @atividades.setter
    def atividades (self,atividades):
        self.__atividades = atividades
    
    @seminario.setter
    def seminario (self,seminario):
        self.__seminario = seminario
    
    @participacao.setter
    def participacao (self,participacao):
        self.__participacao = participacao

    def calcula_nota_final_grau (self):
        notaF = (self.atividades*0.3) + (self.seminario * 0.6) + (self.participacao*0.1)
        return notaF
    
    def __str__(self):
        print(f'GrauB(Inicio:{self.data_comeco}, Fim:{self.data_fim})\n',
              f'Atividades:{self.atividades}, Seminário:{self.seminario}, Participacao:{self.participacao}')