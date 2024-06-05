import tkinter as tk # importa a biblioteca Tkinter

def cadastrar_aluno():
    '''
    Cadastrar_aluno() = Coleta os dados dos campos de entrada, verifica se não estão vazios e se a idade e a nota são do tipo correto.
    '''
    nome = entry_nome.get()
    idade = entry_idade.get()
    nota = entry_nota.get()

    if not nome or not idade or not nota:
        print("ATENÇÃO!!!!Todos os campos são obrigatórios")
        return

    try:
        idade = int(idade)
        nota = float(nota)
    except ValueError:
        print("ATENÇÃO!!!!Idade deve ser um número inteiro e nota deve ser um número decimal")
        return

    # print(f"Nome: {nome}, Idade: {idade}, Nota: {nota}")
    message_print.insert(tk.END, f"Nome: {nome}, Idade: {idade}, Nota: {nota}\n")
    #usando o insert para inserir os dados dos alunos cadastrados

root = tk.Tk() #cria a janela principal
root.title("Cadastro de Alunos") #define o título da janela

#Criando os campos de entrada
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
#grid é para organizar os widtges em grade

entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_idade = tk.Label(root, text="Idade:")
label_idade.grid(row=1, column=0, padx=10, pady=5)

entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=2, column=0, padx=10, pady=5)

entry_nota = tk.Entry(root)
entry_nota.grid(row=2, column=1, padx=10, pady=5)

#Botão q chama a funçao de cadstrar o aluno
button_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_aluno)
button_cadastrar.grid(row=3, columnspan=2, pady=10)

message_print = tk.Text(root, height=10, width=40)
message_print.grid(row=4, columnspan=2, padx=10, pady=10)
#criando um widget Text para exibir os dados

#mainloop - ele inicia o loop, logo ele mantem a janela aberta, executando o codigo e exibindo a interface até q o usuário resolva fechar
root.mainloop()
