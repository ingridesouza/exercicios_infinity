#  Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.

valores = []

# loop que solicita ao usuário que insira 10 valores
for i in range(10):
    # converte a entrada do usuário para inteiro e adiciona à lista 'valores'
    escolha = int(input(f'Digite o {i + 1} valor: '))
    valores.append(escolha)


# cria uma lista numeros_pares utilizando list comprehensions para armazenar os números pares.
numeros_pares = [num for num in valores if num % 2 == 0]

# cria uma lista numeros_pares utilizando list comprehensions para armazenar os números impares.
numeros_impares = [num for num in valores if num % 2 != 0]

# números pares
print('-'*50)
print(f'Números Pares: {numeros_pares}')

# números ímpares em formato de tupla
print(f'Números Ímpares: {tuple(numeros_impares)}')

# quantidade de números pares
print(f'Quantidade de Números Pares: {len(numeros_pares)}')

# quantidade de números ímpares
print(f'Quantidade de Números Ímpares: {len(numeros_impares)}')

# soma de números pares
# sum é utilizado para calcular a soma dos elementos nas listas. 
soma_pares = sum(numeros_pares)
print(f'Soma de Números Pares: {soma_pares}')

# soma de números ímpares
soma_impares = sum(numeros_impares)
print(f'Soma de Números Ímpares: {soma_impares}')

# soma de todos os números
soma_total = sum(valores)
print(f'A soma de todos os números é: {soma_total}')