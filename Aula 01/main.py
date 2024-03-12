# método que não rece e parametro
# e não tem retorno


def imprimeNome():
    print("Nome: Henrique")
    

#método que não recebe parametro
#e tem retorno

def getPi():
    return 3.14

#método que recebe parametro
# e não tem retorno

def imprimirAreaCirculo(raio):
    area = getPi() * (raio * raio)
    print(f"Área do circulo: {area}")
    

# método que recebe parametro
# e tem retorno

def calcularAreaCirculo(raio):
    area = getPi() * (raio * raio)
    return area
    

imprimeNome()
imprimirAreaCirculo(10)