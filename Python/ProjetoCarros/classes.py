import sqlite3

# classe para representar um carro
class Carro:
    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa

# conectar ao banco de dados
def conectar_banco():
    conexao = sqlite3.connect('carros.db')
    cursor = conexao.cursor()
    return conexao, cursor

# criar a tabela de carros no banco de dados
def criar_tabela():
    conexao, cursor = conectar_banco()
    cursor.execute('''CREATE TABLE IF NOT EXISTS carros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        marca TEXT NOT NULL,
                        modelo TEXT NOT NULL,
                        ano INTEGER NOT NULL,
                        cor TEXT NOT NULL,
                        placa TEXT NOT NULL UNIQUE)''')
    conexao.commit()
    conexao.close()

# cadastrar um novo carro
def cadastrar_carro(carro):
    conexao, cursor = conectar_banco()
    cursor.execute('''INSERT INTO carros (marca, modelo, ano, cor, placa)
                      VALUES (?, ?, ?, ?, ?)''', (carro.marca, carro.modelo, carro.ano, carro.cor, carro.placa))
    conexao.commit()
    conexao.close()

# remover carro pelo ID
def remover_carro(id_carro):
    conexao, cursor = conectar_banco()
    cursor.execute('''DELETE FROM carros WHERE id = ?''', (id_carro,))
    conexao.commit()
    conexao.close()

# listar carros
def listar_carros():
    conexao, cursor = conectar_banco()
    cursor.execute('''SELECT * FROM carros''')
    carros = cursor.fetchall()
    conexao.close()
    return carros

# pesquisar um carro por placa
def pesquisar_carro(placa):
    conexao, cursor = conectar_banco()
    cursor.execute('''SELECT * FROM carros WHERE placa = ?''', (placa,))
    carro = cursor.fetchone()
    conexao.close()
    return carro

# modificar informações de um carro
def modificar_carro(id_carro, novo_carro):
    conexao, cursor = conectar_banco()
    cursor.execute('''UPDATE carros SET marca = ?, modelo = ?, ano = ?, cor = ?, placa = ?
                      WHERE id = ?''', (novo_carro.marca, novo_carro.modelo, novo_carro.ano, 
                                        novo_carro.cor, novo_carro.placa, id_carro))
    conexao.commit()
    conexao.close()
