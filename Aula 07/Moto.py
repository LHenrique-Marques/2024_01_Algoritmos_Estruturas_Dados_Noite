from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, ano,cilindradas):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas
    
    def imprimir(self):
        super().imprimir()
        print(f"              Quantidade de Portas: {self.cilindradas}")
    
    def ligar(self,chave):
        if chave == "1234":
            print("Moto ligada.")
        else:
            print("Não foi possivel ligar a moto.")
    