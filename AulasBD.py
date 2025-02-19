import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('DB')
cursor = conn.cursor()

#Criando tabela
#Para criar outra tabela, basta repetir o comando abaixo, comentando o anterior
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100),endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100),endereco VARCHAR(100), email VARCHAR(100));')


#Alterando tabela
#Para adicionar mais de uma coluna, basta repetir o comando abaixo, comentando o anterior
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario;')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT;')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone;')

#Inserindo dados
#Para adicionar mais de um dado, basta repetir o comando abaixo, comentando o anterior
#cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (1, "João", "Rua 1","joao@gmail.com",11123456789);')
#cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (2, "Maria", "Rua 2","maria@gmail.com",11123456789);')
#cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (3, "Jose", "Rua 3","jose@gmail.com",11123456789);')
#cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (4, "Marcia", "Rua 4","marcia@gmail.com",11123456789);')

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
visualizar = cursor.execute('SELECT DISTINCT * FROM usuario;')
for usuario in visualizar:
    print(usuario)

#envio de comandos SQL
conn.commit()
conn.close()