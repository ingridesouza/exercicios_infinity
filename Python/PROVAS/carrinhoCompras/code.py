listaProdutos = []
totalProdutos = 0

def adicionarProduto(nomeProduto, quantidadeProduto, valorUnitario):
    totalProduto = round(quantidadeProduto * valorUnitario, 2)
    novoProduto = { 
        'nome': nomeProduto,
        'quantidade': quantidadeProduto,
        'valorUnitario': valorUnitario,
        'total': totalProduto
    }
    listaProdutos.append(novoProduto)
    global totalProdutos
    totalProdutos += totalProduto
    print('-'*50)
    print(f'Produto {nomeProduto} adicionado com sucesso')

def visualizarListaProdutos(listaProdutos):
    if not listaProdutos:
        print('-'*50)
        print("A lista de produtos está vazia.")
    else:
        for indice, produto in enumerate(listaProdutos, start=1):
            print('-'*50)
            nome = produto.get('nome', 'Nome não encontrado')
            valor_unitario = produto.get('valorUnitario', 'Valor unitário não encontrado')
            quantidade = produto.get('quantidade', 'Quantidade não encontrada')
            total = produto.get('total', 'Total não encontrado')
            print(f"{indice} - {nome}, Valor Unitário: {valor_unitario}, Quantidade: {quantidade}, Total: {total}")
        print('-'*50)
        print(f'Valor total de produtos: {round(totalProdutos)}')

def atualizarProduto(listaProdutos, nomeProduto, novoNome, novaQuantidade, novoValorUnitario):
    totalProdutos = 0
    for produto in listaProdutos:
        if produto['nome'] == nomeProduto:
            totalProdutoAntigo = produto['total']
            produto['nome'] = novoNome
            produto['quantidade'] = novaQuantidade
            produto['valorUnitario'] = novoValorUnitario
            produto['total'] = round(novaQuantidade * novoValorUnitario, 2)
            totalProdutos += produto['total']
            totalProdutos -= totalProdutoAntigo
            print('-'*50)
            print(f'Produto {nomeProduto} atualizado com sucesso.')
        else:
            totalProdutos += produto['total']
    return listaProdutos, totalProdutos


def removerProduto(listaProdutos, nomeProduto):
    totalProdutos = 0
    for produto in listaProdutos:
        if produto['nome'] == nomeProduto:
            totalProdutos -= produto['total']
            listaProdutos.remove(produto)
            print('-'*50)
            print(f'Produto {nomeProduto} removido com sucesso!')
            return listaProdutos, totalProdutos
        else:
            totalProdutos += produto['total']
    print('-'*50)
    print(f'Produto {nomeProduto} não encontrado.')
    return listaProdutos, totalProdutos

#----------------------------------------------------


while True:
    print('---------------LISTA DE COMPRAS---------------')
    print('----------SELECIONE A OPÇÃO DESEJADA----------')
    escolha = input('''
                    1- Adicionar Produto à lista
                    2- Visualizar lista
                    3- Atualizar informações de um produto da lista
                    4- Remover produto da lista
                    5- Encerrar programa
                    ''')
    match escolha:
        case '1':
            print('----------ADICIONAR PRODUTO----------')
            nomeProduto = input('Digite o nome do produto para adicionar: ')
            quantidadeProduto = int(input('Insira a quantidade do produto a ser adicionado: '))
            valorUnitario = float(input('Insira o valor unitário do produto: '))
            adicionarProduto(nomeProduto, quantidadeProduto, valorUnitario)
            
        case '2':
            print('----------LISTA DE PRODUTOS----------')
            visualizarListaProdutos(listaProdutos)
            
        case '3':
            print('----------ATUALIZAR INFORMAÇÕES DO PRODUTO----------')
            nomeProduto = input('Digite o nome do produto que deseja atualizar: ')
            novoNome = input('Digite o novo nome do produto: ')
            novaQuantidade = int(input('Digite a nova quantidade do produto: '))
            novoValorUnitario = float(input('Digite o novo valor unitário do produto: '))
            atualizarProduto(listaProdutos ,nomeProduto, novoNome, novaQuantidade, novoValorUnitario) 
        
        case '4':
            print('----------REMOVER PRODUTO----------')
            removerNomeProduto = input('Insira o nome do produto que deseja remover: ')
            removerProduto(listaProdutos, removerNomeProduto)
            
        case '5':
            print('Programa encerrado. Até logo!')
            break
        case _:
            print('Opção Inválida. Tente Novamente.')
