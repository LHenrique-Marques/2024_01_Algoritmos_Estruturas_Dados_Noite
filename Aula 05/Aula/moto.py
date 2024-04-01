from veiculo import Veiculo
class Moto(Veiculo):
    def __init__(self, marca,ano,cat,cilindradas):
        super().__init__(marca, ano, cat)
        self.cilindradas = cilindradas
        
    def __str__(self):
        return super().__str__() + f"""\nCilindradas: {self.cilindradas} \n"""
    
    def imprimir(self):
        print(self)