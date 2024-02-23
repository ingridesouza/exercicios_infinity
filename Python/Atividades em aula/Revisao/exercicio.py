# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:

# O total de votos para cada candidato;

# A percentagem de votos nulos sobre o total de votos;

# A percentagem de votos em branco sobre o total de votos;

votosCandidatos = {'Jose' : 0,
                    'João' : 0,
                    'Augusto' : 0,
                    'Maria' : 0}

votosNulo = 0
votosBranco = 0


quantidadeVotos = int(input('Qual a quantidade de eleitorados?'))



for eleitores in range(quantidadeVotos):
    voto = int(input('''Digite o número do canditado: 
                     1 - José
                     2- João
                     3- Augusto
                     4- Maria
                     5- Nulo
                     6- Branco'''))
    match voto:
        case 1:
            votosCandidatos['Jose'] += 1
        case 2:
            votosCandidatos['João'] += 1
        case 3:
            votosCandidatos['Augusto'] += 1
        case 4:
            votosCandidatos['Maria'] += 1
        case 5:
            votosNulo += 1
        case 6:
            votosBranco += 1

totalVotosCandidatos = sum(votosCandidatos.values())

percentagemNulos = quantidadeVotos * (votosNulo/100)
percentagemBrancos = quantidadeVotos * (votosBranco/100)


