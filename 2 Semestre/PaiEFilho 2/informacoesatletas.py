from nadador import Nadador
from corredor import Corredor

class InformacoesAtletas ():

    def imprime_exclusivo_atleta (self):
        
        if isinstance(self,Nadador):
            print(f'É um nadador e sua categoria é: {self.categoria}')
        
        if isinstance(self,Corredor):
            print(f'É um corredor e seu peso é: {self.peso}')
    
    def imprime_informacoes_atleta(self):
        self.imprime_info()
    
    
