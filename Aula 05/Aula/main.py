from Categoria import Categoria
from veiculo import Veiculo
from Carro import Carro
from moto import Moto

cat1 = Categoria("SUV")
cat2 = Categoria("Estradeiras")
cat3 = Categoria("Calma calabreso")

v1 = Veiculo(cat = cat3)
v1.imprimir()

print("---------------------------")
c1 = Carro("Jeep", 2021,cat1,4)
c1.imprimir()

print("---------------------------")
m1 = Moto("BMW",2020,cat2,500)
m1.imprimir()