import tkinter as tk
import sqlite3
import random

class JogoRPG:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo RPG")
        
        # Conectar ao banco de dados
        self.conn = sqlite3.connect("personagens.db")
        self.c = self.conn.cursor()
        self.criar_tabela()
        
        self.criar_widgets()
        self.carregar_personagens()
    
    def criar_tabela(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS personagens (
                            id INTEGER PRIMARY KEY,
                            nome TEXT,
                            classe TEXT,
                            nivel INTEGER,
                            hp INTEGER
                          )""")
        self.conn.commit()
    
    def criar_widgets(self):
        self.label = tk.Label(self.master, text="Jogo RPG")
        self.label.pack()
        
        self.botao_criar_personagem = tk.Button(self.master, text="Criar Personagem", command=self.criar_personagem)
        self.botao_criar_personagem.pack()
        
        self.botao_batalha = tk.Button(self.master, text="Batalha", command=self.batalha)
        self.botao_batalha.pack()
        
        self.info_personagem_texto = tk.Text(self.master, height=10, width=50)
        self.info_personagem_texto.pack()
        
    def criar_personagem(self):
        nome = input("Digite o nome do personagem: ")
        classe = input("Digite a classe do personagem: ")
        nivel = random.randint(1, 10)
        hp = random.randint(50, 100)
        
        self.c.execute("INSERT INTO personagens (nome, classe, nivel, hp) VALUES (?, ?, ?, ?)", (nome, classe, nivel, hp))
        self.conn.commit()
        
        self.info_personagem_texto.insert(tk.END, f"Personagem {nome} criado!\n")
        self.info_personagem_texto.insert(tk.END, f"Classe: {classe}, Nível: {nivel}, HP: {hp}\n")
        self.info_personagem_texto.see(tk.END)
    
    def carregar_personagens(self):
        self.c.execute("SELECT * FROM personagens")
        personagens = self.c.fetchall()
        for personagem in personagens:
            self.info_personagem_texto.insert(tk.END, f"Personagem Carregado: {personagem}\n")
        self.info_personagem_texto.insert(tk.END, "Personagens carregados!\n")
        self.info_personagem_texto.see(tk.END)
        
    def batalha(self):
        # Simular uma batalha
        self.info_personagem_texto.insert(tk.END, "Batalha iniciada!\n")
        self.info_personagem_texto.see(tk.END)

root = tk.Tk()
jogo = JogoRPG(root)        

root.mainloop() 