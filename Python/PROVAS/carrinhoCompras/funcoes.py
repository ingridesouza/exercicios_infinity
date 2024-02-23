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
# listaProdutos = []

# def adicionarProduto(nomeProduto, quantidadeProduto, valorUnitario):
#     novoProduto = { 
#         'nome': nomeProduto,
#         'quantidade': quantidadeProduto,
#         'valorUnitario': valorUnitario
#     }
#     listaProdutos.append(novoProduto)
#     print('-'*50)
#     print(f'Produto {nomeProduto} adicionado com sucesso')

# def visualizarListaProdutos(listaProdutos):
#     if not listaProdutos:
#         print('-'*50)
#         print("A lista de produtos está vazia.")
#     else:
#         for indice, produto in enumerate(listaProdutos, start=1):
#             print('-'*50)
#             nome = produto.get('nome', 'Nome não encontrado')
#             valor_unitario = produto.get('valorUnitario', 'Valor unitário não encontrado')
#             quantidade = produto.get('quantidade', 'Quantidade não encontrada')
#             print(f"{indice} - {nome}, Valor Unitário: {valor_unitario}, Quantidade: {quantidade}")

# def atualizarProduto(listaProdutos, nomeProduto, novoNome, novaQuantidade, novoValorUnitario):
#     for produto in listaProdutos:
#         if produto['nome'] == nomeProduto:
#             produto['nome'] = novoNome
#             produto['quantidade'] = novaQuantidade
#             produto['valorUnitario'] = novoValorUnitario
#             print('-'*50)
#             print(f'Produto {nomeProduto} atualizado com sucesso.')
#             return
#     print('-'*50)
#     print(f'Produto {nomeProduto} não encontrado.')

# def removerProduto(listaProdutos, nomeProduto):
#     for produto in listaProdutos:
#         if produto['nome'] == nomeProduto:
#             listaProdutos.remove(produto)
#             print('-'*50)
#             print(f'Produto {nomeProduto} removido com sucesso!')
#             return
#     print('-'*50)
#     print(f'Produto {nomeProduto} não encontrado.')