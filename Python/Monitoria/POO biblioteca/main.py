# A classe Livro deve conter atributos como título, autor, ID, status de empréstimo (disponível ou emprestado).

class Livro:

    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status_emprestimo = 'disponível'

#A classe Membro deve conter atributos como nome,número de membro e histórico de livros emprestados.

class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimo = []

# A classe Biblioteca deve conter um catálogo de livros disponíveis, um registro de membros e métodos para empréstimo, devolução e pesquisa de livros.

class Biblioteca:

    proximo_id = 1

    def __init__(self):
        self.catalogo_livros = []
        self.registro_membros = []

    def adicionar_livro(self, titulo, autor):
        livro = Livro(Biblioteca.proximo_id, titulo, autor)
        Biblioteca.proximo_id += 1
        self.catalogo_livros.append(livro)
        return f'O livro "{livro.titulo}" foi adicionado ao catálogo.'
    
    def adicionar_membro(self, nome, numero_membro):
        membro = Membro(nome, numero_membro)
        self.registro_membros.append(membro)
        return f'O membro {membro.nome} foi adicionado!'
    
    def emprestar_livro(self, id_livro, numero_membro):
        livro_encontrado = None
        membro_encontrado = None

        # Procurando o livro pelo ID
        for livro_atual in self.catalogo_livros:
            if livro_atual.id == id_livro:
                livro_encontrado = livro_atual
                break

        # Verificando se o livro foi encontrado
        if not livro_encontrado:
            return f'O livro com ID {id_livro} não foi encontrado'

        # Procurando o membro pelo número de membro
        for membro_atual in self.registro_membros:
            if membro_atual.numero_membro == numero_membro:
                membro_encontrado = membro_atual
                break

        # Verificando se o membro foi encontrado
        if not membro_encontrado:
            return 'Membro não encontrado'

        # Verificando se o livro está disponível para empréstimo
        if livro_encontrado.status_emprestimo != 'disponível':
            return f'O livro "{livro_encontrado.titulo}" já está emprestado'

        # Realizando o empréstimo do livro
        livro_encontrado.status_emprestimo = 'emprestado'
        membro_encontrado.historico_emprestimo.append(livro_encontrado.id)

        return f'O livro "{livro_encontrado.titulo}" foi emprestado para {membro_encontrado.nome}.'

            
    def devolver_livro(self, id_livro, numero_membro):
        livro_encontrado = None
        membro_encontrado = None

        for livro_atual in self.catalogo_livros:
            if livro_atual.id == id_livro:
                livro_encontrado = livro_atual
                break

        for membro_atual in self.registro_membros:
            if membro_atual.numero_membro == numero_membro:
                membro_encontrado = membro_atual
                break

        if not livro_encontrado:
            return 'Livro não encontrado'

        if not membro_encontrado:
            return 'Membro não encontrado'

        if livro_encontrado.status_emprestimo != 'emprestado' or id_livro not in membro_encontrado.historico_emprestimo:
            return f'O livro "{livro_encontrado.titulo}" não está emprestado para {membro_encontrado.nome}.'

        livro_encontrado.status_emprestimo = 'disponível'
        membro_encontrado.historico_emprestimo.remove(id_livro)
        return f'O livro "{livro_encontrado.titulo}" foi devolvido por {membro_encontrado.nome}.'

    
    def pesquisar_livro(self, titulo):
        livros_encontrados = []
        for livro in self.catalogo_livros:
            if titulo.lower() in livro.titulo.lower():
                livros_encontrados.append(livro)
        return livros_encontrados if livros_encontrados else 'Nenhum livro encontrado :('
    
