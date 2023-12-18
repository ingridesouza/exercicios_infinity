# crie uma lista de compras com as opcoes do usuario
# criar lista, dar as opcoes ao usuario

listaCompras = []

while True:
    print('''
    1. Adicionar itens na lista
    2. Remover itens na lista
    3. Visualizar itens na lista
    4. Visualizar o tamanho da lista
          ''')

    escolha = int(input("Escolha uma das opções 1/2/3/4 \n ->"))


    if escolha == 1:
        itensLista = input("Digite um item para adicionar a lista:")
        listaCompras.append(itensLista)
       
    elif escolha == 2:
        removerItensLista = input("Digite um item para remover a lista:")
        listaCompras.remove(removerItensLista)

    elif escolha == 3:
        print(listaCompras)
    

    else:
        print("calma")