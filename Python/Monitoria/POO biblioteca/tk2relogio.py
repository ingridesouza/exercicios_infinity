import tkinter as tk
import time

def atualizar_horas():
    hora_atual = time.strftime('%H:%M:%S') #.strftime = formatar data e hora no formato que vc escrever e converte para STRING
    label_hora.config(text=hora_atual)
    root.after(1000, atualizar_horas)


root = tk.Tk()
root.title("Relógio Digital")


label_hora = tk.Label(root, font=('Arial', 24))
label_hora.pack(padx=20, pady=20)

# Chama a função de atualização do relógio para iniciar o relógio
atualizar_horas()


root.mainloop()
