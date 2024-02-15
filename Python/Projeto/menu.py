from classes import Biblioteca

biblioteca = Biblioteca()

while True:
    escolha = input('''Digite o número da opção desejada:
                    
                    1. Adicionar Livro ao catálogo
                    2. Adicionar Membro à biblioteca
                    3. Emprestar Livro
                    4. Devolver Livro
                    5. Pesquisar Livros
                    6. Sair''')
    opcoes: input('Digite o número da opção: ')
    
    match escolha:
        
        case '1':
            titulo = input('Digite o Título do Livro: ')
            autor = input('Digite o nome do Autor do Livro: ')
            biblioteca.adicionar_livro(titulo, autor)

        case '2':
            nome = input('Insira o nome do membro: ')
            biblioteca.adicionar_membro(nome)

        case '3':
            nomeLivro = input('Digite o nome do Livro: ')
            biblioteca.encontrar_livro_por_nome(nomeLivro)

        case '6':
            print('Saindo...')
            break
            
