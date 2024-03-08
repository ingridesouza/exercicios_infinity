from livro import Livro
from revista import Revista

while True:
    print("""
    =================== BEM VINDO ===================================
    1. Exibir informações do livro "As Crônicas de Gelo e Fogo"
    2. Exibir informações do livro "A Menina que Roubava Livros"
    3. Exibir informações do livro "A Sutil Arte de Ligar o F*da-se"
    4. Exibir informações da revista "Superinteressante"
    5. Exibir informações da revista "Harvard Business Review"
    6. Exibir informações da revista "Rolling Stone"
    7. Sair
    =================================================================
    """)
    opcao = input("Escolha uma opção: ")

    match opcao:
        case '1':
            livro1 = Livro("As Crônicas de Gelo e Fogo", "George R. R. Martin", "Fantasia")
            livro1.exibir_informacoes()
        case '2':
            livro2 = Livro("A Menina que Roubava Livros", "Markus Zusak", "Drama")
            livro2.exibir_informacoes()
        case '3':
            livro3 = Livro("A Sutil Arte de Ligar o F*da-se", "Mark Manson", "Autoajuda")
            livro3.exibir_informacoes()
        case '4':
            revista1 = Revista("Superinteressante", "Editora Abril", "Edição de Maio de 2022")
            revista1.exibir_informacoes()
        case '5':
            revista2 = Revista("Harvard Business Review", "Harvard University", "Edição de Abril de 2022")
            revista2.exibir_informacoes()
        case '6':
            revista3 = Revista("Rolling Stone", "Wenner Media LLC", "Edição de Março de 2022")
            revista3.exibir_informacoes()
        case '7':
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.")
