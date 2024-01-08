#DICIONARIOS - {'chave' : 'valor'}

#Os dicionários são ideais para associar valores a chaves e fazer buscas rápidas por essas chaves.

professores = {"História": "Ingride",
               "Geografia" : "Leonardo",
               "Artes": "Ina",
               "Matemática" : "Leo"
               }
#-------------------------------------------
# exibe o valor da chave ["História"]/ exibe o valor do que ta na posicão História
# aulas = professores["História"]
# print(aulas)
#------------------------------------------
# adicionando novos itens
professores["Quimica"] = "Felipe"
print(professores)
#-----------------------------------------
# exibe as chaves do dicionario
# for i in professores:
    # print(i)
# print('-'*80)
#-----------------------------------------
alunos = {"Turma A" : "Alex",
          "Turma B" : "Tesla",
          "Turma C" : "Luciene"}
#-----------------------------------------
# exibe as chaves do dicionario
# for b in alunos:
#     print(b)
