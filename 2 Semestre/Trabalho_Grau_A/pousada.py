from __future__ import annotations
from produtos import Produtos
from quarto import Quarto
from reserva import Reserva
import os

class Pousada :
    def __init__(self,nome,contato):
        self.__nome = nome
        self.__contato = contato
        self.quartos = []
        self.reservas = []
        self.produtos = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def contato (self):
        return self.__contato
    
    @contato.setter
    def contato(self,contato):
        self.__contato = contato

    def carrega_dados (self):
        #carrega produtos
        #abrindo e lendo o arquivo
        prod = open('produto.txt','r')
        leitura = prod.read().strip().split('\t')
        prod.close()
        if len(leitura) == 3:
            # convertendo de str para inteiro e float dos produtos
            codigo = int(leitura[0])
            nome = leitura[1]
            preco = float(leitura[2])
            self.produtos.append(Produtos(codigo,nome,preco))
        
        #carrega quartos é praticamente mesma coisa que os produtos
        quar = open('quarto.txt','r')
        leitura = quar.read().strip().split('\t')
        quar.close()
        if len(leitura) == 3:
            numero = int(leitura[0])
            categoria = leitura[1]
            diaria = float(leitura[2])
            self.quartos.append(Quarto(numero,categoria,diaria))
        
        #carrega reservas mesma coisa que os dois anteriores só que com 5 itens agora
        reser = open('reserva.txt','r')
        leitura = reser.read().strip().split('\t')
        reser.close()
        if len(leitura) == 5:
            dia_inicio = int(leitura[0])
            dia_fim = int(leitura[1])
            cliente = leitura[2]
            quarto_numero = int(leitura[3])
            status = leitura [4]
            quarto = next((i for i in self.quartos if i.numero == quarto_numero),None)
            if quarto:
                self.reservas.append(Reserva(dia_inicio,dia_fim,cliente,quarto,status))
        #Obs.: O print vai mudar depois desse pois descobri uma forma mais simples de fazer.
        print('Dados carregados:\n', len(self.produtos), 'produtos\n', len(self.quartos), 'quartos\n', len(self.reservas), 'reservas.')
    
    def salva_dados(self):
        # Salva produtos abrindo o arquivo percorrendo a lista produtos os produtos que foram salvos e escrevendo no arquivo com a tabulação de (TAB)
        with open('produto.txt', 'w') as file:
            for produto in self.produtos:
                file.write(f"{produto.codigo}\t{produto.nome}\t{produto.preco:.2f}\n")

        # Salva quartos mesma coisa que os produtos mas agora percorrendo os quartos e salvando com a mesma tabulação
        with open('quarto.txt', 'w') as file:
            for quarto in self.quartos:
                file.write(f"{quarto.numero}\t{quarto.categoria}\t{quarto.diaria:.2f}\n")

        # Salva reservas (exclui as canceladas e com checkout realizado) como a pessoa realizou checkout não tem mais o porque dela esta sendo salva em um arquivo.
        with open('reserva.txt', 'w') as file:
            for reserva in self.reservas:
                if reserva.status not in ['C', 'O']:  # Não salva canceladas ou com check-out.
                    file.write(f"{reserva.dia_inicio}\t{reserva.dia_fim}\t{reserva.cliente}\t{reserva.quarto.numero}\t{reserva.status}\n")

        print("Dados salvos com sucesso.")
    
    def consulta_disponibilidade(self, data, quarto_numero):
        # Verifica se o quarto existe e ao percorrer na lista retorna a primeira instancia verdadeira.
        quarto = next((q for q in self.quartos if q.numero == quarto_numero), None)
        #se não retornar nada exibira a mensagem e retornará falso
        if not quarto:
            print(f"Quarto {quarto_numero} não encontrado.")
            return False

        # Verifica se o quarto ja está reservado para a data informada
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto_numero and reserva.status == 'A':
                if reserva.dia_inicio <= data <= reserva.dia_fim:
                    print(f"O quarto {quarto_numero} está reservado para a data {data}.")
                    return False  # O quarto está reservado nessa data

        # Se passou por todas as reservas e não encontrou conflito, o quarto está disponível
        print(f"O quarto {quarto_numero} está disponível para a data {data}.")
        return True
    
    def consulta_reserva(self, data=None, cliente=None, quarto_numero=None):

        # Filtra as reservas ativas (status == 'A')
        reservas_ativas = [reserva for reserva in self.reservas if reserva.status == 'A']
        resultados = []

        for reserva in reservas_ativas:
            # Verifica se a reserva corresponde aos critérios informados (data, cliente, quarto)
            corresponde_data = data is None or (data >= reserva.dia_inicio and data <= reserva.dia_fim)
            corresponde_cliente = cliente is None or reserva.cliente.lower() == cliente.lower()
            corresponde_quarto = quarto_numero is None or reserva.quarto.numero == quarto_numero

            if corresponde_data and corresponde_cliente and corresponde_quarto:
                resultados.append(reserva)

        # Exibe os resultados encontrados
        if resultados:
            print("Reservas encontradas:")
            for reserva in resultados:
                print(f"Cliente: {reserva.cliente}, Quarto: {reserva.quarto.numero}, "
                      f"Data início: {reserva.dia_inicio}, Data fim: {reserva.dia_fim}")
        else:
            print("Nenhuma reserva encontrada com os parâmetros informados.") 
    
    def realiza_reserva(self, data_inicio, data_fim, cliente, quarto_numero):
        # Verifica se o quarto existe
        quarto = next((q for q in self.quartos if q.numero == quarto_numero), None)
        if not quarto:
            print(f"Quarto {quarto_numero} não encontrado.")
            return False

        # Verifica se o cliente já tem uma reserva ativa ou em check-in
        for reserva in self.reservas:
            if reserva.cliente.lower() == cliente.lower() and reserva.status in ['A', 'I']:
                print(f"O cliente {cliente} já possui uma reserva ativa ou em check-in.")
                return False

        # Verifica a disponibilidade do quarto no período solicitado
        for reserva in self.reservas:
            if reserva.quarto.numero == quarto_numero and reserva.status == 'A':
                # Se as datas se sobrepõem
                if (data_inicio <= reserva.dia_fim and data_fim >= reserva.dia_inicio):
                    print(f"O quarto {quarto_numero} está reservado nesse período.")
                    return False

        # Cria a nova reserva e adiciona à lista de reservas
        nova_reserva = Reserva(data_inicio, data_fim, cliente, quarto, 'A')
        self.reservas.append(nova_reserva)

        print(f"Reserva realizada com sucesso para o cliente {cliente} no quarto {quarto_numero} "
              f"de {data_inicio} até {data_fim}.")
        return True
    
    def cancela_reserva(self, cliente):
        # Verifica se o cliente possui uma reserva ativa
        for reserva in self.reservas:
            if reserva.cliente.lower() == cliente.lower() and reserva.status == 'A':
                # Cancela a reserva, alterando o status para 'C'
                reserva.status = 'C'
                print(f"Reserva do cliente {cliente} foi cancelada com sucesso.")
                return True

        # Caso não haja reserva ativa para o cliente
        print(f"Não existe reserva ativa para o cliente {cliente}.")
        return False
    
    def realiza_checkin(self, cliente):
        # Verifica se o cliente possui uma reserva ativa
        for reserva in self.reservas:
            if reserva.cliente.lower() == cliente.lower() and reserva.status == 'A':
                # Calcula a quantidade de dias da reserva
                dias_reservados = reserva.dia_fim - reserva.dia_inicio + 1
                valor_total_diarias = dias_reservados * reserva.quarto.diaria

                # Altera o status da reserva para Check-In ('I')
                reserva.status = 'I'

                # Exibe os dados do check-in
                print(f"Check-in realizado para o cliente {cliente}.")
                print(f"Data de início: {reserva.dia_inicio}")
                print(f"Data de fim: {reserva.dia_fim}")
                print(f"Quantidade de dias: {dias_reservados}")
                print(f"Valor total das diárias: R$ {valor_total_diarias:.2f}")
                print(f"Dados do quarto: Número {reserva.quarto.numero}, Categoria {reserva.quarto.categoria}, Diária R$ {reserva.quarto.diaria:.2f}")
                
                return True

        # Caso o cliente não possua uma reserva ativa
        print(f"Não existe reserva ativa para o cliente {cliente}.")
        return False
    
    def realiza_checkout(self, cliente):
        # Verifica se o cliente possui uma reserva com check-in
        for reserva in self.reservas:
            if reserva.cliente.lower() == cliente.lower() and reserva.status == 'I':
                # Calcula a quantidade de dias da reserva
                dias_reservados = reserva.dia_fim - reserva.dia_inicio + 1
                valor_total_diarias = dias_reservados * reserva.quarto.diaria

                # Calcula o valor total do consumo
                valor_total_consumo = sum(self.produtos[produto_id].preco for produto_id in reserva.quarto.consumo)
                
                # Valor final a ser pago (diárias + consumo)
                valor_final = valor_total_diarias + valor_total_consumo

                # Exibe os dados do check-out
                print(f"Check-out realizado para o cliente {cliente}.")
                print(f"Data de início: {reserva.dia_inicio}")
                print(f"Data de fim: {reserva.dia_fim}")
                print(f"Quantidade de dias: {dias_reservados}")
                print(f"Valor total das diárias: R$ {valor_total_diarias:.2f}")
                print("Consumo:")
                for produto_id in reserva.quarto.consumo:
                    produto = self.produtos[produto_id]
                    print(f" - {produto.nome}: R$ {produto.preco:.2f}")
                print(f"Valor total do consumo: R$ {valor_total_consumo:.2f}")
                print(f"Valor final a ser pago (diárias + consumo): R$ {valor_final:.2f}")

                # Alterar o status da reserva para Check-Out ('O')
                reserva.status = 'O'

                # Limpar o consumo do quarto
                reserva.quarto.limpa_consumo()

                return True

        # Caso o cliente não possua uma reserva com check-in
        print(f"Não existe reserva com check-in para o cliente {cliente}.")
        return False
    
    
    def registrar_consumo(self, nome_cliente):
        # Procura a reserva do cliente que está em check-in
        reserva = None
        for r in self.reservas:
            if r.cliente == nome_cliente and r.status == 'I':  # 'I' = Check-in
                reserva = r
                break

        if reserva:
            # Mostra os produtos disponíveis
            print("\n--- Produtos Disponíveis ---")
            for produto in self.produtos:
                print(f"Código: {produto.codigo}, Produto: {produto.nome}, Valor: R${produto.preco:.2f}")

            # Solicita o código do produto consumido
            codigo_produto = int(input("Informe o código do produto consumido: "))

            # Procura o produto com o código informado
            produto_consumido = None
            for produto in self.produtos:
                if produto.codigo == codigo_produto:
                    produto_consumido = produto
                    break

            if produto_consumido:
                # Adiciona o produto à lista de consumo do quarto
                reserva.quarto.consumo.append(produto_consumido.codigo)
                print(f"Produto '{produto_consumido.nome}' adicionado ao consumo do cliente {nome_cliente}.")
            else:
                print("Código de produto inválido.")
        else:
            print(f"Não há reserva em check-in para o cliente {nome_cliente}.")