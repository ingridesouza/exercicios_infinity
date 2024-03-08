from material import Material

class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Gênero: {self.genero}")
