class Cidade():
    def __init__(self,id,nome):
        self.id = int(id)
        self.nome = str(nome)



class Pessoa():
    def __init__(self):
        self.id = int()
        self.nome = str()
        self.idade = int()
        self.cidade = Cidade(12345,"Porto Alegre")