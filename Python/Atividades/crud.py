students = {}

while True:
    option = input('''
    INFINITY SCHOOL
    
    1- Adicionar Aluno
    2- Remover Aluno
    3- Visualizar Alunos Cadastrados
    
    Escolha uma das opções acima: 
    ''')
    print('-'*80)

    match option:
        case '1':
            studentName = input('Digite o nome do aluno que deseja adicionar: ')
            matricula = input('Digite o número de matrícula do aluno: ')
            #usei o print '-' só para organizar o terminal e conseguir visualizar direito cada passo
            print('-'*80)
            if matricula in students:
                print("Erro: Matrícula já existe no sistema.")
            else:
                students[matricula] = studentName
                print(f"Aluno {studentName} adicionado com sucesso!")
                print('-'*80)

        case '2':
            studentRemove = input('Informe o número de matrícula do aluno que deseja remover: ')

            if matricula in students:
                studentName = students.pop(matricula)
                print(f"Aluno {studentName} removido !")
            else:
                print("Erro: Matrícula não encontrada.")


        case '3':
            if not students:
                print("Não há alunos registrados no sistema.")
            else:
                print("\nLista de Alunos:")
                for matricula, nome in students.items():
                    print(f"Matrícula: {matricula}, Nome: {studentName}")

        case '4':
            print('Encerrando o sistema...')
            break

        case _ :
            print('Opção Inválida, tente novamente')