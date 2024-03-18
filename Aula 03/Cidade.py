class Cidade:
    def __init__(self,id = 52,nome = "Viamão"):
        self.id = id
        self.nome = nome
        print(f"Cidade {self.nome} construida.")

    
    def __str__(self):
        return f"""
        Cidade: {self.nome}
        Cidade ID : {self.id}
        """