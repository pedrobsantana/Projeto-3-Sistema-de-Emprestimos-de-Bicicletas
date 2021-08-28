import datetime
import math

class Cliente(object):
    def __init__(self, qtdBikes, tipoLocacao, horaLocacao):
        self.qtdBikes = qtdBikes
        self.tipoLocacao = tipoLocacao
        self.horaLocacao = horaLocacao

    # visulizar as bicicletas disponíveis no Estoque da Loja
    def mostrarEstoque(self, novaLoja):
        return print(f"Estoque disponível: {novaLoja.estoque} bicicletas")

    # alugar bicicletas, conforme a quantidade e modalidades a serem escolhidas
    def alugarBike(self, qtdBikes, tipoLocacao, novaLoja):
        self.qtdBikes = qtdBikes
        self.tipoLocacao = tipoLocacao

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
            tipoLocacao = input("Qual o tipo de locação? \n \
                1 - Locação por HORA (R$ 5,00 / hora); \n \
                2 - Locação por DIA (R$ 25,00 / dia); \n \
                3 - Locação por SEMANA (R$ 100,00 / semana). \n"
                )
            
            try:
                tipoLocacao = int(tipoLocacao)
            except ValueError:
                print("Entrada inválida. Favor digitar um número inteiro positivo.")

            while tipoLocacao not in [1, 2, 3]:
                print("Entrada inválida. Favor digitar 1 para HORA, 2 para DIA ou 3 para SEMANA.")
                tipoLocacao = 0
                break

            if tipoLocacao == 1:
                self.horaLocacao = novaLoja.locacaoHora(self.qtdBikes, novaLoja)
            elif tipoLocacao == 2:
                self.horaLocacao = novaLoja.locacaoDia(self.qtdBikes, novaLoja)
            else:
                self.horaLocacao = novaLoja.locacaoSemana(self.qtdBikes, novaLoja)
            self.tipoLocacao = tipoLocacao
            return self.qtdBikes, self.tipoLocacao, self.horaLocacao

class Loja(object):
    def __init__(self, estoque):
        self.estoque = estoque
  
    # mostra o Estoque disponível para locação
    def mostrarEstoque(self):
        print(f"Estoque disponível: {self.estoque} bicicletas")
    
    # aluguel por hora com validação do estoque
    def locacaoHora(self, qtdBikes, novoCliente):
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
            print(f"Você está alugando {qtdBikes} bicicleta(s), às {horaLocacao.strftime('%H:%M %d-%m-%Y')}. O valor para locação por HORA é de R$ 5,00 por hora, por bicicleta.")
            self.estoque -= qtdBikes
            return horaLocacao
    
    # aluguel por dia com validação do estoque
    def locacaoDia(self, qtdBikes, novoCliente):
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
            print(f"Você está alugando {qtdBikes} bicicleta(s), às {horaLocacao.strftime('%H:%M %d-%m-%Y')}. O valor para locação por DIA é de R$ 25,00 por dia, por bicicleta.")
            self.estoque -= qtdBikes
            return horaLocacao

    # aluguel por semana com validação do estoque
    def locacaoSemana(self, qtdBikes, novoCliente):
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
            print(f"Você está alugando {qtdBikes} bicicleta(s), às {horaLocacao.strftime('%H:%M %d-%m-%Y')}. O valor para locação por SEMANA é de R$ 100,00 por semana, por bicicleta.")
            self.estoque -= qtdBikes
            return horaLocacao

    def locacaoFamilia(self, qtdBikes, novoCliente):
        # Promoção que pode incluir de 3 a 5 empréstimos (de qualquer tipo) com 30% de desconto no valor total
        # verifica se é possível aplicar a promoção, se for possível retorna True e se não for possível, retorna False
        
        if not (3 <= qtdBikes <= 5):
            print("O desconto da Promoção Família não é aplicável.")
            return False
        else:
            print(f"Você está alugando {qtdBikes} bicicleta(s) e obteve o desconto da 'Promoção Família' em que terá 30% de desconto sobre o valor final da locação.")
            return True

    # calcular a conta na hora da devolução da bicicleta
    def calcularConta(self, objCliente, locacaoFamilia):

        if objCliente.horaLocacao and objCliente.tipoLocacao and objCliente.qtdBikes:
            if self.estoque < 100:
                self.estoque += objCliente.qtdBikes
            else:
                print("Estoque já está cheio")
                pass
            horaAtual = datetime.datetime.now()
            tempoLocacao = horaAtual - objCliente.horaLocacao

            # se a locação tiver sido por HORA, opção 1
            if objCliente.tipoLocacao == 1:
                conta = (math.ceil(tempoLocacao.seconds / 3600) * objCliente.qtdBikes) * 5
                #conta = horas * 5
                #conta = math.ceil((tempoLocacao.seconds / 3600) * 5 * objCliente.qtdBikes)

            # se a locação tiver sido por DIA, opção 2
            elif objCliente.tipoLocacao == 2:
                conta = (math.ceil(tempoLocacao.seconds / 3600 / 24) * objCliente.qtdBikes) * 25
                #dias = math.ceil(tempoLocacao.seconds / 3600 / 24) * objCliente.qtdBikes
                #conta = dias * 25
                #conta = math.ceil((tempoLocacao.days) * 25 * objCliente.qtdBikes)

            # se a locação tiver sido por SEMANA, opção 3
            else:
                conta = (math.ceil(tempoLocacao.seconds / 3600 / 24 / 7) * objCliente.qtdBikes) * 100
                #semanas = math.ceil(tempoLocacao.seconds / 3600 / 24 / 7) * objCliente.qtdBikes
                #conta = semanas * 100
                #conta = math.ceil((tempoLocacao.days / 7) * 100 * objCliente.qtdBikes)

            # verificação da promoção do desconto família
            if locacaoFamilia(objCliente.qtdBikes, objCliente) == True:
                conta = conta * 0.7
            else:
                #self.locacaoFamilia(objCliente.qtdBikes, objCliente) - desabilitei essa linha para que não o print que a promoção não era aplicável não aparecesse duas vezes
            
                self.conta = conta # e aqui, puxei pra identação do else

            # cliente devolve as bicicletas e retorna o valor que ele deve pagar
            print(f"Devolução de bicicletas aceita. O valor total da sua locação é de: R$ {conta}")
            return conta
        else:
            print("A locação não foi encontrada no sistema.")