from aluno import Aluno
from grau import Grau
from grauA import GrauA
from grauB import GrauB
from turma import Turma
import random

class main():
    codigo = int('Digite um código para a turma: ')
    capacidade = int('Digite a capacidade de alunos na turma(máximo: 30): ')
    capacidade = min(capacidade, 30)

    turma = Turma (codigo,capacidade)

    numero_alunos = random.randint(1,100)
    for i in range (1, numero_alunos +1):
        aluno = Aluno(f'Aluno{i}')
        sucesso = turma.insere_aluno(aluno)
        print(f'Tentativa de inserir {aluno.nome}: {'Sucesso' if sucesso else 'Falha'}')
        if not sucesso:
            break
    
        turma.altere_notas_ga(aluno.nome, random.uniform(0,100), random.uniform(0,100))
        turma.altere_notas_ga(aluno.nome, random.uniform(0,100), random.uniform(0,100), random.uniform(0,100))

    

