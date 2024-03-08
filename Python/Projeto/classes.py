class Livro:
    def __init__(self, titulo, autor, id, status_emprestimo=False):
        """
        Inicializa um objeto Livro.

        Args:
            titulo (str): O título do livro.
            autor (str): O autor do livro.
            id (int): O identificador único do livro.
            status_emprestimo (bool, opcional): O status de empréstimo do livro. Padrão é False.
        """
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status_emprestimo = status_emprestimo

    def __str__(self):
        """
        Retorna uma representação em string do objeto Livro.

        Returns:
            str: A representação em string do livro.
        """
        status = 'Disponível' if not self.status_emprestimo else 'Indisponível'
        return f"{self.titulo} (ID: {self.id}) - Autor: {self.autor}, Empréstimo: {status}"


class Membro:
    def __init__(self, nome, id):
        """
        Inicializa um objeto Membro.

        Args:
            nome (str): O nome do membro.
            id (int): O identificador único do membro.
        """
        self.nome = nome
        self.id = id
        self.livros_emprestados = []

    def __str__(self):
        """
        Retorna uma representação em string do objeto Membro.

        Returns:
            str: A representação em string do membro.
        """
        return f"{self.nome} (ID: {self.id}) - Livros emprestados: {len(self.livros_emprestados)}"


class Biblioteca:
    def __init__(self):
        """Inicializa um objeto Biblioteca."""
        self.catalogo = []
        self.registro_membros = []

    def adicionar_livro(self, titulo, autor):
        """
        Adiciona um novo livro ao catálogo da biblioteca.

        Args:
            titulo (str): O título do livro.
            autor (str): O autor do livro.

        Returns:
            str: Mensagem informando que o livro foi adicionado ao catálogo.
        """
        livro = Livro(titulo, autor, len(self.catalogo) + 1)
        self.catalogo.append(livro)
        return f'O livro "{livro.titulo}" foi adicionado ao catálogo.'

    def adicionar_membro(self, nome):
        """
        Adiciona um novo membro à biblioteca.

        Args:
            nome (str): O nome do membro.

        Returns:
            str: Mensagem informando que o membro foi adicionado à biblioteca.
        """
        membro = Membro(nome, len(self.registro_membros) + 1)
        self.registro_membros.append(membro)
        return f'O membro "{membro.nome}" foi adicionado à biblioteca.'

    def emprestar_livro(self, id_livro, id_membro):
        """
        Empresta um livro para um membro da biblioteca.

        Args:
            id_livro (int): O ID do livro a ser emprestado.
            id_membro (int): O ID do membro que solicita o empréstimo.

        Returns:
            str: Mensagem informando o resultado da operação de empréstimo.
        """
        livro = self.encontrar_livro_por_id(id_livro)
        membro = self.encontrar_membro_por_id(id_membro)

        if livro and membro:
            if not livro.status_emprestimo:
                livro.status_emprestimo = True
                membro.livros_emprestados.append(livro)
                return f'O livro "{livro.titulo}" foi emprestado para o membro "{membro.nome}".'
            else:
                return f'O livro "{livro.titulo}" já está emprestado.'
        else:
            return 'Livro ou membro não encontrado.'

    def registrar_devolucao(self, id_livro, id_membro):
        """
        Registra a devolução de um livro pela biblioteca.

        Args:
            id_livro (int): O ID do livro devolvido.
            id_membro (int): O ID do membro que devolveu o livro.

        Returns:
            str: Mensagem informando o resultado da operação de devolução.
        """
        livro = self.encontrar_livro_por_id(id_livro)
        membro = self.encontrar_membro_por_id(id_membro)

        if livro and membro:
            if livro.status_emprestimo and livro in membro.livros_emprestados:
                livro.status_emprestimo = False
                membro.livros_emprestados.remove(livro)
                return f'O livro "{livro.titulo}" foi devolvido pelo membro "{membro.nome}".'
            else:
                return f'O livro "{livro.titulo}" não está atualmente emprestado para o membro "{membro.nome}".'
        else:
            return 'Livro ou membro não encontrado.'

    def pesquisar_livros(self, termo):
        """
        Pesquisa livros no catálogo da biblioteca.

        Args:
            termo (str): O termo a ser pesquisado.

        Returns:
            str: Mensagem com os resultados da pesquisa.
        """
        resultados = [livro for livro in self.catalogo if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower() or str(livro.id) == termo]
        
        if resultados:
            mensagem = "Resultados da pesquisa:\n"
            for livro in resultados:
                mensagem += str(livro) + "\n"
            return mensagem
        else:
            return f"Nenhum livro encontrado para o termo: '{termo}'."

    def encontrar_livro_por_id(self, id_livro):
        """
        Encontra um livro no catálogo da biblioteca pelo ID.

        Args:
            id_livro (int): O ID do livro a ser encontrado.

        Returns:
            Livro or None: O livro encontrado ou None se não encontrado.
        """
        for livro in self.catalogo:
            if livro.id == id_livro:
                return livro
        return None
    
    def encontrar_membro_por_id(self, id_membro):
        """
        Encontra um membro na lista de membros da biblioteca pelo ID.

        Args:
            id_membro (int): O ID do membro a ser encontrado.

        Returns:
            Membro or None: O membro encontrado ou None se não encontrado.
        """
        for membro in self.registro_membros:
            if membro.id == id_membro:
                return membro
        return None

    def visualizar_catalogo(self):
        """Visualiza o catálogo da biblioteca."""
        print("\nCatálogo da Biblioteca:")
        for livro in self.catalogo:
            print(livro)
