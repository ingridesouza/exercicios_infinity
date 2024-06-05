from main import *

biblioteca = Biblioteca()

while True:
    escolha = input('''
               1. Adicionar Livro 
               2. Adicionar Membro
               3. Emprestar Livro
               4. Devolver Livro
               5. Pesquisar Livro 
               6. Exibir Todos os Livros
               7. Sair      
                ''')
    
    match escolha:
        case '1':
            titulo_livro = input('Digite o nome do livro: ')
            autor_livro = input('Digite o nome do autor: ')
            print(biblioteca.adicionar_livro(titulo_livro, autor_livro))


        case '2':
            nome = input("Digite o nome do membro: ")
            numero_membro = input("Digite o número do membro: ")
            print(biblioteca.adicionar_membro(nome, numero_membro))

        case '3':
            id_livro = input("Digite o ID do livro: ")
            numero_membro = input("Digite o número do membro: ")
            print(biblioteca.emprestar_livro(id_livro, numero_membro))

        case '4':
            id_livro = input("Digite o ID do livro: ")
            numero_membro = input("Digite o número do membro: ")
            print(biblioteca.devolver_livro(id_livro, numero_membro))
                

        case '5':
            titulo_livro = input('Digite o nome do livro: ')
            print(biblioteca.pesquisar_livro(titulo_livro))
        case '6':
            print('-- CATALOGO DE LIVROS--')
            print('TODOS:')
            print(biblioteca.catalogo_livros)

        case '7':
            print('Saindo do programa.. Até mais!')

        case _:
            print('Opção inválida, tente novamente')
            continue