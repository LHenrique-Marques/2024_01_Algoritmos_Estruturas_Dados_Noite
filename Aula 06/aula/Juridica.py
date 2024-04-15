from Pessoa import Pessoa
class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone,cnpj,inscricao,qtfuncionarios):
        super().__init__(codigo, nome, endereco, telefone)
        self.cnpj = cnpj
        self.inscricao = inscricao
        self.qtfuncionarios = qtfuncionarios
    
    def imprime_cnpj(self):
        print(f"CNPJ: {self.cnpj}")
        
    def emitir_nota(self):
        print("Nota Fiscal")