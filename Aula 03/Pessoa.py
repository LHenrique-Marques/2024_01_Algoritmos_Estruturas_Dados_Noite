from Cidade import Cidade
class Pessoa:
    def __init__(self,nome,idade=18,cid = Cidade("Tangamandápio")):
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

henrique = Pessoa("Henrique",21,Cidade("Porto Alegre",51))
print(henrique)