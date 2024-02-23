# Você está desenvolvendo um programa para gerenciar uma lista de compras. O programa permite adicionar produtos à lista, visualizar a lista de produtos, atualizar as informações de um produto existente e remover produtos da lista. Além disso, o programa calcula o valor total de todos os produtos da lista.
# O programa oferece as seguintes opções:

# Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade e o valor unitário do produto. O programa calcula automaticamente o valor total do produto (quantidade * valor unitário) e atualiza o valor total de todos os produtos.

# Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total de todos os produtos da lista.

# Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. O programa solicita o nome do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.

# Remover produto: O usuário pode remover um produto da lista informando o nome do produto que deseja remover. O programa atualiza automaticamente o valor total de todos os produtos.

# Encerrar programa: Encerra a execução do programa.

# O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as informações: "produto", "valor", "quantidade" e "total". A variável totalProdutos é utilizada para armazenar o valor total de todos os produtos da lista.

# A cada operação realizada, o programa exibe mensagens indicando o resultado da operação.

import funcoes

listaProdutos = []
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
            funcoes.adicionarProduto(nomeProduto, quantidadeProduto, valorUnitario)
            
        case '2':
            print('----------LISTA DE PRODUTOS----------')
            funcoes.visualizarListaProdutos(listaProdutos)
            
        case '3':
            print('----------ATUALIZAR INFORMAÇÕES DO PRODUTO----------')
            nomeProduto = input('Digite o nome do produto que deseja atualizar: ')
            novoNome = input('Digite o novo nome do produto: ')
            novaQuantidade = int(input('Digite a nova quantidade do produto: '))
            novoValorUnitario = float(input('Digite o novo valor unitário do produto: '))
            funcoes.atualizarProduto(listaProdutos ,nomeProduto, novoNome, novaQuantidade, novoValorUnitario) 
        
        case '4':
            print('----------REMOVER PRODUTO----------')
            removerNomeProduto = input('Insira o nome do produto que deseja remover: ')
            funcoes.removerProduto(listaProdutos, removerNomeProduto)
            
        case '5':
            print('Programa encerrado. Até logo!')
            break
        case _:
            print('Opção Inválida. Tente Novamente.')
