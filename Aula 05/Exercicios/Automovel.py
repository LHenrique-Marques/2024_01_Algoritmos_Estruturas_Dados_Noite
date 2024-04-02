from Veiculo import Veiculo
class Automovel(Veiculo):
    def __init__(self,marca,qtdrodas,modelo,velocidade,potenciaDoMotor):
        super().__init__(marca,qtdrodas,modelo,velocidade)
        self.potenciaDoMotor = potenciaDoMotor