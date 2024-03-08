from classes import Biblioteca

biblioteca = Biblioteca()

while True:
    escolha = input('''Digite o número da opção desejada:
                    
                    1. Adicionar Livro ao catálogo
                    2. Adicionar Membro à biblioteca
                    3. Emprestar Livro
                    4. Devolver Livro
                    5. Pesquisar Livros
                    6. Visualizar catálogo
                    0. Sair
                    
                    Escolha uma opção: ''')
    
    match escolha:
        
        case "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            biblioteca.adicionar_livro(titulo, autor)
        case "2":
            nome = input("Digite o nome do membro: ")
            biblioteca.adicionar_membro(nome)
        case "3":
            id_livro = int(input("Digite o ID do livro: "))
            id_membro = int(input("Digite o ID do membro: "))
            biblioteca.emprestar_livro(id_livro, id_membro)
        case "4":
            id_livro = int(input("Digite o ID do livro: "))
            id_membro = int(input("Digite o ID do membro: "))
            biblioteca.registrar_devolucao(id_livro, id_membro)
        case "5":
            termo = input("Digite o termo de pesquisa: ")
            biblioteca.pesquisar_livros(termo)
        case "6":
            biblioteca.visualizar_catalogo()
        case "0":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida! Por favor, escolha uma opção válida.")
            
