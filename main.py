import datetime as dt

class Cliente(object):
    def __init__(self, nome, cpf, calculadoraTempo, carteira):
        self.nome = nome
        self.cpf = cpf
        self.calculadoraTempo = calculadoraTempo
        self.carteira = carteira
        self.conta = 0.0


class Loja(object):
    def __init__(self, estoque, pedido, calculadoraTempo, caixa):
        self.estoque = estoque
        self.pedido = pedido
        self.calculadoraTempo = calculadoraTempo
        self.caixa = caixa
        
