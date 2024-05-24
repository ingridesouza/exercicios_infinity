class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Alice", 30)

# Chamando um método do objeto
pessoa1.saudacao()  # Output: Olá, meu nome é Alice e tenho 30 anos.


# Neste exemplo, Pessoa é uma classe que possui dois atributos (nome e idade) e um método (saudacao()). Criamos um objeto chamado pessoa1 a partir desta classe e chamamos o método saudacao() do objeto.