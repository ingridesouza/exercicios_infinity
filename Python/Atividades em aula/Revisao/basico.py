# Exercicio usando laço de repetição if elif else
# user_year = int(input('Qual a sua idade?'))

# if user_year < 12:
#     print('Criança')
# elif user_year > 12 and user_year < 17:
#     print('Adolescente')
# elif user_year > 17 and user_year < 59:
#     print('Adulto')
# elif user_year > 60:
#     print('Idoso')
# -----------------------------------------------------

# Exercicio para pedir ao usuario 3 números e exibir o maior e o menor 
# while True:

#     number_1 =  float(input('Digite o primeiro número: '))
#     number_2 = float(input('Digite o segundo número: '))
#     number_3 = float(input('Digite o terceiro número: '))

#     if number_1 >= number_2 and number_1 >= number_3:
#         maior = number_1
#     elif number_2 >= number_1 and number_1 >= number_3:
#         maior = number_2
#     else:
#         maior = number_3

#     if number_1 <= number_2 and number_1 <= number_3:
#         menor = number_1
#     elif number_2 <= number_1 and number_1 <= number_3:
#         menor = number_2
#     else:
#         menor = number_3


#     print(f'O maior número é {maior} e o menor é o {menor}')

# ---------------------------------------------------

# Faça um programa que peça 10 números inteiros,calcule e mostre a quantidade de números pares e a quantidade de números impares.

# pares = 0
# impares = 0
#CRIAMOS AS VARIAVEIS PARA CONTAR OS NUMEROS PARES E IMPARES O USUARIO IRÁ DIGITAR, AMBAS INICIARAM COM O VALOR ZERO 

# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número inteiro: "))
#USAREMOS UM FOR QUE VAI DE 0 A 9, USANDO O RANGE 10, OU SEJA, ELE VAI ITERAR 10 VEZES

    # if numero % 2 == 0:
    #     pares += 1

    # else:
    #     impares += 1
#USANDO A ESTRUTURA CONDICIONAL IF, CRIAREMOS AS CONDIÇOES E INCREMENTAREMOS OS NÚMEROS, SE O O NÚMERO DIGITADO FOR DIVISIVEL POR 2 E TIVER O RESTO 0, ELE É PAR E SERÁ INCREMETADO A VARIAVEL "PARES" SENÃO SERÁ INCREMENTADO NA VARIAVEL "IMPARES"

# print(f"Quantidade de números pares: {pares}")
# print(f"Quantidade de números ímpares: {impares}")

#POR FIM, IREMOS IMPRIMIR A QUANTIDADE DE NÚMEROS IMPARES E PARES

# ------------------------------------------------------------

# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

#CRIAREMOS UMA VARIAVEL INPUT PARA RECEBER A QUANTIDADE DE PESSOAS DA TURMA 
# quantidade_turma = int(input('Digite a quantidade de pessoas da turma: '))

#CRIAREMOS UMA VARIAVEL PARA RECEBER A SOMA DAS IDADES, QUE SE INICIARÁ COM O VALOR ZERO
# soma_idades = 0 

#USANDO O FOR, SOLICITAREMOS AO USUARIO PARA DIGITAR A IDADE CONFORME A QUANTIDADE DE PESSOAS QUE FOI ARMAZENADA NA VARIAVEL 'QUANTIDADE_TURMA'. EM CADA ITERAÇÃO USAREMOS O INPUT PARA PEDIR A IDADE DE CADA PESSOA
# for i in range(quantidade_turma):

    # idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    #A IDADE É INSERIDA NA VARIAVEL ABAIXO E SENDO SOMADA A CADA ITERAÇÃO
    # soma_idades += idade

#CALCULAREMOS A MEDIA, DIVIDINDO A SOMA DAS IDADES PELA QUANTIDADE DE PESSOAS DA TURMA
# media_idades = soma_idades / quantidade_turma

# if media_idades >= 0 and media_idades <= 25:
#     print('A turma é jovem')
# elif media_idades >= 26 and media_idades <= 60:
#     print('A turma é Adulta')
# else:
#     print('A turma é idosa') 

#--------------------------------------------------------------

# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

quantidade_numeros = int(input('Digite a quantidade de números que será inserido: '))

#Solicita o primeiro número do conjunto
primeiro_numero = int(input("Digite um número: "))

#Inicializa menor_valor, soma_valores e maior_valor com este número
menor_valor = primeiro_numero
maior_valor = primeiro_numero
soma_valores = primeiro_numero

# Solicita os números restantes e atualiza as variáveis
#Um laço for que itera n - 1 vezes (já que o primeiro número já foi processado).
for i in range(quantidade_numeros - 1):
    numero = int(input("Digite um número: "))
    if numero < menor_valor:
        menor_valor = numero
    if numero > maior_valor:
        maior_valor = numero
    soma_valores += numero

# Exibe os resultados
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
print("Soma dos valores:", soma_valores)
