from classes import BombaCombustivel

bomba = BombaCombustivel("Gasolina", 5.0, 1000)

while True:
    escolha = input("""
    ===== BOMBA DE COMBUSTIVEL =====
                    
    1. Abastecer por valor
    2. Abastecer por litro
    3. Alterar valor do litro
    4. Alterar tipo de combustível
    5. Alterar quantidade de combustível na bomba
    6. Sair
    Escolha uma opção: 
                    """)

    match escolha:
        case '1':
            valor = float(input("Informe o valor a ser abastecido: "))
            print(bomba.abastecer_por_valor(valor))
        case '2':
            litros = float(input("Informe a quantidade em litros de combustível: "))
            print(bomba.abastecer_por_litro(litros))
        case '3':
            novo_valor = float(input("Informe o novo valor do litro: "))
            print(bomba.alterar_valor(novo_valor))
        case '4':
            novo_tipo_combustivel = input("Informe o novo tipo de combustível: ")
            print(bomba.alterar_combustivel(novo_tipo_combustivel))
        case '5':
            nova_quantidade = float(input("Informe a nova quantidade de combustível na bomba: "))
            print(bomba.alterar_quantidade_combustivel(nova_quantidade))
        case '6':
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.")
