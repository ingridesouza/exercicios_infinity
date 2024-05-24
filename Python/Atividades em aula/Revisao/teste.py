#Metodo Del => remove um item na lista com base no seu indice

print('Metodo DEL')
alunos = ['Ingride', 'Ander', 'Clarice', 'Wili', 'Doja']
print(f'Lista anterior{alunos}')

del(alunos[1])
print(f'Lista atual{alunos}')
#------------------------------
print('-'*80)
#------------------------------
# Metodo Remove => remove a primeira ocorrencia do elemento com base no seu valor

print('Metodo Remove')
notas = [6,4,4,5,1,1]
print(f'Notas anteriores {notas}')

notas.remove(4)
print(f'Notas atuais {notas}')

#------------------------------
print('-'*80)
#------------------------------
#Metodo append => adiciona um elemento ao final da lista

objetos = ['mesa', 'cadeira', 'teclado','monitor','gabinete']
objetos.append('mouse')
print(objetos)

#------------------------------
print('-'*80)
#------------------------------
#Metodo insert => insere um elemento na lista utilizando dois parametros. 1 Paramentro = indice que será inserido, 2 Parametro => o elemento que será inserido no indice expecificado

materiais = ['lapis','caneta','marca-texto']
print(f'Lista anterior {materiais}')

materiais.insert(1,'borracha')
print(f'Lista atualizada {materiais}')

#------------------------------
print('-'*80)
#------------------------------
#Metodo pop

frutas = ['maçã', 'banana', 'laranja', 'pera', 'uva']
print(f'Lista anterior {frutas}')

#remove e retorna um elemento de uma posição especifica
frutaRemovida = frutas.pop(2)
print(f'Salada Mista atuallizada {frutas}')
print(f'A fruta {frutaRemovida} foi removida da nossa salada!')

#------------------------------
print('-'*80)
#------------------------------
# Função Len() => utilizada para exibir a quantidade de elementos da lista


planetaSistema = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']
print(len(planetaSistema))

#------------------------------
print('-'*80)
#------------------------------
#Acessar um elemento pelo seu indice

cores = ['Vermelho', 'Laranja', 'Amarelo', 'Verde', 'Azul', 'Anil', 'Violeta']
print(cores[4])

#------------------------------
print('-'*80)
#------------------------------

#Alterar um elemento pela sua posição

livros_classicos = ['Dom Quixote','Moby Dick', 'Guerra e Paz', 'Orgulho e Preconceito', '1984']

livros_classicos[3] = 'Ingride'
print(livros_classicos)

#-------------------------------
#Metodo extend => concatenar ou combinar duas listas em uma unica lista, modificando a lista original diretamente

livros = ['Dom Quixote','Moby Dick', 'Guerra e Paz']
classicos = [ 'Orgulho e Preconceito', '1984', 'ingride', 'jorge']

livros.extend(classicos)
print(livros)

#--------------------------
print('-'*80)
#--------------------------
#Metodo index => retorna o indice da primeira ocorrencia do elemento

nomes = ['Maria', 'João', 'Ana', 'Pedro', 'João', 'Luana']

indice_luana = nomes.index('Luana')

print("O índice da primeira ocorrência de 'Luana' é:", indice_luana)

#--------------------------
print('-'*80)
#--------------------------

