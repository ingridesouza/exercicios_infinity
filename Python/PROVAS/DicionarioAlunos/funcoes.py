

def adicionar_aluno(alunos, nome_aluno, numero_matricula):
    novo_aluno = {
        'nome_aluno' : nome_aluno,
        'numero_matricula' : numero_matricula
    }
    alunos.append(novo_aluno)
    print(f'Aluno {nome_aluno} cadastrado com sucesso!')



def removerAluno(alunos, matricula_usuario_remover):
    for matricula in alunos:
        if matricula['numero_matricula'] == matricula_usuario_remover:
            matricula.remove(matricula)
            print(f'Aluno {matricula_usuario_remover} removido com sucesso!')
            return
        print( f'Matrícula não encontrada')


def atualizarAluno(alunos, numero_matricula, nome_aluno_atualizar):
    for aluno in alunos:
        if aluno['numero_matricula'] == numero_matricula:
            aluno['nome'] = nome_aluno_atualizar
            print(f'Nome do aluno com a matrícula {numero_matricula} atualizado com sucesso!')
            return
    print('Matrícula não encontrada...')


def verAlunos(alunos):
    print("Lista de todos os alunos:")
    for aluno in alunos:
        print(f"Matrícula: {aluno['numero_matricula']}, Nome: {aluno['nome']}")

def linha():
    print('-'*30)