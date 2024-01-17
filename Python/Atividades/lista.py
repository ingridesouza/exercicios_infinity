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

            match escolha:

                case '1':
                    itensLista = input("Digite um item para adicionar a lista:")
                    listaCompras.append(itensLista)
                
                case '2':
                    removerItensLista = input("Digite um item para remover a lista:")
                    listaCompras.remove(removerItensLista)

                case '3':
                    print(listaCompras)
                

                case '4':
                    print(len(listaCompras))

                case '5':
                    break