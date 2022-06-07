import sqlite3

db = sqlite3.connect('database.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS funcionario (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            nome TEXT,
            cargo TEXT,
            cpf INTEGER,
            entrada TEXT,
            idade INTEGER)""")

db.commit()

db.close()