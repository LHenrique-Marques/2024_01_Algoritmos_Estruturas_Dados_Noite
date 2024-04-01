from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca,ano,cat,qtdPortas):
        super().__init__(marca, ano, cat)
        self.qtdPortas = qtdPortas
        
    def __str__(self):
        return super().__str__() + f"""\nQuantidade de Portas: {self.qtdPortas} \n"""
    
    def imprimir(self):
        print(self)