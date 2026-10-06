from dataclasses import dataclass 

@dataclass()
class Produtos: 
    id: int 
    nome : str 
    preco: float 
    estoque: int 

    def aumentar_estoque(self, numero_aumentar: int):
        self.estoque : int = self.estoque + numero_aumentar 