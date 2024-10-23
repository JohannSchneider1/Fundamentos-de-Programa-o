from veiculo import Veiculo

class Aquatico (Veiculo):
    def __init__(self, ano: int, peso: int, tanque: float, modelo: str,qtMotor:int,qtConves:int):
        super().__init__(ano, peso, tanque, modelo)
        self.__qtMotor = qtMotor
        self.__qtConves = qtConves
    
    @property
    def qtMotor (self):
        return self.__qtMotor
    
    @property
    def qtConves (self):
        return self.__qtConves
    
    @qtMotor.setter
    def qtMotor (self,qtMotor):
        self.__qtMotor = qtMotor
    
    @qtConves.setter
    def qtConves (self,qtConves):
        self.__qtConves = qtConves

    def info(self):
        super().info()
        print(f'Quantidade de Motores: {self.qtMotor}')
        print(f'Quantidade de Conves: {self.qtConves}')
    
    def consumo (self):
        gastos = 1/((self.peso*0.00002)+(self.qtMotor*0.02))
        return gastos
    
    def autonomia (self):
        autonomia = self.consumo() * self.tanque
        return autonomia