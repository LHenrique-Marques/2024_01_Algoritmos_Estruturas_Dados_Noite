class Categoria():
    def __init__(self,id = 0,nome = "Não Definido"):
        self.id = id
        self.nome = nome
    
    def __str__(self):
        return f"""
        Nome: {self.nome}
        """