from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdrodas, modelo, velocidade,numMarchas,bagageiro):
        super().__init__(marca, qtdrodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro
    