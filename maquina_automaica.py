class Maquina_Vendas():
    def __init__(self):
        print('iniciando uma maquina automatica de vender frango')

        self.list_produtos = []

    def reabastecer_maquina(self, produto):
        self.list_produtos.append(produto)

    def comprar_produtos(self):
        print("comprei um " +
              self.list_produtos[len(self.list_produtos)-1].nome_produto())
        del self.list_produtos[len(self.list_produtos)-1]


        
        

class Produto():
    def __init__(self):
        print('criei um frango assado')
        self.name_produto = "frango assado"
    def nome_produto(self):
        return self.name_produto

maquina = Maquina_Vendas()


p1 = Produto()
p2 = Produto()



maquina.reabastecer_maquina(p1)
maquina.reabastecer_maquina(p2)

maquina.comprar_produtos()




