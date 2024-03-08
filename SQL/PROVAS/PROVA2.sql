CREATE TABLE IF NOT EXISTS Pessoa (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeCompleto VARCHAR(100),
    Idade INT,
    Genero VARCHAR(20),
    Nacionalidade VARCHAR(50),
    Email VARCHAR(100),
    EstadoCivil VARCHAR(20),
    NomePai VARCHAR(100),
    NomeMae VARCHAR(100)
);

INSERT INTO Pessoa (NomeCompleto, Idade, Genero, Nacionalidade, Email, EstadoCivil, NomePai, NomeMae) VALUES
('Ingride de Souza Lima', 18, 'Feminino', 'Brasileira', 'ingride@email.com', 'Solteira', 'Josenilson Santiago', 'Renata de Cássia'),
('Renata de Cássia', 37, 'Feminino', 'Brasileira', 'renata@email.com', 'Casada', 'Renato Sampaio', 'Lucinneide Santana'),
('Lucinneide Santana', 56, 'Feminino', 'Brasileira', 'lucineide@email.com', 'Casada', 'Jose Santana', 'Ana Santos');

SELECT * FROM Pessoa;

UPDATE Pessoa
SET NomeCompleto = 'Cosme' ,Idade = 19, EstadoCivil = 'Casado', Email = 'cosme@email.com'
WHERE ID = 1;

SELECT * FROM Pessoa;

DELETE FROM Pessoa WHERE ID = 1;

SELECT * FROM Pessoa;
