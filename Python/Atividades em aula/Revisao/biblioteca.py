# Livro: Representa um livro na biblioteca e contém atributos como título, autor, ano de publicação, etc.
class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
    

# Biblioteca: Representa a biblioteca em si e contém métodos para adicionar livros, pesquisar livros, emprestar livros, devolver livros e visualizar a lista de livros disponíveis.
class Biblioteca:
    def __init__(self):
        self.livros = []

    
    def adicionarLivro(self, titulo, autor, ano):
        livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)

    def pesquisarLivro(self, livro):
        for livro in self.livros:
            if livro == termo:
                print(livro)

    def visualizar_livros(self):
        for livro in self.livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}")
        

biblioteca = Biblioteca()

while True:

    opcao = input("Escolha uma opção: 1. Adicionar Livro, 2. Pesquisar Livro, 3. Emprestar Livro, 4. Devolver Livro, 5. Visualizar Lista de Livros, 6. Sair")

    match opcao:
    
        case '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor do livro: ")
            ano = input("Digite o ano de publicação do livro: ")
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro(livro)
        case '2':
            termo = input("Digite o título do livro para a pesquisa: ")
            biblioteca.pesquisar_livro(termo)
        case '3':
            titulo = input("Digite o título do livro que deseja emprestar: ")
            for livro in biblioteca.livros:
                if livro.titulo == titulo:
                    biblioteca.emprestar_livro(livro)
                    print(f"O livro '{titulo}' foi emprestado com sucesso!")
                    break
            else:
                print(f"O livro '{titulo}' não está disponível para empréstimo.")
        case '4':
            titulo = input("Digite o título do livro que deseja devolver: ")
            # Verificar se o livro foi emprestado e devolver se foi
            for livro in biblioteca.livros:
                if livro.titulo == titulo and livro.emprestado:
                    biblioteca.devolver_livro(livro)
                    print(f"O livro '{titulo}' foi devolvido com sucesso!")
                    break
            else:
                print(f"O livro '{titulo}' não foi emprestado ou não está na biblioteca.")
        case '5':
            biblioteca.visualizar_livros()
        case _:
            print("Opção inválida!")