from Categoria import Categoria

class Veiculo:
    def __init__(self,marca = "Honda", ano = 2014, cat = Categoria(None)):
        self.id = None
        self.marca = marca
        self.ano = ano
        self.cat = cat
    
    def __str__(self):
        return f"""Marca: {self.marca}
Ano: {self.ano}
Categoria: {self.cat.nome}"""
    
    def imprimir(self):
        print(self)