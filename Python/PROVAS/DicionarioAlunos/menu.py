# [PY-A07] Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. 
# O programa deve permitir adicionar, remover, atualizar e listar os alunos. 
# Para isso, você deve implementar um módulo que contém as seguintes funções:
#-----------------------------------------------------------------------------


# Importa as funções definidas no módulo 'funcoes' e o módulo 'bancoDados'
from funcoes import *
from bancoDados import *

# Loop principal que mantém o programa em execução continuamente
while True:
    
    # Imprime o menu de opções para o usuário
    print(''' 
            1- Adicionar Aluno.
            2- Remover Aluno.
            3- Aualizar Aluno.
            4- Ver Alunos.
            5- Sair.
            ''')
    
    # Solicita ao usuário que digite a opção desejada
    escolha = input('Digite o número da opção desejada: -->')

    
    #Uso a instrução 'match' para avaliar a escolha do usuário e executar a ação correspondente.
    match escolha:
        case '1':
            # Solicita ao usuário o nome e número de matrícula do aluno a ser adicionado
            nome_aluno = input('Digite o nome do aluno que deseja adicionar: ')
            numero_matricula = input('Digite o número da matrícula do mesmo: ')
            linha()
            # Chama a função 'adicionar_aluno', fornecendo os argumentos inseridos pelo usuário.
            adicionar_aluno(alunos, nome_aluno, numero_matricula)
            linha()

        case '2':
            # Solicita ao usuário o número de matrícula do aluno a ser removido
            matricula_usuario_remover = int(input('Digite o número da matrícula do aluno que deseja remover: '))
            linha()
            # Chama a função 'removerAluno' fornecendo os argumentos inseridos pelo usuário.
            removerAluno(alunos, matricula_usuario_remover)
            linha()

        case '3':
            # Solicita ao usuário o número de matrícula do aluno e o novo nome
            numero_matricula = input('Digite o número da matrícula do aluno que deseja atualizar: ')
            nome_aluno_atualizar = input('Insira o nome atualizado do aluno: ')
            linha()
            # Chama a função 'atualizarAluno' fornecendo os argumentos inseridos pelo usuário.
            atualizarAluno(alunos, numero_matricula, nome_aluno_atualizar)
            linha()

        case '4':
            linha()
            # Chama a função 'verAlunos' para listar todos os alunos cadastrados
            verAlunos(alunos)
            linha()

            # Sai do programa usando o break quando a opção '5' é escolhida
        case '5':
            print("Saindo do programa. Até logo!")
            break

        case _:
            linha()
            # Imprime uma mensagem de erro se a escolha do usuário não corresponder a nenhuma opção válida
            print('ERRO! Tente novamente')
            linha()
