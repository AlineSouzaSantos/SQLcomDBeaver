import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('DB')
cursor = conn.cursor()

cursor.execute('')

#envio de comandos SQL
conn.commit()
conn.close()