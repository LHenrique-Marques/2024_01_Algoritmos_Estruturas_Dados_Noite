class Aluno():
    def __init__(self,codigo,nome,matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
    def __str__(self):
        return f"""
            Nome: {self.nome}
            Código: {self.codigo}
            Matricula: {self.matricula}"""

    def imprimir(self):
        print(self)


class Aluno_Ensino_Médio(Aluno):
    def __init__(self,codigo,nome,matricula,ano):
        super().__init__(codigo,nome,matricula)
        self.ano = ano

    def __str__(self):
        return f"""{super().__str__()} \n            Ano: {self.ano}"""
    
class Aluno_Graduacao(Aluno):
    def __init__(self,codigo,nome,matricula,semestre):
        super().__init__(codigo,nome,matricula)
        self.semestre = semestre
    
    def __str__(self):
        return f"""{super().__str__()} \n            Semestre:{self.semestre}"""
        

teste = Aluno_Ensino_Médio(0,"Henrique",23,14)
teste2 = Aluno_Graduacao(1,"Renan",0,2)
teste.imprimir()
teste2.imprimir()