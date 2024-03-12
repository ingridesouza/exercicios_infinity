# database.py
import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="876@ni2!a",
            database="gerenciadorTarefas"
        )
        self.cursor = self.conexao.cursor()

    def salvar_tarefa(self, tarefa):
        query = "INSERT INTO tarefas (nome, descricao, inicio, fim, status) VALUES (%s, %s, %s, %s, %s)"
        valores = (tarefa.nome, tarefa.descricao, tarefa.inicio, tarefa.fim, tarefa.status)
        self.cursor.execute(query, valores)
        self.conexao.commit()

    def remover_tarefas_concluidas(self):
        query = "DELETE FROM tarefas WHERE status = 'Concluído'"
        self.cursor.execute(query)
        self.conexao.commit()

    def atualizar_status_tarefa(self, nome, novo_status):
        query = "UPDATE tarefas SET status = %s WHERE nome = %s"
        valores = (novo_status, nome)
        self.cursor.execute(query, valores)
        self.conexao.commit()
