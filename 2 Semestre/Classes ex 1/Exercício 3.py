class IRSimplificado:
    def __init__(self, nome, ano_nascimento, profissao, escolaridade, renda_mensal, dependentes):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.profissao = profissao
        self.escolaridade = escolaridade
        self.renda_mensal = renda_mensal
        self.dependentes = dependentes
    
    def idade_atual (self):
        idade = 2024 - self.ano_nascimento
        return idade
    
    def renda_anual (self):
        total = 12*self.renda_mensal
        return total
    
    def renda_per_capita_mensal (self):
        total = self.renda_mensal / self.dependentes
        return total
    
    def aliquota (self):
        if self.renda_mensal <= 2259.20:
            return 0
        elif self.renda_mensal>= 2259.21 and self.renda_mensal<= 2826.65:
            return 0.075
        elif self.renda_mensal>=2826.66 and self.renda_mensal<= 3751.05:
            return 0.15
        elif self.renda_mensal>=3751.06 and self.renda_mensal<= 4664.68:
            return 0.225
        elif self.renda_mensal> 4664.68:
            return 0.275
    
    def deducao_aliquota (self):
        if self.renda_mensal <= 2259.20:
            return 0
        elif self.renda_mensal>= 2259.21 and self.renda_mensal<= 2826.65:
            return 169.44
        elif self.renda_mensal>=2826.66 and self.renda_mensal<= 3751.05:
            return 381.44
        elif self.renda_mensal>=3751.06 and self.renda_mensal<= 4664.68:
            return 662.77
        elif self.renda_mensal> 4664.68:
            return 896.00
    
    def imposto_renda_mensal (self):
        resultado = self.renda_mensal * self.aliquota() - self.deducao_aliquota()
        return resultado
    
    def imposto_renda_anual(self):
        resultado = self.imposto_renda_mensal() * 12
        return resultado
    
def main():
    nome = input('Digite seu nome: ')
    nascimento = int(input('Digite o ano que nasceu: '))
    profissao = input('Digite sua profição: ')
    escolaridade = input('Digite sua escolaridade: ')
    renda = float(input('Digite sua renda mensal: '))
    dependentes = int(input('Digite quantos dependentes: '))

    p1 = IRSimplificado(nome,nascimento,profissao,escolaridade,renda,dependentes)

    print('nome: ',nome,'\nidade: ',p1.idade_atual(),'\nprofissâo: ',p1.profissao,'\nescolaridade: ',p1.escolaridade,'\ndependentes: ',p1.dependentes)
    print('renda mensal: ',p1.renda_mensal,'\nrenda anual: {:.2f}'.format(p1.renda_anual()))
    print('rena per capita mensal: {:.2f}'.format(p1.renda_per_capita_mensal()))
    print('imposto de renda mensa: {:.2f}'.format(p1.imposto_renda_mensal()))
    print('imposto de renda anual: {:.2f}'.format(p1.imposto_renda_anual()))


if __name__ == '__main__':
    main()