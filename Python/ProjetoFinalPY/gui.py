# gui.py
import tkinter as tk
from tkinter import messagebox
from tarefa import Tarefa
from database import DatabaseManager
from datetime import datetime

class GerenciadorTarefasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Tarefas")
        self.master.configure(bg="white")

        # Definindo a fonte Times New Roman
        self.fonte_times_new_roman = ("Times New Roman", 12)

        self.stark_label = tk.Label(master, text="Stark Corporation", bg="black", fg="white", font=self.fonte_times_new_roman)
        self.stark_label.grid(row=0, columnspan=3, pady=10)

        self.tarefas = []

        self.nome_label = tk.Label(master, text="Nome:", bg="white", fg="black", font=self.fonte_times_new_roman)
        self.nome_label.grid(row=1, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(master, width=50, font=self.fonte_times_new_roman)
        self.nome_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        self.descricao_label = tk.Label(master, text="Descrição:", bg="white", fg="black", font=self.fonte_times_new_roman)
        self.descricao_label.grid(row=2, column=0, padx=5, pady=5)
        self.descricao_entry = tk.Entry(master, width=50, font=self.fonte_times_new_roman)
        self.descricao_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        self.inicio_label = tk.Label(master, text="Data de Início:", bg="white", fg="black", font=self.fonte_times_new_roman)
        self.inicio_label.grid(row=3, column=0, padx=5, pady=5)
        self.inicio_entry = tk.Entry(master, width=20, font=self.fonte_times_new_roman)
        self.inicio_entry.grid(row=3, column=1, padx=5, pady=5)

        self.fim_label = tk.Label(master, text="Data de Término:", bg="white", fg="black", font=self.fonte_times_new_roman)
        self.fim_label.grid(row=4, column=0, padx=5, pady=5)
        self.fim_entry = tk.Entry(master, width=20, font=self.fonte_times_new_roman)
        self.fim_entry.grid(row=4, column=1, padx=5, pady=5)

        self.status_label = tk.Label(master, text="Status:", bg="white", fg="black", font=self.fonte_times_new_roman)
        self.status_label.grid(row=5, column=0, padx=5, pady=5)
        self.status_var = tk.StringVar(master)
        self.status_var.set("A Fazer")
        self.status_menu = tk.OptionMenu(master, self.status_var, "A Fazer", "Em Andamento", "Concluído")
        self.status_menu.grid(row=5, column=1, padx=5, pady=5)

        self.adicionar_button = tk.Button(master, text="Adicionar Tarefa", command=self.adicionar_tarefa, bg="red", fg="white", font=self.fonte_times_new_roman)
        self.adicionar_button.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

        self.remover_button = tk.Button(master, text="Remover Tarefas Concluídas", command=self.remover_tarefas_concluidas, bg="red", fg="white", font=self.fonte_times_new_roman)
        self.remover_button.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        self.tarefas_frame = tk.Frame(master, bg="white")
        self.tarefas_frame.grid(row=8, column=0, columnspan=3, padx=5, pady=5)
        self.mostrar_tarefas()

        # Conectar ao banco de dados MySQL
        self.db_manager = DatabaseManager()

    def adicionar_tarefa(self):
        nome = self.nome_entry.get()
        descricao = self.descricao_entry.get()
        inicio = self.inicio_entry.get()
        fim = self.fim_entry.get()
        status = self.status_var.get()

        # Convertendo a string de data para objeto datetime
        data_inicio = datetime.strptime(inicio, "%d-%m-%Y")
        data_fim = datetime.strptime(fim, "%d-%m-%Y")

        # Formatando a data no formato 'YYYY-MM-DD'
        inicio_formatado = data_inicio.strftime("%Y-%m-%d")
        fim_formatado = data_fim.strftime("%Y-%m-%d")

        tarefa = Tarefa(nome, descricao, inicio_formatado, fim_formatado, status)
        self.tarefas.append(tarefa)
        self.db_manager.salvar_tarefa(tarefa)
        self.mostrar_tarefas()
        self.limpar_campos()

    def mostrar_tarefas(self):
        for widget in self.tarefas_frame.winfo_children():
            widget.destroy()

        bg_color = ["white", "lightgrey"]
        for i, tarefa in enumerate(self.tarefas, start=1):
            descricao_label = tk.Label(self.tarefas_frame, text=f"{tarefa.nome} - {tarefa.descricao} - Status: {tarefa.status}", bg=bg_color[i%2], fg="black", font=self.fonte_times_new_roman)
            descricao_label.grid(row=i, column=0, columnspan=2, sticky="w", padx=10, pady=5)
            concluido_checkbox = tk.Checkbutton(self.tarefas_frame, text="Concluído", command=lambda idx=i-1: self.marcar_concluido(idx))
            concluido_checkbox.select() if tarefa.status == "Concluído" else concluido_checkbox.deselect()
            concluido_checkbox.grid(row=i, column=2, padx=5, pady=5)
            if tarefa.status == "Concluído":
                descricao_label.config(bg="lightgreen", font=self.fonte_times_new_roman)

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.descricao_entry.delete(0, tk.END)
        self.inicio_entry.delete(0, tk.END)
        self.fim_entry.delete(0, tk.END)
        self.status_var.set("A Fazer")

    def remover_tarefas_concluidas(self):
        tarefas_restantes = [tarefa for tarefa in self.tarefas if tarefa.status != "Concluído"]
        tarefas_removidas = [tarefa for tarefa in self.tarefas if tarefa.status == "Concluído"]
        self.tarefas = tarefas_restantes
        self.db_manager.remover_tarefas_concluidas()
        self.mostrar_tarefas()
        if tarefas_removidas:
            messagebox.showinfo("Tarefas Removidas", "Tarefas concluídas removidas com sucesso.")

    def marcar_concluido(self, idx):
        if self.tarefas[idx].status == "Concluído":
            self.tarefas[idx].status = "A Fazer"
        else:
            self.tarefas[idx].status = "Concluído"
    
        # Atualizar o status da tarefa no banco de dados
        self.db_manager.atualizar_status_tarefa(self.tarefas[idx].nome, self.tarefas[idx].status)
        
        # Chamar a função mostrar_tarefas() para refletir a mudança na interface
        self.mostrar_tarefas()
