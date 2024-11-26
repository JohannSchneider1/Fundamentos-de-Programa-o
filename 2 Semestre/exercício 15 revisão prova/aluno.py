from grau import Grau
from grauA import GrauA
from grauB import GrauB

class Aluno:
    def __init__(self,nome:str):
        self.__nome = nome
        self.__ga = GrauA ('01-01-2024','30-06-2024',0.0, 0.0)
        self.__gb = GrauB ('01-07-2024','31-12-2024',0.0, 0.0, 0.0)

    @property
    def nome (self):
        return self.__nome
    
    @property
    def ga (self):
        return self.__ga
    
    @property
    def gb (self):
        return self.__gb
    
    @nome.setter
    def nome (self,nome):
        self.__nome = nome
    
    @ga.setter
    def ga (self,ga):
        self.__ga = ga
    
    @gb.setter
    def gb (self,gb):
        self.__gb = gb

    def calcula_nota_final(self):
        nota_final_ga = self.ga.calcula_nota_final_grau()
        nota_final_gb = self.gb.calcula_nota_final_grau()
        nota_final = (nota_final_ga*0.33)+(nota_final_gb*0.67)
        return nota_final

    def __str__(self):
        print(f'Aluno:{self.nome}\n',
              f'GrauA:{self.ga.calcula_nota_final_grau():.2f}\n',
              f'GrauB:{self.gb.calcula_nota_final_grau():.2f}'
              f'Nota Final:{self.calcula_nota_final():.2f}')