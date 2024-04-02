from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdrodas, modelo, velocidade, potenciaDoMotor,partidaEletrica):
        super().__init__(marca, qtdrodas, modelo, velocidade, potenciaDoMotor)
        self.partidaEletrica = partidaEletrica