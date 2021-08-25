import datetime as dt

class Cliente(object):
    def __init__(self, qtdBikes, tipoLocacao, horaLocacao):
        self.qtdBikes = qtdBikes
        self.tipoLocacao = tipoLocacao
        self.horaLocacao = horaLocacao
    
    # visulizar as bicicletas disponíveis no Estoque da Loja
    def mostrarEstoque(self):
        return print(f"Estoque disponível: {Loja.estoque} bicicletas")

    # alugar bicicletas, conforme a quantidade e modalidades a serem escolhidas
    def alugarBike(self, qtdBikes, tipoLocacao):
        qtdBikes = input("Quantas bicicletas você quer alugar? ")
        try:
            qtdBikes = int(qtdBikes)
        except ValueError:
            print("Quantidade inválida, favor inserir um número inteiro positivo.")
            return -1
        
        if qtdBikes < 1:
            print("Quantidade inválida. A quantidade deve ser maior do que zero.")
            return -1
        else:
            self.qtdBikes = qtdBikes

        tipoLocacao = 0
        while tipoLocacao == 0:
            tipoLocacao = input("Qual o tipo de locação?\n (Digite o número)\n \
                1 - Locação por HORA (R$ 5,00 / hora); \n \
                2 - Locação por DIA (R$ 25,00 / dia); \n \
                3 - Locação por SEMANA (R$ 100,00 / semana).")
            
            try:
                tipoLocacao = int(tipoLocacao)
            except ValueError:
                print("Entrada inválida. Favor digitar um número inteiro positivo.")

            while tipoLocacao not in [1, 2, 3]:
                print("Entrada inválida. Favor digitar 1 para HORA, 2 para DIA ou 3 para SEMANA.")
                tipoLocacao = 0

            if tipoLocacao == 1:
                self.horaLocacao = Loja.locacaoHora(Cliente.qtdBikes)
            elif tipoLocacao == 2:
                self.horaLocacao = Loja.locacaoDia(Cliente.qtdBikes)
            else:
                self.horaLocacao = Loja.locacaoDia(Cliente.qtdBikes)

            return self.qtdBikes, self.tipoLocacao, self.horaLocacao

class Loja(object):
    def __init__(self, estoque):
        self.estoque = estoque
  
    def mostrarEstoque(self):
        pass

    def locacaoHora(self, qtdBikes):
        pass

    def locacaoDia(self, qtdBikes):
        pass

    def locacaoSemana(self, qtdBikes):
        pass

    def locacaoFamilia(self, qtdBikes):
        pass




