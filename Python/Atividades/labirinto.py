# Desenvolvimento de Jogo de Labirinto

# Você foi desafiado a criar um jogo de labirinto utilizando Python. O jogo será representado por uma grade retangular, onde alguns espaços são caminhos livres ('0'), e outros são paredes ('1'). O jogador será representado por um ponto de partida ('x'), e o objetivo é encontrar a saída ('9').

# Regras do jogo:

# O jogador só pode se mover para cima, para baixo, para a esquerda ou para a direita, nunca na diagonal.
# Não é permitido dar a volta no labirinto (não é possível passar da extremidade esquerda para a direita e vice-versa).
# Se um movimento para uma parede ou para fora dos limites do labirinto for realizado, ele será considerado inválido.
# Tarefa:

# Desenvolva um código em Python que permita ao jogador interagir com o labirinto. Ao começar, o jogador estará na posição 'x'. O jogo deve solicitar ao jogador a próxima jogada (W para cima, S para baixo, A para esquerda, D para direita) e mostrar o labirinto atualizado após cada jogada. O jogo deve terminar quando o jogador encontrar a saída ('9').

# Esta questão desafia os alunos a criarem um jogo de labirinto com regras específicas e a desenvolverem um código em Python para implementar essa lógica. Isso testará suas habilidades de programação e lógica, além de envolver conceitos de manipulação de matrizes e estruturas condicionais.

labirinto = [
            [0, 1, 0, 1, 0], 
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 0, 1]
]
    
caminhoBoneco = 0
parede = 1

while True:
    escolhaMovimentos = input('''
        Escolha uma opção: 
        W- Movimente-se para cima
        S- Movimente-se para baixo
        A- Movimente-se para a esquerda
        D- Movimente-se para a direita
    ''')

    # match escolhaMovimentos:
        # case 'S':
            

#   digite a sua proxima jogada :       