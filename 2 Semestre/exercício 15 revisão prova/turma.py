from aluno import Aluno

class Turma:
    def __init__(self, codigo:str, capacidade:int):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__alunos = []

    @property
    def codigo (self):
        return self.__codigo
    
    @property
    def capacidade (self):
        return self.__capacidade
    
    @property
    def alunos (self):
        return self.__alunos

    @codigo.setter
    def codigo (self,codigo):
        self.__codigo = codigo

    @capacidade.setter
    def capacidade (self,capacidade):
        self.__capacidade = capacidade
    
    @alunos.setter
    def alunos (self, alunos):
        self.__alunos = alunos

    def insere_aluno (self, aluno:Aluno):
        if len(self.alunos) < self.capacidade:
            self.alunos.append(aluno)
            print(f'O aluno foi adicionado')
            return True
        else:
            print('O numero máximo de alunos na turma já foi atingido')
            return False
        
    def media_notas_turma (self):
        if not self.alunos:
            return -1
        else:
            media_turma = sum(aluno.calula_nota_final() for aluno in self.alunos) / len(self.alunos)
            return media_turma
    
    def altere_notas_ga (self, nome:str, trabalho:float, prova:float):
        for aluno in self.alunos:
            if aluno.nome == nome:
                aluno.ga.trabalho = trabalho
                aluno.ga.prova = prova

    def altere_notas_gb (self, nome:str, atividades:float, seminario:float, participacao:float):
        for aluno in self.alunos:
            if aluno.nome == nome:
                aluno.gb.atividades = atividades
                aluno.gb.seminario = seminario
                aluno.gb.participacao = participacao
                