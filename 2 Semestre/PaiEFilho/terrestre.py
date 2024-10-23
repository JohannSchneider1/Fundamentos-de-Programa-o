from veiculo import Veiculo

class Terrestre (Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str,qtRoda:int,qtPorta:int):
        super().__init__(ano, peso, tanque, modelo)
        self.__qtRoda = qtRoda
        self.__qtPorta = qtPorta
    
    @property
    def qtRoda (self):
        return self.__qtRoda
    
    @property
    def qtPorta (self):
        return self.__qtPorta
    
    @qtRoda.setter
    def qtRoda (self, qtRoda):
        self.__qtRoda = qtRoda
    
    @qtPorta.setter
    def qtPorta (self,qtPorta):
        self.__qtPorta = qtPorta
    
    def info(self):
        super().info()
        print(f'Quantidade de Rodas: {self.qtRoda}')
        print(f'Quantidade de Portas: {self.qtPorta}')
    
    def consumo (self):
        gastos = 1/((self.peso*0.00005)+(self.qtRoda*0.005))

        return gastos
    
    def autonomia (self):
        autonomia = self.consumo() * self.tanque
        return autonomia
    

