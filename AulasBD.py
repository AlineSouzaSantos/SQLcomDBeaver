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

#Excluindo tabela
cursor.execute('DROP TABLE produtos;')


#envio de comandos SQL
conn.commit()
conn.close()