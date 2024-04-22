from abc import ABC,abstractmethod
class Computador(ABC):
    def __init__(self,modelo,cor,preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        
    def get_infos(self):
        return f""""
    Modelo : {self.modelo}
    Cor : {self.cor}
    Preço : {self.preco}
    """
    
    @abstractmethod
    def cadastrar(self):
        print(f"{Produto} cadastrado com sucesso.")
        

class Desktop(Computador):
    def __init__(self,modelo,cor,preco,potenciaFonte):
        super().__init__(modelo,cor,preco)
        self._potenciaFonte = potenciaFonte
        
    def get_infos(self):
        return super().get_infos() + f"Potencia da Fonte : {self._potenciaFonte}"
    
    def cadastrar(self):
        Produto = "Desktop"
        super().cadastrar()

class Notebook(Computador):
    def __init__(self, modelo, cor, preco,tempoBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoBateria = tempoBateria
    
    def get_infos(self):
        return super().get_infos() + self.__tempoBateria
    
    def cadastrar(self):
        Produto = "Notebook"
        return super().cadastrar()