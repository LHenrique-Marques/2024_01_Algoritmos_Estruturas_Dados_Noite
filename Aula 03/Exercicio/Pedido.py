from Pessoa import Pessoa
class Pedido():
    def __init__(self,id = 0,end = "Não Informado",pessoa = Pessoa()):
        self.id = id
        self.end = end
        self.produtos = []
        self.cliente = pessoa
    
    def __str__(self):   
        x = ""
        for p in self.produtos:
            x += str(p) + "\n"
        return f"""
        Cliente: {self.cliente}
        Endereço: {self.end}
        Produtos: {x}
        """
    def adiciona_produto(self,novo_produto):
        self.produtos.append(novo_produto)
        soma = 0
        for p in self.produtos:
            soma += p.preco
        return soma
    
    def calcula_pedido(self):
        calculo = 0
        for produto in self.produtos:
            calculo = calculo + produto.preco 

        return calculo
