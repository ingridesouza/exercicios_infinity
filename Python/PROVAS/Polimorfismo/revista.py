from material import Material

class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Edição: {self.edicao}")
