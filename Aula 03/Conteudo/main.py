from Cidade import Cidade
from Pessoa import Pessoa

c1 = Cidade()
c2 = Cidade(nome = "Porto Alegre")
c3 = Cidade(1 , "Capão da Canoa")

# print(c1)
# print(c2)
# print(c3)

p1 = Pessoa("Luis Henrique",21,c2)
p2 = Pessoa("João",20)
p3 = Pessoa("Maria",25,c1)
p4 = Pessoa("Joana",cid = c3)
p5 = Pessoa("Julia",idade = 32)