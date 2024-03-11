import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Tarefa:
    def __init__(self, nome, descricao, inicio, fim, status):
        self.nome = nome
        self.descricao = descricao
        self.inicio = inicio
        self.fim = fim
        self.status = status

class GerenciadorTarefasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Tarefas")
        self.master.configure(bg="white")
        
        self.stark_label = tk.Label(master, text="Stark Corporation", bg="black", fg="white")
        self.stark_label.grid(row=0, columnspan=3, pady=10)

        self.tarefas = []

        self.nome_label = tk.Label(master, text="Nome:", bg="white", fg="black")
        self.nome_label.grid(row=1, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(master, width=50)
        self.nome_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        self.descricao_label = tk.Label(master, text="Descrição:", bg="white", fg="black")
        self.descricao_label.grid(row=2, column=0, padx=5, pady=5)
        self.descricao_entry = tk.Entry(master, width=50)
        self.descricao_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        self.inicio_label = tk.Label(master, text="Data de Início (DD-MM-YYYY):", bg="white", fg="black")
        self.inicio_label.grid(row=3, column=0, padx=5, pady=5)
        self.inicio_entry = tk.Entry(master, width=20)
        self.inicio_entry.grid(row=3, column=1, padx=5, pady=5)

        self.fim_label = tk.Label(master, text="Data de Término (DD-MM-YYYY):", bg="white", fg="black")
        self.fim_label.grid(row=4, column=0, padx=5, pady=5)
        self.fim_entry = tk.Entry(master, width=20)
        self.fim_entry.grid(row=4, column=1, padx=5, pady=5)

        self.status_label = tk.Label(master, text="Status:", bg="white", fg="black")
        self.status_label.grid(row=5, column=0, padx=5, pady=5)
        self.status_var = tk.StringVar(master)
        self.status_var.set("A Fazer")
        self.status_menu = tk.OptionMenu(master, self.status_var, "A Fazer", "Em Andamento", "Concluído")
        self.status_menu.grid(row=5, column=1, padx=5, pady=5)

        self.adicionar_button = tk.Button(master, text="Adicionar Tarefa", command=self.adicionar_tarefa, bg="red", fg="white")
        self.adicionar_button.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

        self.remover_button = tk.Button(master, text="Remover Tarefas Concluídas", command=self.remover_tarefas_concluidas, bg="red", fg="white")
        self.remover_button.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        self.tarefas_frame = tk.Frame(master, bg="white")
        self.tarefas_frame.grid(row=8, column=0, columnspan=3, padx=5, pady=5)
        self.mostrar_tarefas()

        # Conectar ao banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="876@ni2!a",
            database="gerenciadorTarefas"
        )
        self.cursor = self.conexao.cursor()

    def adicionar_tarefa(self):
        nome = self.nome_entry.get()
        descricao = self.descricao_entry.get()
        inicio = self.inicio_entry.get()
        fim = self.fim_entry.get()
        status = self.status_var.get()
        
        # Verificar se as datas são válidas antes de salvar no banco de dados
        if self.validar_data(inicio) and self.validar_data(fim):
            tarefa = Tarefa(nome, descricao, inicio, fim, status)
            self.tarefas.append(tarefa)
            self.salvar_tarefa_no_bd(tarefa)
            self.mostrar_tarefas()
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Data inválida. Use o formato DD-MM-YYYY.")

    def validar_data(self, data):
        try:
            # Verifica se a data pode ser convertida para o formato 'DD-MM-YYYY'
            parts = data.split("-")
            if len(parts) != 3:
                return False
            day, month, year = map(int, parts)
            return 1 <= day <= 31 and 1 <= month <= 12 and 1000 <= year <= 9999
        except ValueError:
            return False

    def mostrar_tarefas(self):
        for widget in self.tarefas_frame.winfo_children():
            widget.destroy()

        bg_color = ["white", "lightgrey"]
        for i, tarefa in enumerate(self.tarefas, start=1):
            descricao_label = tk.Label(self.tarefas_frame, text=f"{tarefa.nome} - {tarefa.descricao} - Status: {tarefa.status}", bg=bg_color[i%2], fg="black")
            descricao_label.grid(row=i, column=0, columnspan=2, sticky="w", padx=10, pady=5)
            concluido_checkbox = tk.Checkbutton(self.tarefas_frame, text="Concluído", command=lambda idx=i-1: self.marcar_concluido(idx))
            concluido_checkbox.select() if tarefa.status == "Concluído" else concluido_checkbox.deselect()
            concluido_checkbox.grid(row=i, column=2, padx=5, pady=5)
            if tarefa.status == "Concluído":
                descricao_label.config(bg="lightgreen")

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
        self.remover_tarefas_concluidas_do_bd()
        self.mostrar_tarefas()
        if tarefas_removidas:
            messagebox.showinfo("Tarefas Removidas", "Tarefas concluídas removidas com sucesso.")

    def marcar_concluido(self, idx):
        if self.tarefas[idx].status == "Concluído":
            self.tarefas[idx].status = "A Fazer"
        else:
            self.tarefas[idx].status = "Concluído"
        self.atualizar_status_no_bd(idx)

    def salvar_tarefa_no_bd(self, tarefa):
        query = "INSERT INTO tarefas (nome, descricao, inicio, fim, status) VALUES (%s, %s, %s, %s, %s)"
        valores = (tarefa.nome, tarefa.descricao, tarefa.inicio, tarefa.fim, tarefa.status)
        self.cursor.execute(query, valores)
        self.conexao.commit()

    def remover_tarefas_concluidas_do_bd(self):
        query = "DELETE FROM tarefas WHERE status = 'Concluído'"
        self.cursor.execute(query)
        self.conexao.commit()

    def atualizar_status_no_bd(self, idx):
        query = "UPDATE tarefas SET status = %s WHERE nome = %s"
        novo_status = self.tarefas[idx].status
        nome_tarefa = self.tarefas[idx].nome
        valores = (novo_status, nome_tarefa)
        self.cursor.execute(query, valores)
        self.conexao.commit()

def main():
    root = tk.Tk()
    app = GerenciadorTarefasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
