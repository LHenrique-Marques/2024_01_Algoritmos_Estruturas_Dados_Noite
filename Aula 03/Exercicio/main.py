from Pessoa import Pessoa
from Cidade import Cidade
from Pedido import Pedido
from Produto import Produto
from Categoria import Categoria

cidade1 = Cidade(52,"Viamão")
pessoa1 = Pessoa("Henrique",21,cidade1)
pedido1 = Pedido(1,"Estrd Caminho do Meio,4772",pessoa1)
catego1 = Categoria(1,"Bebidas")
produto1 = Produto(1,"Coca-Cola",10,1,catego1)

