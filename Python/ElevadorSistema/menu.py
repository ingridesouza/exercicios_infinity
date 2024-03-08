from classes import Elevador

elevador = Elevador(10, 5)  # Capacidade máxima: 10 pessoas, total de andares: 5

while True:
    print("""
        ======================
         Seu elevador chegou!
          Escolha uma opção:
        ======================
        1. Entrar
        2. Subir
        3. Descer
        4. Sair
        5. Encessar sessão
        """)
    opcao = input("Escolha uma opção: ")

    match opcao:
        case '1':
            elevador.Entrar()
        case '2':
            elevador.Subir()
        case '3':
            elevador.Descer()
        case '4':
            elevador.Sair()
        case '5':
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.")
