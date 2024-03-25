def menu_principal():
    while True:
        print(f"""
    ----------Menu--------
    0 - Fechar o programa
    1 - Pessoa
    2 - Cidade
    3 - Pedido
    4 - Produto
    5 - Categoria
""")
        escolha = int(input("Escolha: "))
        if escolha == 0:
            break
        elif escolha == 1:
            menu_pessoa()
        elif escolha == 2:
            pass
        elif escolha == 3:
            pass
        elif escolha == 4:
            pass
        elif escolha == 5:
            pass

def menu_pessoa():
    while True:
        print("""
          ------Menu da Pessoa-----
          0 - Voltar
          1 - Criar Pessoa
          2 - Remover Pessoa
          3 - Alterar Pessoa
          """)
        escolha = int(input("Escolha: "))
        
        if escolha == 0:
            break
        
        elif escolha == 1:
            pass
        
        elif escolha == 2:
            pass
        
        elif escolha == 3:
            pass

def menu_cidade():
    while True:
        print(f"""
              -----Menu Cidade------
              0 - Voltar
              1 - Adiciona Cidade
              2 - Remove Cidade
              3 - Altera Cidade
              
              
              """)