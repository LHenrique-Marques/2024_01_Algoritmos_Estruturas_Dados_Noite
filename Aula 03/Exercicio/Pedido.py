from Pessoa import Pessoa
class Pedido():
    def __init__(self,id = 0,end = "Não Informado",pessoa = Pessoa()):
        self.id = id
        self.end = end
        self.produtos = []
        self.cliente = pessoa
    
    def __str__(self):
        return f"""
        Cliente: {self.cliente}
        Endereço: {self.end}
        Produtos: {self.produtos}
        """
    def adiciona_produto(self,novo_produto):
        self.produtos.append(novo_produto)
    
    def calcula_pedido(self):
        calculo = 0
        for produto in self.produtos:
            calculo = calculo + produto.preco 

        return calculo
