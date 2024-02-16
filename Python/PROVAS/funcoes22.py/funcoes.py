# Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.


def calcular_media(notas):
    soma = sum(notas)
    quantidade_notas = len(notas)
    media = soma / quantidade_notas
    return round(media)

def verificar_situacao(media):
    if media == 10:
        return f'Parabéns, sua média é 10'
    elif media >=7 :
        return f'Aluno aprovado com a média {media}'
    else:
        return 'Aluno Reprovado! ;('
    