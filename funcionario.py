import sqlite3

class Funcionario(object):

    def init(self, id = 0, nome = "", cargo = "", cpf = "", entrada = "", idade = 0):
        self.info = {}
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.cpf = cpf
        self.entrada = entrada
        self.idade = idade


    def insertFuncionario(self):

        db = sqlite3.connect('database.db')

        c = db.cursor()


        query = """
        INSERT INTO funcionario (nome, cargo, cpf,
        entrada, idade) VALUES ('%s', '%s', %d, '%s', %d)
        """ % (self.nome,self.cargo,int(self.cpf),self.entrada,int(self.idade))
        c.execute(query)

        db.commit()
        c.close()

    def deletarFuncionario(self):
        db = sqlite3.connect('database.db')

        c = db.cursor()
        
        c.execute("""
        DELETE FROM funcionario 
        WHERE id = %d
        """.format(self.id))
        c.close()
    
    def buscarFuncionario(self):
        db = sqlite3.connect('database.db')

        c = db.cursor()
        query = c.execute("""
        SELECT 
            id,
            nome,
            idade,
            cargo,
            cpf,
            entrada
        """.format(self.id))
        c.close()

        return query

    
