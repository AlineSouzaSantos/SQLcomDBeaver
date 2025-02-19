import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('DB')
cursor = conn.cursor()

#Criando tabela
#Para criar outra tabela, basta repetir o comando abaixo, comentando o anterior
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100),endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100),endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100),endereco VARCHAR(100), email VARCHAR(100));')

#Alterando tabela
#Para adicionar mais de uma coluna, basta repetir o comando abaixo, comentando o anterior
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario;')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT;')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone;')

#Inserindo dados
#Para adicionar mais de um dado, basta repetir o comando abaixo, comentando o anterior
#cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (1, "João", "Rua 1","joao@gmail.com");')
#cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (2, "Maria", "Rua 2","maria@gmail.com");')
#cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (3, "Jose", "Rua 3","jose@gmail.com");')
#cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (4, "Marcia", "Rua 4","marcia@gmail.com");')
#cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (8, "Kelly", "Rua 5","kelly@gmail.com");')

#Excluindo Dados
#cursor.execute('DELETE FROM usuario WHERE id = 1;')

#Atualizando Dados
#cursor.execute('UPDATE usuario SET endereco = "Minas Gerais" WHERE id = 1;')

#Excluindo tabela
#cursor.execute('DROP TABLE produtos;')

#Comando SELECT com clausulas
#Seleciona tudo da tabela usuario e verificando os resultados no python
#visualizar = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC;')
#visualizar = cursor.execute('SELECT * FROM usuario LIMIT 3;')
#visualizar = cursor.execute('SELECT DISTINCT * FROM usuario;')

#GROUP BY e HAVING
#visualizar = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3;')

#JOIN - retorna informações de duas tabelas
#INNER JOIN
#Preenche as informações das duas tabelas, somente se houver correspondência
#visualizar = cursor.execute('SELECT gerentes.nome, usuario.nome FROM gerentes INNER JOIN usuario ON gerentes.id = usuario.id;')

#LEFT JOIN
#Preenche as informações da tabela da esquerda, mesmo que não tenha correspondência na tabela da direita
#visualizar = cursor.execute('SELECT * FROM gerentes LEFT JOIN usuario ON gerentes.id = usuario.id;')

#RIGHT JOIN
#Preenche as informações da tabela da direita, mesmo que não tenha correspondência na tabela da esquerda
#visualizar = cursor.execute('SELECT * FROM gerentes RIGHT JOIN usuario ON gerentes.id = usuario.id;')

#FULL JOIN
#Preenche as informações das duas tabelas, mesmo que não haja correspondência
#visualizar = cursor.execute('SELECT * FROM gerentes FULL JOIN usuario ON gerentes.id = usuario.id;')

#Sub-queries
#Consultas dentro de consultas
visualizar = cursor.execute('SELECT * FROM usuario WHERE id IN (SELECT id FROM gerentes);')
for usuario in visualizar:
    print(usuario)



#envio de comandos SQL
conn.commit()
conn.close()