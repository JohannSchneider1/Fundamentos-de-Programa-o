import os
from Processo import Processo
from ComputingProcess import ComputingProcess


class ReadingProcess(Processo):
    def __init__(self, pid, fila_processos):
        super().__init__(pid)
        self.fila_processos = fila_processos
    
    def execute(self):
        if os.path.exists("computation.txt"):
            with open("computation.txt", "r") as file:
                for linha in file:
                    expressao = linha.strip()
                    novo_pid = max([p.pid for p in self.fila_processos.processos], default=0) + 1
                    self.fila_processos.adicionar_processo(ComputingProcess(novo_pid, expressao))
            open("computation.txt", "w").close()
            print("Processos de cálculo adicionados à fila e arquivo computation.txt limpo.")