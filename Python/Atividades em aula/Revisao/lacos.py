#REVISANDO OS METODOS DE LISTAS EM PYTHON CRIANDO UM TODO LIST 
tarefas = []

while True:
    escolha = int(input(
        '''
        1-Adicionar Tarefa
        2-Remover Tarefa
        3-Ver todas as Tarefas
        4-Ordenar todas as Tarefas
        5-Limpar todas as Tarefas
        6-Sair do programa
        '''
    ))

    match escolha:
        case 1:
            novaTarefa = input('Digitar a nova tarefa: ')
            tarefas.append(novaTarefa)
            print(f"Tarefa {novaTarefa} adicionada.")

        case 2:
            removerTarefa = input('Digite o nome da tarefa que será removida: ')
            if removerTarefa in tarefas:
                tarefas.remove(removerTarefa)
                print(f"Tarefa '{removerTarefa}' removida.")
            else:
                print(f'Tarefa {removerTarefa} não escontrada, tente novamente!')

        case 3:
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                print("Tarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa}")
        case 4:
            tarefas.sort()
            print(f'Tarefas ordenadas com sucesso!')
        
        case 5:
            tarefas.clear()
            print(f'As tarefas foram removidas!')
        
        case 6:
            print('Saindo do programa...')
            break

