# def soma(x,y):
#     return x+y

# soma(5,6)

# print(soma(5,6))

# print com o 'soma' sem paranteses da erro pq o sistema ler como variavel, 'soma' precisa dos parenteses e dos argumentos
#---------------------------------------------
# def - palavra reservada para criar funções
# (x,y) - Parâmetros
# return x+y - corpo da função
# soma (5,6) - Argumentos; Chamada da função
# return - retorna algo na função, 
# soma - nome da função
# print - fora da função
# virgula - É o separador
#---------------------------------------------
# Paradigma procedural - Ler de cima pra baixo, da esquerda pra direita
# Paradigma Funcional - Realiza computações através da avaliação de funções, evitando mudança de estado e dados mutáveis.
# Evitar colocar print ou input dentro de funções pq elas são funções depuradoras
#----------------------------------------------------------------------------------------

#Crie uma função que receba um nome e imprima uma saudação personalizada.

# nome = input("Digite o seu nome: ")

# def saudacao(nome):
#     return f"Seja Bem-Vindo, {nome}"

# print(saudacao(nome))

#----------------------------------------------------------------------------------------

# Crie uma função que receba um horário e imprima "Bom dia!" , "Boa tarde!" ou "Boa noite!" conforme o horário.

# horas = int(input("Digite que horas são: "))

# def saudacao(horas):
#     if horas >= 0 and horas <= 12:
#         return "Bom dia!"

#     elif horas >= 12 and horas <= 17:
#         return "Boa tarde!"
    
#     elif horas >= 17 and horas <= 23:
#         return "Boa noite!"
#     else:
#         return "Horário Inválido"
    
# print(saudacao(horas))
#----------------------------------------------------------------------------------------

# Crie uma função que receba dois números e retorne a soma deles.

# def soma(x,y):
#     return x+y
# soma(12,98)
# print(soma(12,98))

#------------------------------

# def soma(x,y):
#     return x+y

# soma(12,98)
# resultado = soma(12,98)
# print(resultado)

#----------------------------------------------------------------------------------------
#valores padrões sempre são os ultimos.
# def exemplo(x,y=4): - o y teve o seu valor definido na função
# Ele tbm pode ser redefinido no print -> exemplo: print(exemplo(7,9)) o y agora é 9.
# Crie uma função que receba dois números e retorne a subtração do primeiro pelo segundo.

# def subtracao(x,y):
#     return x-y

# subtracao(12,98)
# resultado = subtracao(12,98)
# print(resultado)

#-------------------------------------------------------------------------------
# Crie uma função que receba dois números e retorne a multiplicação deles.

# def multiplicar (x,y=5):
#     return x*y

# print(multiplicar(9,3))

#------------------------------------------------------------------------------ 

# Crie uma calculadora com opções de soma, multiplicação, subtração, divisão e sair.

# (Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)

# Utilize funções de rotina para cada operação e funções de unidade lógica para realizar os cálculos.

# Dica:
# Utilize de condicionais e Laços de Repetição para realizar esse exercício.

# match case só aceita IGUALDADE

def somar(x,y):
        return x + y


def subtrair(x,y):
        return x - y

def multiplicar(x,y):
     return x * y

def dividir(x,y):
     return x / y


while True:


    number = int(input(
        '''
        CALCULADORA


        Digite o número: 
        '''
    ))

    option = input(
        '''
        + Somar
        - Subtrair
        x Multiplicar
        / Dividir
        S Sair
        '''
    )    

    number2 = int(input('Digite outro número: '))

    match option:
        case '+':
            print(f"O resultado da operação é: {somar(number,number2)}")
        
        case '-':
            print(f"O resultado da operação é: {subtrair(number, number2)}")

        case 'x':
            print(f"O resultado da operação é: {multiplicar(number,number2)}")
        
        case '/':
            print(f"O resultado da operação é: {dividir(number,number2)}")
        
        case 'S':
            print('Saindo do Sistema...')
            break

        case _: #dunder
            print('Número Inválido')

