class Categoria():
    def __init__(self,id = 0,nome = "Outro"):
        self.id = id
        self.nome = nome
    
    def __str__(self):
        return f"""
        Categoria: {self.nome}
        """