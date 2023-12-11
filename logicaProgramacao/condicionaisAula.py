#1. Faça um Programa que peça dois números e imprima o maior deles. 



#2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# valor1 = input("Digite um valor:")

# if valor1 > "0":
#     print("O número é positivo")
# else:
#     print("O valor é negativo")
#--------------------------------------------------------------------------

#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# sexo = input("Digite o seu sexo:")

# if sexo == "F":
#     print("Seu sexo é Feminino.")
# elif sexo == "M" :
#     print("Seu sexo é Masculino.")
# else:
#     print("Sexo Inválido")
#------------------------------------------------------------------------------

#4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

#---------------------------------------------------------------------------
#5. Faça um programa para a leitura de duas notas parciais de um aluno. O
#programa deve calcular a média alcançada por aluno e apresentar:
#○ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#○ A mensagem "Reprovado", se a média for menor do que sete;
#○ A mensagem "Aprovado com Distinção", se a média for igual a dez.

# nota1 = 8
# nota2 = 3

# media = nota1 + nota2 / 2

# if media >= 7:
#     print("Aluno Aprovado")
# elif media < 7:
#     print("Aluno Reprovado")
# else:
#     print("Aluno Aprovado com Distinção")
#-----------------------------------------------------------------------------
# 6. Faça um Programa que leia três números e mostre o maior deles.
# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
#-----------------------------------------------------------------------------
# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
nome = input("Digite o seu nome:")
turno = input("Em qual turno você estuda?")

match turno:
    case "Matutino":
        print(f"Bom dia,{nome}!")
    case "Vespertino":
        print(f"Boa Tarde, {nome}!")
    case "Noturno":
        print(f"Boa noite,{nome}!")
    case _ :
        print("Valor Inválido")
#-----------------------------------------------------------------------------
# nome = input('nome: ')
# match nome:
#     case 'ingride':
#         print('seu nome é ', nome)
#     case _ :
#         print('nome não definido')
