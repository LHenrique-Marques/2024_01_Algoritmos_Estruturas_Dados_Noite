class Cidade:
    def __init__(self,nome = "Não Informado" ,id = None):
        self.id = id
        self.nome = nome

    
    def __str__(self):
        return f"""Cidade: {self.nome}
        Cidade ID : {self.id}
        """