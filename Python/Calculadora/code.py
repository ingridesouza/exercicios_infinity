def somar(x,y):
        return x + y


def subtrair(x,y):
        return x - y

def multiplicar(x,y):
     return x * y

def dividir(x,y):
     return x / y


while True:
    number = int(input(
        '''
        CALCULADORA


        Digite um número: 
        '''
    ))
    option = input(
        '''
        + Somar
        - Subtrair
        x Multiplicar
        / Dividir
        S Sair
        '''
    )    
    number2 = int(input('Digite outro número: '))

    match option:
        case '+':
            print(f"O resultado da operação é: {somar(number,number2)}")
        
        case '-':
            print(f"O resultado da operação é: {subtrair(number, number2)}")

        case 'x':
            print(f"O resultado da operação é: {multiplicar(number,number2)}")
        
        case '/':
            print(f"O resultado da operação é: {dividir(number,number2)}")
        
        case 'S':
            print('Saindo do Sistema...')
            break

        case _: #dunder
            print('Número Inválido')

