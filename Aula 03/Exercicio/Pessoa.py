from Cidade import Cidade
class Pessoa:
    def __init__(self,nome = "Não informado",idade = 0,cid = Cidade()):
        self.nome = nome
        self.idade = idade
        self.cidade = cid
        print(f"Pessoa {self.nome}, construida.")

    def __str__(self):
        return f"""
        Nome : {self.nome}
        Idade : {self.idade}
        {self.cidade}
        """