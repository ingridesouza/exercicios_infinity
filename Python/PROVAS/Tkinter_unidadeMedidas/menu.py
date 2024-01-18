import tkinter as tk

janela = tk.Tk()

def button_click():
    try:
        # Capturo o valor da entra em Float
        centimetros_usuario1 = float(entrada.get())
        
        # Calculo
        numeroConvertido = centimetros_usuario1 / 100
        
        # Resultado atualizado
        resultado.config(text=f'{centimetros_usuario1} centímetros são {numeroConvertido} metros')

    except ValueError:
        # Exceção para lidar com erro
        resultado.config(text='Erro: Insira um valor numérico válido')

titulo = tk.Label(janela, text='Conversor de centímetros para metros', font=('Arial', 12), background= 'gray', fg='white')
titulo.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text='Confira', command=button_click)
botao.pack()

resultado = tk.Label(janela, text='')
resultado.pack()

janela.mainloop()
