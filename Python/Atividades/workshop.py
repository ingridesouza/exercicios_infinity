
while True:
    escolha = input('''
            escolha uma operação:
            1- contar de 1 a 10
            2- digitar um numero e verificar se ele é par
            3- digitar uma palavra e contar as letras
            4- encerrar o teste
            ''')
    print("-"*80)

    match escolha:
        case '1':
            for numero in range(1,10+1):
                print(numero)
        
        case '2':
            numero = int(input("Digite um número: "))
            print('par')if numero % 2 == 0 else print('impar')
        case '3':
            palavra = input("Digite uma palavra: ")
            for letras in palavra:
                print(letras)
            print(len(palavra))
        case '4':
            print("Fim do Programa")
            break
        case _ :
            print("opção inválida")