from veiculo import Veiculo
from terrestre import Terrestre
from aereo import Aereo
from aquatico import Aquatico

def main ():
    carro = Terrestre(2023,300,35,'uno',4,4)
    aviao = Aereo (2022,1500,70,'gol',4,3)
    navio = Aquatico(2000,1050,100,'sim',2,2)

    
    carro.info()
    print(f'Quantidade de Consumo gasto é de: {carro.consumo()}')
    print(f'Autonomia: {carro.autonomia()}\n')

    aviao.info()
    print(f'Quantidade de Consumo gasto é de: {aviao.consumo()}')
    print(f'Autonomia: {aviao.autonomia()}\n')

    navio.info()
    print(f'Quantidade de Consumo gasto é de: {navio.consumo()}')
    print(f'Autonomia: {navio.autonomia()}')

if __name__ == '__main__':
    main()