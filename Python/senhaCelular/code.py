# Simulador de cadastro de senha e inicialização de celular

print("CADASTRO DE SENHA")
senha = input("Digite a senha desejada: ")


print("\nINICIALIZAÇÃO DO CELULAR")


for tentativa in range(3, 0, -1):
    entrada_senha = input("Digite a senha para desbloquear o celular: ")
    
    if entrada_senha == senha:
        print("Bem-vindo!")
        break
    else:
        if tentativa == 1:
            print("Senha incorreta. Você tem 1 tentativa restante. O celular será bloqueado após esta tentativa.")
        else:
            print(f"Senha incorreta. Você tem {tentativa - 1} tentativas restantes.")

else:
    print("O celular foi bloqueado. Por favor, entre em contato com o suporte.")
