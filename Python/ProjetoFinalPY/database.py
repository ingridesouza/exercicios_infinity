import mysql.connector

class DatabaseManager:
    def __init__(self):
        # Conecta ao banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host="localhost",        # Endereço do servidor MySQL
            user="root",             # Nome de usuário
            password="876@ni2!a",    # Senha do banco de dados
            database="gerenciadorTarefas"  # Nome do banco de dados
        )
        self.cursor = self.conexao.cursor()

    def criar_tabela_tarefas(self):
        query = """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            descricao TEXT,
            inicio DATETIME,
            fim DATETIME,
            status VARCHAR(50)
        )
        """
        self.cursor.execute(query)
        self.conexao.commit()

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
