from Categoria import Categoria

class Produto():
    def __init__(self,id = 0,nome = "Não Definido",preco = 0,qtd = 0,categ = Categoria()):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.categ = categ
    
    def __str__(self):
        return f"""
        Nome: {self.nome}
        Preco: {self.preco}
        Quantidade: {self.qtd}
        Categoria: {self.categ}
        """