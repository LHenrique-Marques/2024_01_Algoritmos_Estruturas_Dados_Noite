produtos = ["camiseta","regata","bermuda"]
preco = [10,20,30]
qtd = [2,4,6]


def deletar_produto(x):
    del produtos[x]
    del preco[x]
    del qtd[x]
    
def mostra_itens():
    for prod in range(len(produtos)):        
        print(f"Produto [{prod}]: {produtos[prod]} Preço:{preco[prod]} Quantidade: {qtd[prod]}")


mostra_itens() 

teste = int(input("Digite o indice do produto que deseja deletar:"))

deletar_produto(teste)

mostra_itens()
    
