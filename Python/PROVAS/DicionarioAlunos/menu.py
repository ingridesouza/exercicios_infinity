# [PY-A07] Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos. Para isso, você deve implementar um módulo que contém as seguintes funções: 

#AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos. 

#RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos. 

#AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário . 

#VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.

from funcoes import *
from bancoDados import *

while True:

        print(''' 
                1- Adicionar Aluno.
                2- Remover Aluno.
                3- Aualizar Aluno.
                4- Ver Alunos.
                5- Sair.
                ''')
    
        escolha = input('Digite o número da opção desejada: -->')

        match escolha:
            case '1':
                nome_aluno = input('Digite o nome do aluno que deseja adicionar: ')
                numero_matricula = input('Digite o número da matricula do mesmo: ')
                linha()
                adicionar_aluno(alunos,nome_aluno, numero_matricula)
                linha()

            case '2':
                matricula_usuario_remover = int(input('Digite o número da matrícula do aluno que deseja remover: '))
                linha()
                removerAluno(alunos, matricula_usuario_remover)
                linha()

            case '3':
                numero_matricula = input('Digite o número da matricula do aluno que deseja atualizar: ')
                nome_aluno_atualizar = input('Insira o nome atualizado do aluno: ')
                linha()
                atualizarAluno(alunos, numero_matricula, nome_aluno_atualizar)
                linha()

            case '4':
                linha()
                verAlunos(alunos)
                linha()
            case _:
                linha()
                print('ERRO! Tente novamente')
                linha()