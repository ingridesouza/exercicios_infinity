quantidade_numeros = 0
soma_numeros = 0

while True:
    numero = int(input("Digite um número (digite 0 para sair): "))
    
    if numero == 0:
        break
    
    quantidade_numeros += 1
    soma_numeros += numero

if quantidade_numeros > 0:
    media = soma_numeros / quantidade_numeros
else:
    media = 0

#resultados
print("Quantidade de números digitados:", quantidade_numeros)
print("Soma dos números digitados:", soma_numeros)
print("Média dos números digitados:", media)
