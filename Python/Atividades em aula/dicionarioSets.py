# Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele: "maçã", "banana", "uva" , "laranja" e "morango". Em seguida, imprima o conjunto.

# frutas ={"maçã", "banana", "uva" , "laranja", "morango"}
# print(frutas)
# ------------------------------------------------------------------
# Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.

# frutas ={"maçã", "banana", "uva" , "laranja", "morango"}
# for banana in frutas:
#     print(banana)

#------------------------------------------
# Crie um conjunto chamado frutas_vermelhas e adicione as seguintes frutas a ele: "morango","cereja" e "framboesa". Em seguida, imprima o conjunto.

# frutas_vermelhas = set()
#set vazio -> variavel = set()

# frutas = ["morango","cereja", "framboesa"]
# variavel com as frutas para adicionar

# frutas_vermelhas.update(frutas)
#adicionando o conteudo de frutas em frutas vermelhas

# print(frutas_vermelhas)

#-----------------------------------------
# Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.


frutas_vermelhas = set()
#set vazio -> variavel = set()
frutas = "morango","cereja", "framboesa"
# o python reconhece uma tupla mesmo sem os parenteses
frutas_vermelhas.update(frutas)
# antes do discart lanço um print
print(frutas_vermelhas)
frutas_vermelhas.discard('cereja')
# descartando cereja
print(frutas_vermelhas)
# printando o set

print(type(frutas_vermelhas))


#--------------------------------------
#LISTAS E TUPLAS

#As listas e tuplas são estruturas de dados em Python que armazenam coleções de elementos. A principal diferença entre elas reside na mutabilidade. Listas são mutáveis [], o que significa que seus elementos podem ser modificados após a criação. Em contrapartida, tuplas são imutáveis (), tornando seus elementos fixos após a declaração.

#--------------------------------------

#DICIONARIOS E SETS

#Um "set" (conjunto) é uma coleção de elementos únicos e não ordenados. Isso significa que um conjunto não permite elementos duplicados e não mantém a ordem de inserção dos elementos.

#Método de adicionar no inicio do set -> add().
#Ao utilizar o método update para os sets, foram adicionados os valores de um set em outro, sem que haja valores duplicados, já que os conjuntos possuem um único valor de cada tipo. -> update()
#Sets não possibilitam acessar seus elementos através de índices (assim como Listas) ou chaves (como os Dicionários).

#Dicionários são uma das estruturas de dados que permitem armazenar valores associados a chaves.
#Os elementos de um dicionário são armazenados de forma não ordenada.
#