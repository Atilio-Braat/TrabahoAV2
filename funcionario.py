import sqlite3

class Funsionario(object):

    def init(self, id = 0, nome = "", cargo = "", cep = "", entrada = "", idade = 0):
        self.info = {}
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.cep = cep
        self.entrada = entrada
        self.idade = idade


    def insertUser(self):

        db = sqlite3.connect('database.db')

        c = db.cursor()
        try:

            c.execute("""
            INSERT INTO funcionario (nome, cargo, cep,
            entrada, idade) VALUES (%s, %s, %d, %s, %s)
            """.format(self.nome,self.cargo,self.cep,self.entrada,self.idade))

            db.commit()
            c.close()

            return "Funcionário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do funcionário"

    def deleteUser(self):
        db = sqlite3.connect('database.db')

        c = db.cursor()
        
        try:
            c.execute("""
            DELETE FROM funcionario 
            WHERE id = %d
            """.format(self.id))

            return "Funcionário deletado"
        except:
            return "Ocorreu um erro ao deletar"
    
    def buscarFuncionario(self):
        db = sqlite3.connect('database.db')

        c = db.cursor()
        try:
            c.execute("""
            SELECT 
                id,
                nome,
                idade,
                cargo,
                cep,
                entrada
            WHERE id = %d
            """.format(self.id))

            return "Busca feita com sucesso"
        except:
            return "Ocorreu um erro na busca"

    
