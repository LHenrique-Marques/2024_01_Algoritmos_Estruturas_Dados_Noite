from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, ano,qtdportas):
        super().__init__(modelo, ano)
        self.qtdportas = qtdportas
    
    def imprimir(self):
        super().imprimir()
        print(f"              Quantidade de Portas: {self.qtdportas}")
    
    def ligar(self,chave):
        if chave == "1234":
            print("Carro ligado.")
        else:
            print("Não foi possivel ligar o carro.")
    