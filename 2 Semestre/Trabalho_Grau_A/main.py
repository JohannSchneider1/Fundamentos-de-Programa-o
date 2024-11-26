from pousada import Pousada
from produtos import Produtos
from quarto import Quarto
from reserva import Reserva


def main():
    # Criação da Pousada
    pousada = Pousada("Pousada Bela Vista", "contato@pousada.com")
    
    # Criação dos produtos
    produtos_iniciais = [
        Produtos(0," ", 0.00),
        Produtos(1, "Cerveja", 10.00),
        Produtos(2, "Água", 5.00),
        Produtos(3, "Refrigerante", 7.00),
        Produtos(4, "Sanduíche", 15.00),
        Produtos(5, "Café", 3.00)
    ]
    
    # Adiciona os produtos à lista de produtos da pousada
    pousada.produtos.extend(produtos_iniciais)

    # Criação dos quartos
    quartos_iniciais = [
        Quarto(101, 'S', 300.00),
        Quarto(102, 'M', 400.00),
        Quarto(103, 'P', 500.00),
        Quarto(104, 'S', 300.00),
        Quarto(105, 'M', 400.00)
    ]
    
    # Adiciona os quartos à lista de quartos da pousada
    pousada.quartos.extend(quartos_iniciais)

    # Salva os dados iniciais em arquivos texto e carrega os existentes
    pousada.carrega_dados()
    pousada.salva_dados()


    while True:
        # Exibe o menu de opções
        print("\n--- Sistema de Gerenciamento da Pousada ---")
        print("1. Consultar disponibilidade")
        print("2. Consultar reserva")
        print("3. Realizar reserva")
        print("4. Cancelar reserva")
        print("5. Realizar check-in")
        print("6. Realizar check-out")
        print("7. Registrar consumo")
        print("8. Salvar dados")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        # Verifica qual opção foi escolhida e chama a função correspondente
        if opcao == '1':
            # Consultar disponibilidade
            data = int(input("Informe a data (AAAAMMDD): "))
            numero_quarto = int(input("Informe o número do quarto: "))
            pousada.consulta_disponibilidade(data, numero_quarto)

        elif opcao == '2':
            # Consultar reserva
            # Solicitar a data e verificar se o campo foi preenchido
            data_input = input("Informe a data (AAAAMMDD) ou deixe em branco: ")
            data = int(data_input) if data_input else None  # Converte para inteiro somente se houver entrada de informação

            # Solicitar as outras informações como nome
            cliente = input("Informe o nome do cliente ou deixe em branco: ")

            numero_quarto_input = input("Informe o número do quarto ou deixe em branco: ")
            numero_quarto = int(numero_quarto_input) if numero_quarto_input else None # Converter o número do quarto para inteiro, se fornecido

            pousada.consulta_reserva(data if data else None, cliente if cliente else None, numero_quarto if numero_quarto else None)

        elif opcao == '3':
            # Realizar reserva
            numero_quarto = None
            data_inicio = int(input("Informe a data de início (AAAAMMDD): "))
            data_fim = int(input("Informe a data de fim (AAAAMMDD): "))
            cliente = input("Informe o nome do cliente: ")
            numero_quarto = int(input("Informe o número do quarto: "))
            pousada.realiza_reserva(data_inicio, data_fim, cliente, numero_quarto)

        elif opcao == '4':
            # Cancelar reserva
            cliente = input("Informe o nome do cliente: ")
            pousada.cancela_reserva(cliente)

        elif opcao == '5':
            # Realizar check-in
            cliente = input("Informe o nome do cliente: ")
            pousada.realiza_checkin(cliente)

        elif opcao == '6':
            # Realizar check-out
            cliente = input("Informe o nome do cliente: ")
            pousada.realiza_checkout(cliente)

        elif opcao == '7':
            # Registrar consumo
            cliente = input("Informe o nome do cliente: ")
            pousada.registrar_consumo(cliente)

        elif opcao == '8':
            # Salvar dados
            pousada.salva_dados()
            print("Dados salvos com sucesso.")

        elif opcao == '0':
            # Sair do sistema
            print("Saindo do sistema... Salvando dados.")
            pousada.salva_dados()
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()