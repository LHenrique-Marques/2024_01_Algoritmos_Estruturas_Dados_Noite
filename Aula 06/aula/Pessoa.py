class Pessoa():
    def __init__(self,codigo,nome,endereco,telefone):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
    
    def imprime(self):
        print(f""""
    Código: {self.codigo}
    Nome: {self.nome}
    Endereço: {self.endereco}
    Telefone: {self.telefone}
    """)
    
    def imprime_telefone(self):
        print(f"Telefone: {self.telefone}")
    
        