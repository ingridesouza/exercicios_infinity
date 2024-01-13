# n é uma variável que é inicializada com o valor 1 e será usada como contador no loop.
n = 1
#-------------------------------------------------------------------------------------

# produto é uma variável que é inicializada com o valor 1 e será utilizada para acumular o produto dos números de 1 a 5.
produto = 1
#-------------------------------------------------------------------------------------

# Inicia um loop while que continuará enquanto o valor de n for menor ou igual a 5.
while n <= 5:
    #A cada iteração do loop, o valor de produto é multiplicado pelo valor atual de n e o resultado é armazenado novamente em produto. Isso acumula o produto dos números de 1 a 5.
    produto = produto * n
    
    #Incrementa o valor de n em 1 a cada iteração do loop. Isso é feito para garantir que o loop eventualmente termine e evite um loop infinito.
    n += 1

#O resultado final será que a variável produto conterá o valor do fatorial de 5, pois o loop multiplica os números de 1 a 5. O fatorial de 5 é 1 * 2 * 3 * 4 * 5, que é igual a 120.
    

#EXPLICAÇÃO 2 -
    
    # Neste código, estamos utilizando um laço de repetição "while" para multiplicar os números de 1 a 5 e armazenar o resultado na variável 'produto'. 


    # O laço inicia com 'n' igual a 1 e 'produto' igual a 1. A cada iteração do loop, o valor de 'n' é multiplicado pelo valor atual de 'produto'. Assim, na primeira iteração, temos 'produto' = 1 * 1, resultando em 'produto' = 1. Na segunda iteração, temos 'produto' = 1 * 2, resultando em 'produto' = 2. Esse processo se repete até que 'n' seja igual a 5, multiplicando 'produto' por 5 e obtendo 'produto' = 120. Portanto, ao final da execução do código, o VALOR FINAL de 'produto' será igual a 120.

# DICA -
    
    # A estrutura "for" é adequada quando o número de iterações é conhecido antecipadamente, enquanto a estrutura "while" é mais adequada quando o número de iterações é desconhecido ou depende de uma condição.

    # A estrutura for é geralmente utilizada quando se sabe antecipadamente quantas iterações serão necessárias, como percorrer elementos em uma lista, tupla ou outra sequência.

    # A estrutura while é mais apropriada quando o número de iterações não é conhecido antecipadamente ou quando as iterações dependem de uma condição que pode mudar durante a execução do programa.
    
    # Portanto, a escolha entre "for" e "while" depende das características específicas do problema que está sendo resolvido. Ambas as estruturas têm seus usos apropriados em diferentes situações.