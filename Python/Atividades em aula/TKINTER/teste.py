#label - Usado para exibir texto na tela.
#entry - Widget de entrada de dados que permite apenas uma única linha de texto.
#button - Um botão que pode conter texto e realizar uma ação quando clicado.
#checkbox - Uma caixa de seleção para implementar ações do tipo liga/desliga.
#radiobutton - Uma caixa de seleção para implementar uma de muitas seleções.


#----------------------------------------------------------------
import tkinter as tk

#Instaciar a janela (Criação da janela)

janela = tk.Tk()

#----------------------------------------------------------------
#Label (Rótulo)
texto_exemplo = tk.Label(janela, text='Ingride Linda', font= ('Arial', 12))
texto_exemplo.pack()


#----------------------------------------------------------------
#Text (Caixa de Texto)

Email = tk.Text(janela, height= 3, width= 20, wrap='word')
Email.insert(tk.END, 'Insira seu Email')
#----------------------------------------------------------------
#Entry (Campo de Entrada)
entry_text = tk.StringVar()
Entry = tk.Entry(janela, textvariable=entry_text, show='*')
# Senha = tk.Text(janela, height= 3, width= 20, wrap='word')
# Senha.insert(tk.END, 'Insira sua Senha')
#height = linhas
#width = caracteres


Email.pack()
Entry.pack()
# Senha.pack()
#----------------------------------------------------------------
# radio_var = tk.StringVar()

# Feminino = tk.Radiobutton(janela, text='Feminino', variable=radio_var, value= 'option2')
# Masculino = tk.Radiobutton(janela, text='Masculino', variable=radio_var, value= 'option1')
# Feminino.pack()
# Masculino.pack()
#-----------------------------------------------------------------
#Checkbutton (Botão de Verificação)
#variaveis de controles - uma pra cada botão para não dar erro
check_var = tk.BooleanVar()
check_var2 = tk.BooleanVar()

Feminino1 = tk.Checkbutton(janela, text='Masculino', variable=check_var)
Masculino1 = tk.Checkbutton(janela, text='Feminino', variable=check_var2)
Feminino1.pack()
Masculino1.pack()

#--------------------------------------------------------------

menu = tk.Menu(janela)
janela.config(menu=menu)
file_menu = tk.Menu (menu)
menu.add_cascade(label='Arquivo', menu= file_menu)
file_menu.add_command(label='Abrir')
file_menu.add_command(label='Salvar')
file_menu.add_separator()
file_menu.add_command(label='Sair')
#----------------------------------------------------------------
#Frame (quadro)
frame = tk.Frame(janela,relief=tk. RAISED, borderwidth=5)
frame.pack()
#----------------------------------------------------------------
scale_var = tk.DoubleVar
scale = tk.Scale(janela, from_=1, to=50, orient=tk. HORIZONTAL, variable=scale_var)
scale2 = tk.Scale(janela, from_=50, to=1, orient=tk. VERTICAL, variable=scale_var)
scale.pack() 
scale2.pack() 
#----------------------------------------------------------------
#Canvas (Tela)
canvas = tk.Canvas(janela, width=200, height=300)
canvas.pack()
canvas.create_rectangle(10,10,100,60,fill='pink')

#----------------------------------------------------------------
def button_click():
    texto_exemplo.config(text='Deu certo!')

#----------------------------------------------------------------
#Button (Botão)  
Button = tk.Button(janela, text='Clique em mim!', command=button_click)
Button.pack()

#----------------------------------------------------------------
#Checkbutton (Botão de Verificação)
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(janela, text='Aceitar termos', variable=check_var)
checkbutton.pack()
#----------------------------------------------------------------
#----------------------------------------------------------------
 
janela.mainloop()