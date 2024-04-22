from classes import Desktop, Notebook

d1 = Desktop("GTX","Branco","25.50","1000z")
d2 = Desktop("G3x","Vermelho","10.50","1500z")
n1 = Notebook("Asus","Azul","99.00","1h")
n2 = Notebook("Apple","Verde","199.00","10h")

print(d1.get_infos())
print(d2.get_infos())
print(n1.get_infos())
print(n2.get_infos())