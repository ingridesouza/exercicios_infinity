class Livro:
    def __init__(self, titulo, autor, id, status_emprestimo = False):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status_emprestimo = status_emprestimo


    def __str__(self):
        return f"{self.titulo} (ID: {self.id}) - Autor: {self.autor}, Empréstimo: {'Disponível' if not self.status_emprestimo else 'Indisponível'}"

class Membro:
    def __init__(self, nome, id_membro, livros_emprestados = None):
        self.nome = nome
        self.id_membro = id_membro
        self.livros_emprestados = livros_emprestados if livros_emprestados else []


    def __str__(self):
        # O método __str__ é um método 'especial' do python para controlar como um objeto é convertido em uma string.

        return f"{self.nome} (ID: {self.id_membro}) - Livros emprestados: {len(self.livros_emprestados)}"

class Biblioteca:
    def __init__(self, registro_membros=None):
        self.catalogo = []
        self.registro_membros = registro_membros if registro_membros else []
        self.registro_membros = registro_membros if registro_membros else []

        #  Se registro_membros for fornecido ao criar uma instância da classe (Biblioteca), ele será utilizado. Caso contrário, será criada uma lista vazia ([]) e atribuída a registro_membros. Isso garante que o atributo registro_membros sempre seja uma lista, mesmo que inicialmente não seja fornecido nenhum valor ou seja fornecido um valor nulo.

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor, len(self.catalogo) + 1)
        self.catalogo.append(livro)
        return f'O livro "{livro.titulo}" foi adicionado ao catálogo.'


    def adicionar_membro(self, nome):
        membro = Membro(nome, len(self.registro_membros) + 1)
        self.registro_membros.append(membro)
        return f'O membro "{membro.nome}" foi adicionado à biblioteca.'


    def emprestar_livro(self, id_livro, id_membro):
        livro = self.encontrar_livro_por_id(id_livro)
        membro = self.encontrar_membro_por_id(id_membro)

        if livro and membro:
            # verifica se tanto o objeto livro quanto o objeto membro existem (não são None ou outros valores considerados como False em Python), garantindo que ambos os objetos necessários para realizar o empréstimo estejam presentes.
            if not livro.status_emprestimo:
                # verifica se o livro não está atualmente emprestado, usando a condição not 
                livro.status_emprestimo = True
                membro.livros_emprestados.append(livro)
                print(f'O livro "{livro.titulo}" foi emprestado para o membro "{membro.nome}".')
            else:
                print(f'O livro "{livro.titulo}" já está emprestado.')
        else:
            print('Livro ou membro não encontrado.')


    def registrar_devolucao(self, id_livro, id_membro):
        livro = self.encontrar_livro_por_id(id_livro)
        membro = self.encontrar_membro_por_id(id_membro)

        if livro and membro:
            if livro.status_emprestimo and livro in membro.livros_emprestados:
                livro.status_emprestimo = False
                membro.livros_emprestados.remove(livro)
                print(f'O livro "{livro.titulo}" foi devolvido pelo membro "{membro.nome}".')
            else:
                print(f'O livro "{livro.titulo}" não está atualmente emprestado para o membro "{membro.nome}".')
        else:
            print('Livro ou membro não encontrado.')


    def pesquisar_livros(self, termo):
        resultados = [livro for livro in self.catalogo if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower() or str(livro.id) == termo]
        
        if resultados:
            print("Resultados da pesquisa:")
            for livro in resultados:
                print(livro)
        else:
            print(f"Nenhum livro encontrado para o termo: '{termo}'.")

#----------------------------------------------------------------------

    # def encontrar_livro_por_id(self, id_livro):
    #     for livro in self.catalogo:
    #         if livro.id == id_livro:
    #             return livro
    #     return None
            
    def encontrar_livro_por_nome(self, nome_livro):
        for livro in self.catalogo:
            if livro.nome == nome_livro:
                return livro
        return None
    
#----------------------------------------------------------------------

    def encontrar_membro_por_id(self, id_membro):
        for membro in self.registro_membros:
            if membro.id_membro == id_membro:
                return membro
        return None

#----------------------------------------------------------------------

    def __str__(self):
        catalogo_str = "\n".join([str(livro) for livro in self.catalogo])
        membros_str = "\n".join([str(membro) for membro in self.registro_membros])
        return f"Catálogo:\n{catalogo_str}\nMembros:\n{membros_str}"

#----------------------------------------------------------------------

    def visualizar_catalogo(self):
        print("\nCatálogo da Biblioteca:")
        for livro in self.catalogo:
            print(livro)

