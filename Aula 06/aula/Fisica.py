from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone,cpf,idade,peso,altura):
        super().__init__(codigo, nome, endereco, telefone)
        self.cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def imprime_cpf(self):
        print(f"CPF : {self.cpf}")
    
    def calcula_imc(self):
        return self.peso + (self.altura * self.altura)