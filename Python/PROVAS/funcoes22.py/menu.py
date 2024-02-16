from funcoes import *

notas = []

while True:
    
    print('------- SISTEMA DE NOTAS -------')

    escolha = input('''
                    1 - Inserir notas do aluno
                    2- Calcular média e verificar situação do aluno
                    3- Sair
                    ''')
    
    match escolha:
        case '1':
            quantidade_notas = int(input("Quantas notas você deseja inserir? "))
            for i in range(quantidade_notas):
                nota = float(input(f"Digite a nota {i+1}: "))
                notas.append(nota)

            media = calcular_media(notas)
            situacao = verificar_situacao(media)

        case '2':
            if not notas:
                print("Digite as notas primeiro.")
            else:
                media = calcular_media(notas)
                situacao = verificar_situacao(media)
                print("A média do aluno é:", round(media, 2))
                print("Situação do aluno:", situacao)
        case '3': 
            print('Encerrando...')
            break
        case _:
            print('Opção Inválida, tente novamente')