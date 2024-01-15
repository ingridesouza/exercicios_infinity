# Definição da função para adicionar um aluno ao dicionário 'alunos'
def adicionar_aluno(alunos, nome_aluno, numero_matricula):
    # Cria um novo dicionário representando o aluno a ser adicionado
    novo_aluno = {
        'nome_aluno': nome_aluno,
        'numero_matricula': numero_matricula
    }
    # Adiciona o novo aluno a lista de alunos
    alunos.append(novo_aluno)
    # Imprime uma mensagem indicando que o aluno foi cadastrado com sucesso
    print(f'Aluno {nome_aluno} cadastrado com sucesso!')


#-----------------------------------------------------------------
    
# Definição da função para remover um aluno do dicionário 'alunos'
def removerAluno(alunos, matricula_usuario_remover):
    # Percorre a lista de alunos para encontrar o aluno com a matrícula a ser removida
    for aluno in alunos:
        if aluno['numero_matricula'] == matricula_usuario_remover:
            # Remove o aluno da lista
            alunos.remove(aluno)
            # Imprime uma mensagem indicando que o aluno foi removido com sucesso
            print(f'Aluno {matricula_usuario_remover} removido com sucesso!')
            return
    # Se a matrícula não for encontrada, imprime uma mensagem indicando que a matrícula não foi encontrada
    print('Matrícula não encontrada')


#-----------------------------------------------------------------

# Definição da função para atualizar o nome de um aluno no dicionário 'alunos'
def atualizarAluno(alunos, numero_matricula, nome_aluno_atualizar):
    # Percorre a lista de alunos para encontrar o aluno com a matrícula a ser atualizada
    for aluno in alunos:
        if aluno['numero_matricula'] == numero_matricula:
            # Atualiza o nome do aluno
            aluno['nome_aluno'] = nome_aluno_atualizar
            # Imprime uma mensagem indicando que o nome do aluno foi atualizado com sucesso
            print(f'Nome do aluno com a matrícula {numero_matricula} atualizado com sucesso!')
            return
    # Se a matrícula não for encontrada, imprime uma mensagem indicando que a matrícula não foi encontrada
    print('Matrícula não encontrada...')


#-----------------------------------------------------------------

# Definição da função para listar todos os alunos no dicionário 'alunos'
def verAlunos(alunos):
    # Imprime uma mensagem indicando que a lista de alunos será exibida
    print("Lista de todos os alunos:")
    # Percorre a lista de alunos e imprime as informações de cada aluno
    for aluno in alunos:
        print(f"Matrícula: {aluno['numero_matricula']}, Nome: {aluno['nome_aluno']}")


#-----------------------------------------------------------------

# Definição da função para imprimir uma linha de caracteres '-' para melhorar a apresentação visual
def linha():
    print('-'*30)
