
import sqlite3

# Conectar ao banco db
conn = sqlite3.connect('sqlite3db.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela para armazenar os dados de nome e idade
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados (
        nome TEXT,
        idade INTEGER
    )
''')

# Função para inserir um novo dado no banco de dados
def gravar_dado(nome, idade):
    cursor.execute('''
        INSERT INTO dados (nome, idade)
        VALUES (?, ?)
    ''', (nome, idade))
    conn.commit()
gravar_dado('Carlos', 21)
# Função para recuperar todos os dados do banco de dados
def obter_dados():
    cursor.execute('''
        SELECT * FROM dados
    ''')
    return cursor.fetchall()

