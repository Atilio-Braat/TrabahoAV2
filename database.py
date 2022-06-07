import sqlite3

db = sqlite3.connect('database.db')

c = db.cursor()

c.execute("""create table if not exists funcionario (
            id integer primary key autoincrement ,
            nome text,
            cargo text,
            cep text,
            entrada date,
            idade integer)""")

db.commit()

db.close()