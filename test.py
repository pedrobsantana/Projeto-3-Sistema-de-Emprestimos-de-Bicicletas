import unittest
import datetime
import main
from classes import Loja, Cliente

class TestaEmprestimoBikes(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente(0, 0, 0)
        self.loja = Loja(100)

    def testeMostraEstoque(self):
        print("\nTeste de LOJA - Mostrar Estoque")
        self.assertEqual(self.loja.mostrarEstoque(), 100)

    def testeLocacaoHoraComZeroBikes(self):
        print("\nTeste de LOJA - Locação HORA com 0 Bikes")
        self.assertEqual(self.loja.locacaoHora(0, True), None)

    def testLocacaoHoraAcimaDoEstoque(self):
        print("\nTeste de LOJA - Locação HORA de 150 Bikes, acima do estoque")
        self.assertEqual(self.loja.locacaoHora(150, True), None)

    def testeLocacaoHoraComDuasBikes(self):
        print("\nTeste de LOJA - Locação HORA com 2 Bikes")
        self.assertEqual(self.loja.locacaoHora(2, True), datetime.datetime.now())
    
    def testeLocacaoHoraComBikeNegativa(self):
        print("\nTeste de LOJA - Locação HORA com Bike Negativa")
        self.assertEqual(self.loja.locacaoHora(-1, True), None)

    def testeLocacaoDiaComZeroBikes(self):
        print("\nTeste de LOJA - Locação DIA com 0 Bikes")
        self.assertEqual(self.loja.locacaoDia(0, True), None)

    def testeLocacaoDiaComDuasBikes(self):
        print("\nTeste de LOJA - Locação DIA com 2 Bikes")
        self.assertEqual(self.loja.locacaoDia(2, True), datetime.datetime.now())
    
    def testeLocacaoDiaComBikeNegativa(self):
        print("\nTeste de LOJA - Locação DIA com Bike Negativa")
        self.assertEqual(self.loja.locacaoDia(-1, True), None)
    
    def testLocacaoDiaaAcimaDoEstoque(self):
        print("\nTeste de LOJA - Locação DIA de 150 Bikes, acima do estoque")
        self.assertEqual(self.loja.locacaoDia(150, True), None)

    def testeLocacaoSemanaComZeroBikes(self):
        print("\nTeste de LOJA - Locação SEMANA com 0 Bikes")
        self.assertEqual(self.loja.locacaoSemana(0, True), None)

    def testeLocacaoSemanaComDuasBikes(self):
        print("\nTeste de LOJA - Locação SEMANA com 2 Bikes")
        self.assertEqual(self.loja.locacaoSemana(2, True), datetime.datetime.now())
    
    def testeLocacaoSemanaComBikeNegativa(self):
        print("\nTeste de LOJA - Locação SEMANA com Bike Negativa")
        self.assertEqual(self.loja.locacaoSemana(-1, True), None)
    
    def testLocacaoSemanaAcimaDoEstoque(self):
        print("\nTeste de LOJA - Locação SEMANA de 150 Bikes, acima do estoque")
        self.assertEqual(self.loja.locacaoSemana(150, True), None)

    def testeLocacaoFamiliaComUmaBike(self):
        print("\nTeste de LOJA - Locação Família com apenas 1 Bike, não aplica o desconto")
        self.assertAlmostEqual(self.loja.locacaoFamilia(1, True), False)

    def testeLocacaoFamiliaCenarioIdeal(self):
        print("\nTeste de LOJA - Locação Família com 3 Bikes, Cenário Ideal")
        self.assertAlmostEqual(self.loja.locacaoFamilia(3, True), True)

    def testeLocacaoFamiliaComSeisBike(self):
        print("\nTeste de LOJA - Locação Família com 6 Bikes, não aplica o desconto")
        self.assertAlmostEqual(self.loja.locacaoFamilia(6, True), False)

    #def testeCalcularConta(self):
    #    print("\nTeste de LOJA - Calcular Conta")
    #    self.assertEqual(self.loja.calcularConta(2, True))

if __name__ == "__main__":
    unittest.main()