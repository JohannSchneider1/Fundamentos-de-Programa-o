from veiculo import Veiculo

class Aereo(Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str,qtAsa:int,qtMotor:int):
        super().__init__(ano, peso, tanque, modelo)
        self.__qtAsa = qtAsa
        self.__qtMotor = qtMotor
    
    @property
    def qtAsa (self):
        return self.__qtAsa
    
    @property
    def qtMotor (self):
        return self.__qtMotor
    
    @qtAsa.setter
    def qtAsa (self,qtAsa):
        self.__qtAsa = qtAsa
    
    @qtMotor.setter
    def qtMotor (self,qtMotor):
        self.__qtMotor = qtMotor
    
    def info(self):
        super().info()
        print(f'Quantidade de Asas: {self.qtAsa}')
        print(f'Quantidade de Motores: {self.qtMotor}')
    
    def consumo (self):
        gastos = 1/((self.peso*0.00003)+(self.qtMotor*0.01))
        return gastos

    def autonomia (self):
        autonomia = self.consumo() * self.tanque
        return autonomia
    