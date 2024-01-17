#Considere uma lista de números inteiros 
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:

# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

# Função filter() para obter uma nova lista com números pares da lista numeros

# Função reduce()  para obter a soma de todos os números da lista numeros

# Qual o resultado obtido após a execução das operações acima?

from functools import reduce

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
quadrados = list(map(lambda x: x**2, lista_numeros))

# Função filter() para obter uma nova lista com números pares da lista numeros
numeros_pares = list(filter(lambda x: x % 2 == 0, lista_numeros))

# Função reduce()  para obter a soma de todos os números da lista numeros
soma_total = reduce(lambda x, y: x + y, lista_numeros)

# RESULTADOS
print(f"Lista com o quadrado de cada número: {quadrados}")
print(f"Lista com números pares: {numeros_pares}")
print(f"Soma de todos os números:{soma_total}")

