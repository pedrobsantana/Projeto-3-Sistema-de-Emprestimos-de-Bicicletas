import datetime

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
  
    # mostra o Estoque disponível para locação
    def mostrarEstoque(self):
        print(f"Estoque disponível: {self.estoque} bicicletas")
    
    # aluguel por hora com validação do estoque
    def locacaoHora(self, qtdBikes):
        # número negativo de bicicletas
        if qtdBikes <= 0:
            print("Quantidade inválida, a quantidade deve ser um número inteiro positivo.")
            return None
        # bicicletas solicitadas x estoque atual
        elif qtdBikes > self.estoque:
            print(f"Desculpe, você solicitou {qtdBikes} bicicletas, porém no momento temos apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        # caso o estoque esteja disponível, exibe as informações para o cliente e retorna a hora atual para que depois seja feito o cálculo do valor a ser pago
        else:
            horaLocacao = datetime.datetime.now()
            print(f"Você está alugando {qtdBikes} bicicleta(s), às {horaLocacao} de hoje. O valor para locação por HORA é de R$ 5,00 por hora, por bicicleta.")
            self.estoque -= qtdBikes
            return horaLocacao
    
    # aluguel por dia com validação do estoque
    def locacaoDia(self, qtdBikes):
        # número negativo de bicicletas
        if qtdBikes <= 0:
            print("Quantidade inválida, a quantidade deve ser um número inteiro positivo.")
            return None
        # bicicletas solicitadas x estoque atual
        elif qtdBikes > self.estoque:
            print(f"Desculpe, você solicitou {qtdBikes} bicicletas, porém no momento temos apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        # caso o estoque esteja disponível, exibe as informações para o cliente e retorna a hora atual para que depois seja feito o cálculo do valor a ser pago
        else:
            horaLocacao = datetime.datetime.now()
            print(f"Você está alugando {qtdBikes} bicicleta(s), às {horaLocacao} de hoje. O valor para locação por DIA é de R$ 25,00 por dia, por bicicleta.")
            self.estoque -= qtdBikes
            return horaLocacao

    # aluguel por semana com validação do estoque
    def locacaoSemana(self, qtdBikes):
        # número negativo de bicicletas
        if qtdBikes <= 0:
            print("Quantidade inválida, a quantidade deve ser um número inteiro positivo.")
            return None
        # bicicletas solicitadas x estoque atual
        elif qtdBikes > self.estoque:
            print(f"Desculpe, você solicitou {qtdBikes} bicicletas, porém no momento temos apenas {self.estoque} bicicleta(s) disponível(eis) em estoque.")
            return None
        # caso o estoque esteja disponível, exibe as informações para o cliente e retorna a hora atual para que depois seja feito o cálculo do valor a ser pago
        else:
            horaLocacao = datetime.datetime.now()
            print(f"Você está alugando {qtdBikes} bicicleta(s), às {horaLocacao} de hoje. O valor para locação por SEMANA é de R$ 100,00 por semana, por bicicleta.")
            self.estoque -= qtdBikes
            return horaLocacao

    def locacaoFamilia(self, qtdBikes):
        # Promoção que pode incluir de 3 a 5 empréstimos (de qualquer tipo) com 30% de desconto no valor total
        # verifica se é possível aplicar a promoção, se for possível retorna True e se não for possível, retorna False
        if not (3 <= qtdBikes <= 5):
            print("O desconto da Promoção Família não é aplicável.")
            return False
        else:
            print(f"Você está alugando {qtdBikes} bicicleta(s) e obteve o desconto da 'Promoção Família' em que terá 30% de desconto sobre o valor final da locação.")
            return True

    # calcular a conta na hora da devolução da bicicleta
    def calcularConta(self, alugarBike, locacaoFamilia):
        horaLocacao, tipoLocacao, qtdBikes = alugarBike

        if horaLocacao and tipoLocacao and qtdBikes:
            self.estoque += qtdBikes
            horaAtual = datetime.datetime.now()
            tempoLocacao = horaAtual - horaLocacao

            # se a locação tiver sido por HORA, opção 1
            if tipoLocacao == 1:
                conta = round(tempoLocacao.seconds / 3600) * 5 * qtdBikes

            # se a locação tiver sido por DIA, opção 2
            elif tipoLocacao == 2:
                conta = round(tempoLocacao.days) * 25 * qtdBikes

            # se a locação tiver sido por SEMANA, opção 3
            else:
                conta = round(tempoLocacao.days / 7) * 100 * qtdBikes

            # verificação da promoção do desconto família
            if locacaoFamilia(qtdBikes) == True:
                conta = conta * 0.7
            else:
                locacaoFamilia(qtdBikes)

            # cliente devolve as bicicletas e retorna o valor que ele deve pagar
            print(f"Devolução de bicicletas aceita. O valor total da sua locação é de: R$ {conta}.")
            return conta
        else:
            print("A locação não foi encontrada no sistema.")