from classes import *

criar_tabela()
while True:
    print('''
          ======= Gerenciamento de Carros =======
          1. Cadastrar novo carro
          2. Remover carro
          3. Listar carros
          4. Pesquisar carro por placa
          5. Modificar informações de um carro
          6. Sair do programa
          ''')

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            ano = int(input("Digite o ano de fabricação do carro: "))
            cor = input("Digite a cor do carro: ")
            placa = input("Digite a placa do carro: ")

            carro = Carro(marca, modelo, ano, cor, placa)
            cadastrar_carro(carro)
            print("Carro cadastrado com sucesso!")

        case "2":
            id_carro = int(input("Digite o ID do carro a ser removido: "))
            remover_carro(id_carro)
            print("Carro removido com sucesso!")

        case "3":
            carros = listar_carros()
            if not carros:
                print("Nenhum carro cadastrado.")
            else:
                print("Lista de carros:")
                for carro in carros:
                    print(carro)

        case "4":
            placa = input("Digite a placa do carro a ser pesquisado: ")
            carro = pesquisar_carro(placa)
            if carro:
                print("Carro encontrado:", carro)
            else:
                print("Carro não encontrado.")
        
        case "5":
            id_carro = int(input("Digite o ID do carro a ser modificado: "))
            marca = input("Digite a nova marca do carro: ")
            modelo = input("Digite o novo modelo do carro: ")
            ano = int(input("Digite o novo ano de fabricação do carro: "))
            cor = input("Digite a nova cor do carro: ")
            placa = input("Digite a nova placa do carro: ")

            novo_carro = Carro(marca, modelo, ano, cor, placa)
            modificar_carro(id_carro, novo_carro)
            print("Informações do carro modificadas com sucesso!")

        case "6":
            print("Espero que tenha curtido o sistema! Até logo...")
            break

        case _:
            print("Opção inválida. Tente novamente.")
