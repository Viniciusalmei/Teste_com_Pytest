from main import Produtos

def teste_construtor(): 
    produto_teste = Produtos(1,"Teste",20, 30)

    assert produto_teste.id == 1
    assert produto_teste.nome == "Teste"
    assert produto_teste.preco == 20
    assert produto_teste.estoque == 30


def teste_funcao():
    produto_teste = Produtos(1,"Teste",20, 30)
    produto_teste.aumentar_estoque(20)

    assert produto_teste.estoque == 50